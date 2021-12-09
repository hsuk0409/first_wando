from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
from bson import ObjectId

from web.db.db_manager import DBManager

dbm = DBManager.get_instance()


class UserScheduler:

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
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

    def make_scheduler(self) -> None:
        print(f"[Set scheduler] user_id: {self.user_id}")
        job_type = "cron"
        job_id = self.user_id

        user = dbm.find_one(collection="WANDO_USER", where={"_id": ObjectId(self.user_id)})
        category = user.get("category")
        quiz_count = user.get("quiz_count")
        converted_day_of_week = convert_day_of_week(day_of_week_list=user.get("day_of_week"))
        time_str = user.get("time")
        hour = str(time_str).split(":")[0]
        minute = str(time_str).split(":")[1]

        self.scheduler_obj.add_job(func=self.do_something(category=category, quiz_count=quiz_count),
                                   trigger=job_type, id=job_id, args=(job_type, job_id),
                                   day_of_week=converted_day_of_week, hour=hour, minute=minute)


def convert_day_of_week(day_of_week_list: list) -> str:
    # TODO day_of_week 리스트를 scheduler.add_job day_of_week 파라미터 포맷에 맞춰서 컨버팅한다.
    return ""
