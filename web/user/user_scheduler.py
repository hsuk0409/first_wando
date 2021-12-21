from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
from bson import ObjectId

from web.db.db_manager import DBManager
from web.fcm.fcm_handler import FcmHandler
from web.user.alarm_type import AlarmType
from web.user.quiz_type import QuizType

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
        request_body = {
            "alarmType": AlarmType.ALARM,
            "quizType": self._get_quiz_type(),
            "quiz": self._get_quiz()
        }

        # 파이어베이스 푸시 알림 전송
        fcm_service = FcmHandler(token=self.fcm_token)
        fcm_service.send_message(message_body=request_body)

    def _get_quiz_type(self) -> str:
        # TODO 카테고리에 따른 퀴즈 타입 반환
        return ""

    def _get_quiz(self) -> dict:
        # TODO 카테고리에 따른 퀴즈 반환
        return {}

    def make_scheduler(self) -> None:
        hour = str(self.time_str).split(":")[0]
        minute = str(self.time_str).split(":")[1]

        job_type = "cron"
        job_id = self.user_id
        self.scheduler_obj.add_job(func=self._make_quiz,
                                   trigger=job_type, id=job_id, args=(job_type, job_id),
                                   day_of_week=self.day_of_week, hour=hour, minute=minute)


def convert_day_of_week(day_of_week_list: list) -> str:
    convert_dic = {
        "월": "mon",
        "화": "tue",
        "수": "wed",
        "목": "thu",
        "금": "fri",
        "토": "sat",
        "일": "sun"
    }

    result = ""
    for dow in day_of_week_list:
        if convert_dic.get(dow):
            result = result + "," + convert_dic.get(dow)

    return result[1:]
