from django.test import TestCase
from django.conf import settings

from mock import patch

from rate_limited_twilio.client import twilio_client, RateLimitedClient, RateLimitedMessages
from rate_limited_twilio.models import RateLimitedPhoneNumber
from rate_limited_twilio.utils import get_setting


class TwilioClientTestCase(TestCase):
    def test_twilio_client_exists(self):
        """
        A RateLimitedClient object should be created
        """
        self.assertIsInstance(twilio_client, RateLimitedClient)

    def test_twilio_client_sets_credentials(self):
        """
        twilio_client credentials should be able to be configured
        manually
        """
        self.assertEqual(
            twilio_client.auth,
            (settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        )

    def test_twilio_client_uses_rate_limited_messages(self):
        """
        twilio_client.messages should be overridden with our custom
        RateLimitedMessages
        """
        self.assertIsInstance(twilio_client.messages, RateLimitedMessages)


class RateLimitedMessagesTestCase(TestCase):
    def setUp(self):
        self.valid_from_number = get_setting('TWILIO_TEST_SENDER_NUMBER')
        self.valid_to_number = get_setting('TWILIO_TEST_RECEIVER_NUMBER')

    def test_rate_limited_phone_number_created(self):
        """
        When we send a message to a new number, we should create a
        RateLimitedPhoneNumber objects with that phone number.
        """
        twilio_client.messages.create(
            from_=self.valid_from_number, to=self.valid_to_number, body='test_rate_limited_phone_number_created')
        rate_limit_phone_number = RateLimitedPhoneNumber.objects.get(phone_number=self.valid_to_number)
        self.assertEqual(rate_limit_phone_number.messages_remaining, 4)

    def test_rate_limited_phone_number_decreased_on(self):
        """
        When we send a message to a number, we should decrease the
        number of messages remaining for that number.
        """
        messages_allowed = 5
        rate_limit_phone_number = RateLimitedPhoneNumber.objects.create(
            phone_number=self.valid_to_number,
            messages_remaining=messages_allowed)
        twilio_client.messages.create(
            from_=self.valid_from_number, to=self.valid_to_number, body='test_rate_limited_phone_number_decreased_on')
        rate_limit_phone_number = RateLimitedPhoneNumber.objects.get(
            pk=rate_limit_phone_number.pk)
        messages_after = rate_limit_phone_number.messages_remaining
        print(messages_after)
        self.assertEqual(messages_allowed - messages_after, 1)

    @patch('twilio.rest.api.v2010.account.message.MessageList.create')
    def test_rate_limited_phone_number_stops_send(self, create):
        """
        When a number reaches 0 messages remaining, we should no longer
        be able to send them messages.
        """
        RateLimitedPhoneNumber.objects.create(
            phone_number=self.valid_to_number, messages_remaining=0)
        twilio_client.messages.create(
            from_=self.valid_from_number, to=self.valid_to_number, body='test_rate_limited_phone_number_stops_send')
        self.assertFalse(create.called)

    @patch('twilio.rest.api.v2010.account.message.MessageList.create')
    def test_rate_limited_phone_number_sends(self, create):
        """
        We should be able to send messages to phone numbers that still
        have messages remaining.
        """
        twilio_client.messages.create(
            from_=self.valid_from_number, to=self.valid_to_number, body='test_rate_limited_phone_number_sends')
        self.assertTrue(create.called)

    @patch('twilio.rest.api.v2010.account.message.MessageList.create')
    def test_rate_limited_phone_number_no_to(self, create):
        """
        When no 'to' number is passed to a RateLimitedMessage object,
        we allow the Message object to handle the error.
        """
        twilio_client.messages.create(
            from_=self.valid_from_number, body='test_rate_limited_phone_number_no_to')
        self.assertTrue(create.called)