from web.user.user_scheduler import convert_day_of_week


def test_convert_all_day_of_week():
    months = ['월', '화', '수', '목', '금', '토', '일']

    result = convert_day_of_week(day_of_week_list=months)

    assert result == '0-6'
