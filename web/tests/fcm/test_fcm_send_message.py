from web.db import settings
from web.fcm.fcm_handler import FcmHandler


def test_send_message():
    fcm_service = FcmHandler(token=settings.TEST_FCM_TOKEN)
    message_body = {
        "message": "TEST"
    }
    result = fcm_service.send_message(message_body=message_body)
    print(result)

    assert result is not None
