from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Task
from schemas import TaskCreate, TaskResponse
from scheduler import add_task_to_scheduler
import asyncio
from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}

@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(
        name=task.name,
        description=task.description,
        schedule=task.schedule,
        status="Scheduled",
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    # Schedule the task
    add_task_to_scheduler(db_task.id, db_task.schedule, lambda: run_task(db_task.id, db))

    return db_task

@app.get("/tasks/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

async def run_task(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = "Running"
        task.last_run_time = datetime.now()
        db.commit()

        # Simulate task execution
        await asyncio.sleep(3)

        task.status = "Completed"
        db.commit()

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get(app.openapi_url, include_in_schema=False)
async def openapi_json_url():
    return get_openapi(
        title=app.title + " - OpenAPI JSON",
        version=app.version,
        routes=app.routes,
    )

