from web.db import settings
from web.fcm.fcm_handler import FcmHandler


def test_send_message():
    fcm_service = FcmHandler(token=settings.TEST_FCM_TOKEN)
    message_body = {
        "message": "알람 이름",
        "questions": {
            "name": "justin",
            "quiz_count": 4
        }
    }
    result = fcm_service.send_message(message_body=message_body)

    assert result is not None
