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

    def do_something(self, category: str, quiz_count: int) -> None:
        # TODO 카테고리에 대한 문제 셋팅해서 push 호출
        print(f"Do something")

    def make_scheduler(self, job_id: str, category: str, quiz_count: int) -> None:
        print(f"[Set scheduler] jobId: {job_id}")
        job_type = "cron"

        # TODO 유저 정보 불러와서 day_of_week, hour, minute 설정
        self.scheduler_obj.add_job(func=self.do_something(category=category, quiz_count=quiz_count),
                                   trigger=job_type, id=job_id, args=(job_type, job_id),
                                   day_of_week="", hour="", minute="")
