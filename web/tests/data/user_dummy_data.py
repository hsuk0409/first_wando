def get_user_success_dummy_data():
    return {
        "alarmName": "모닝 알람",
        "time": "05:30",
        "dayOfWeek": ["화", "수", "목", "금"],
        "category": "상식",  # TODO 상수로 변경
        "quizCount": 4,
        "isSound": True
    }


def get_user_fail_empty_time():
    return {
        "alarmName": "모닝 알람",
        "time": "",
        "dayOfWeek": ["화", "수", "목", "금"],
        "category": "상식",  # TODO 상수로 변경
        "quizCount": 4,
        "isSound": True
    }


def get_user_fail_wrong_time():
    return {
        "alarmName": "모닝 알람",
        "time": "05:30123",
        "dayOfWeek": ["화", "수", "목", "금"],
        "category": "상식",  # TODO 상수로 변경
        "quizCount": 4,
        "isSound": True
    }


def get_user_fail_empty_day_of_week():
    return {
        "alarmName": "모닝 알람",
        "time": "05:30",
        "dayOfWeek": [],
        "category": "상식",  # TODO 상수로 변경
        "quizCount": 4,
        "isSound": True
    }


def get_user_fail_none_category():
    return {
        "alarmName": "모닝 알람",
        "time": "05:30",
        "dayOfWeek": ["화", "수", "목", "금"],
        "category": None,  # TODO 상수로 변경
        "quizCount": 4,
        "isSound": True
    }


def get_user_fail_blank_category():
    return {
        "alarmName": "모닝 알람",
        "time": "05:30",
        "dayOfWeek": ["화", "수", "목", "금"],
        "category": "",  # TODO 상수로 변경
        "quizCount": 4,
        "isSound": True
    }
