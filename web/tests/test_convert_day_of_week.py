from web.user.user_scheduler import convert_day_of_week


def test_convert_all_day_of_week():
    months = ['월', '화', '수', '목', '금', '토', '일']

    result = convert_day_of_week(day_of_week_list=months)

    assert result == 'mon,tue,wed,thu,fri,sat,sun'


def test_convert_mon_sun():
    months = ['월', '일']

    result = convert_day_of_week(day_of_week_list=months)

    assert result == 'mon,sun'


def test_convert_mon_wed_fri_sun():
    months = ['월', '수', '금', '일']

    result = convert_day_of_week(day_of_week_list=months)

    assert result == 'mon,wed,fri,sun'
