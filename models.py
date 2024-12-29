from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    schedule = Column(String)  # Cron expression
    status = Column(String, default="Pending")
    last_run_time = Column(DateTime, nullable=True)
