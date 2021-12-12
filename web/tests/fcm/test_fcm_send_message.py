from web.db import settings
from web.fcm.fcm_handler import FcmHandler


def test_send_message():
    fcm_service = FcmHandler(token=settings.TEST_FCM_TOKEN)
    message_body = {
        "message": "TEST"
    }
    result = fcm_service.send_message(title="시계는 와치 테스트 메시지", message_body=message_body)
    print(result)

    assert result is not None
