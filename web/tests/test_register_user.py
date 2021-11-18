from web.tests.data.user_dummy_data import get_user_fail_empty_time, get_user_fail_wrong_time
from web.user.user_handler import UserHandler


def test_user_verify_fail_empty_time():
    request_data = get_user_fail_empty_time()

    handler = UserHandler(request=request_data)
    verify_result = handler.verify_request_data()

    assert verify_result == False


def test_user_verify_fail_empty_time():
    request_data = get_user_fail_wrong_time()

    handler = UserHandler(request=request_data)
    verify_result = handler.verify_request_data()

    assert verify_result == False
