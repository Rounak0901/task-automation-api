from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def add_task_to_scheduler(task_id: int, schedule: str, func):
    parts = schedule.split()  # Assuming a cron expression
    scheduler.add_job(func, 'cron', id=str(task_id), minute=parts[0], hour=parts[1], day=parts[2], month=parts[3], day_of_week=parts[4])

def remove_task_from_scheduler(task_id: int):
    scheduler.remove_job(str(task_id))
