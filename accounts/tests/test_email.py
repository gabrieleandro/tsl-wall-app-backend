import os

from django.core.mail import EmailMessage
from django.test import override_settings
from django.test.testcases import SimpleTestCase


class TestPostToSendgrid(SimpleTestCase):
    def test_post(self):
        """
        Sends a POST to sendgrid's live API using a private API key.
        """

        SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

        settings = {
            "DEBUG": True,
            "SENDGRID_API_KEY": SENDGRID_API_KEY,
            "EMAIL_BACKEND": "sendgrid_backend.SendgridBackend",
        }

        with override_settings(**settings):
            msg = EmailMessage(
                subject="Hello, World!",
                body="Hello, World!",
                from_email="Tester Beta <tester@tsl.io>",
                to=["Tester Beta <tester@tsl.io>"],
            )
            val = msg.send()
            self.assertEqual(val, 1)
