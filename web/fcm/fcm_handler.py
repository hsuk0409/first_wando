from pyfcm import FCMNotification

from web.db import settings


class FcmHandler:

    def __init__(self, token: str) -> None:
        self.fcm_service = FCMNotification(api_key=settings.FCM_API_KEY)
        self.token = token

    def send_message(self, message_body: dict):
        data_message = {
            "title": "시계는 와치",
            "body": message_body
        }

        result = self.fcm_service.single_device_data_message(registration_id=self.token,
                                                             content_available=True,
                                                             data_message=data_message)

        return result
