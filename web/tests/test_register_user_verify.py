from web.tests.data.user_dummy_data import get_user_fail_empty_time, get_user_fail_wrong_time, \
    get_user_fail_empty_day_of_week, get_user_fail_none_category, get_user_fail_blank_category, \
    get_user_success_dummy_data
from web.user.user_handler import verify_request_data


def test_user_verify_fail_empty_time():
    request_data = get_user_fail_empty_time()

    verify_result = verify_request_data(data_to_be_verified=request_data)

    assert verify_result == False


def test_user_verify_fail_wrong_time():
    request_data = get_user_fail_wrong_time()

    verify_result = verify_request_data(data_to_be_verified=request_data)

    assert verify_result == False


def test_user_verify_fail_empty_day_of_week():
    request_data = get_user_fail_empty_day_of_week()

    verify_result = verify_request_data(data_to_be_verified=request_data)

    assert verify_result == False


def test_user_verify_fail_none_category():
    request_data = get_user_fail_none_category()

    verify_result = verify_request_data(data_to_be_verified=request_data)

    assert verify_result == False


def test_user_verify_fail_blank_category():
    request_data = get_user_fail_blank_category()

    verify_result = verify_request_data(data_to_be_verified=request_data)

    assert verify_result == False
