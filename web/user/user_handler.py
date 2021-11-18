
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
            return False
        divide_times = str(request_time).split(":")
        if len(divide_times[0]) > 2 or len(divide_times[1]) > 2:
            return False

        return True
