from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
from bson import ObjectId

from web.db.db_manager import DBManager
from web.fcm.fcm_handler import FcmHandler

dbm = DBManager.get_instance()


class UserScheduler:

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        user = dbm.find_one(collection="WANDO_USER", where={"_id": ObjectId(user_id)})
        self.category = user.get("category")
        self.quiz_count = user.get("quizCount")
        self.fcm_token = user.get("fcmToken")
        self.day_of_week = convert_day_of_week(day_of_week_list=user.get("dayOfWeek"))
        self.time_str = user.get("time")

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

    def _make_quiz(self) -> None:
        request_body = {}
        # TODO 카테고리에 대한 문제 셋팅
        
        # 파이어베이스 푸시 알림 전송
        fcm_service = FcmHandler(token=self.fcm_token)
        fcm_service.send_message(message_body=request_body)

    def make_scheduler(self) -> None:
        hour = str(self.time_str).split(":")[0]
        minute = str(self.time_str).split(":")[1]

        job_type = "cron"
        job_id = self.user_id
        self.scheduler_obj.add_job(func=self._make_quiz,
                                   trigger=job_type, id=job_id, args=(job_type, job_id),
                                   day_of_week=self.day_of_week, hour=hour, minute=minute)


def convert_day_of_week(day_of_week_list: list) -> str:
    # TODO day_of_week 리스트를 scheduler.add_job day_of_week 파라미터 포맷에 맞춰서 컨버팅한다.
    return ""
