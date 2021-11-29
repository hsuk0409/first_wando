from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler


class UserScheduler:

    def __init__(self):
        self.scheduler_obj = BackgroundScheduler()
        self.scheduler_obj.start()

    def __del__(self):
        self.scheduler_obj.shutdown()

    def kill_scheduler(self, job_id: str) -> None:
        try:
            self.scheduler_obj.remove_job(job_id=job_id)
        except JobLookupError as e:
            print(f"fail to stop scheduler: {str(e)}")
            return

    def do_something(self, job_type: str, job_id: str) -> None:
        print(f"Do something")

    def make_scheduler(self, job_type: str, job_id: str, category: str, quiz_count: int) -> None:
        print(f"Set scheduler")
