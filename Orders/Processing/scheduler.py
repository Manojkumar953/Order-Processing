from apscheduler.schedulers.background import BackgroundScheduler
from .queue import scan_queue


# scheduler that runs every minute scans the queue and calls the worker for each event inside the queue
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scan_queue, 'interval', minutes=1)  # Runs every minute
    scheduler.start()