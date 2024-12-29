from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    description: str
    schedule: str  # Cron expression

class TaskResponse(TaskCreate):
    id: int
    status: str
    last_run_time: str | None = None

    class Config:
        orm_mode = True
