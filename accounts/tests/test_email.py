import os

from django.core.mail import EmailMessage
from django.test import override_settings
from django.test.testcases import SimpleTestCase


class TestEmailWelcome(SimpleTestCase):
    def test_send_email(self):
        """
        Ensure the welcome email is sent.
        """

        settings = {
            "DEBUG": True,
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
