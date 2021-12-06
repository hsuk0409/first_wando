from web.db.db_manager import DBManager
from web.user.user_scheduler import UserScheduler


class UserHandler:

    def __init__(self, request):
        self.request_data = request.json
        self.dbm = DBManager.get_instance()

    def register_user(self):
        # 리퀘스트 체크
        if not verify_request_data(self.request_data):
            return {"return_code": 401, "message": "요청 데이터가 잘못 되었습니다. 다시 확인해주세요."}

        user_id = self.dbm.insert_one(collection="wando_test", document=self.request_data)
        print(f"[Register User] DB Insert Result:; {user_id}")

        scheduler = UserScheduler(user_id=user_id)
        scheduler.make_scheduler()


def verify_request_data(data_to_be_verified: dict) -> bool:
    json_data = data_to_be_verified
    if not json_data:
        return False
    # 시간 체크
    request_time = json_data.get("time")
    if not request_time:
        notice_error_field("time")
        return False
    divide_times = str(request_time).split(":")
    if len(divide_times[0]) > 2 or len(divide_times[1]) > 2:
        notice_error_field("time")
        return False

    # 요일 체크
    day_of_weeks = json_data.get("dayOfWeek")
    if len(day_of_weeks) < 1:
        notice_error_field("dayOfWeek")
        return False

    # 카테고리 체크
    category = json_data.get("category")
    if not category:
        notice_error_field("category")
        return False

    return True


def notice_error_field(filed_name: str) -> None:
    # TODO 로그로 변경
    print(f"{filed_name}값이 비어있거나 잘못 되어 있습니다.")
