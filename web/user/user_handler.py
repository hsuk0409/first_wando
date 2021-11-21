
class UserHandler:

    def __init__(self, request):
        self.request = request

    def register_user(self):
        pass

    def verify_request_data(self) -> bool:
        if not self.request:
            return False
        # args = self.request.args
        args = self.request
        # 시간 체크
        request_time = args.get("time")
        if not request_time:
            notice_error_field("time")
            return False
        divide_times = str(request_time).split(":")
        if len(divide_times[0]) > 2 or len(divide_times[1]) > 2:
            notice_error_field("time")
            return False

        # 요일 체크
        day_of_weeks = args.get("dayOfWeek")
        if len(day_of_weeks) < 1:
            notice_error_field("dayOfWeek")
            return False

        # 카테고리 체크
        category = args.get("category")
        if not category:
            notice_error_field("category")
            return False

        return True


def notice_error_field(filed_name: str) -> None:
    # TODO 로그로 변경
    print(f"{filed_name}값이 비어있거나 잘못 되어 있습니다.")
