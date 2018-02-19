from twilio.rest import Client
from twilio.rest.api.v2010.account import MessageList
import logging

from .models import RateLimitedPhoneNumber
from .utils import get_setting


logger = logging.getLogger(__name__)


class RateLimitedMessages(MessageList):
    """
    A wrapper around Messages to limit the number of messages sent
    in a given period of time.
    """
    def create(self, *args, **kwargs):
        # Use default error handling if there is no 'to'
        if 'to' not in kwargs.keys():
            return super(RateLimitedMessages, self).create(*args, **kwargs)
        else:
            phone_number = RateLimitedPhoneNumber.objects.filter(
                phone_number=kwargs['to']).first()
            if phone_number:
                # Rate limit if too many messages have been sent
                if phone_number.messages_remaining == 0:
                    logger.warning(
                        'Too many messages were sent to {}.  The message '
                        '"{}" will not be sent.'.format(
                            kwargs['to'], kwargs['body']))
                    return
                else:
                    phone_number.messages_remaining = \
                        phone_number.messages_remaining - 1
                    phone_number.save()
            else:
                print("The first time we see this number.")
                # The first time we see a phone number
                RateLimitedPhoneNumber.objects.create(
                    phone_number=kwargs['to'],
                    messages_remaining= get_setting(
                        'MESSAGES_PER_TIME_PERIOD') - 1)
        return super(RateLimitedMessages, self).create(*args, **kwargs)


class RateLimitedClient(Client):
    """
    A subclass of twilio.rest.Client. Override getter of the messages property
    to return our custom message class instead. 
    """
    @Client.messages.getter
    def messages(self):
        """
        :rtype: RateLimitedMessages
        """
        return RateLimitedMessages(self.api.v2010, self.account_sid)


# # Your Auth Token from twilio.com/console

account_sid = get_setting('TWILIO_ACCOUNT_SID')
auth_token = get_setting('TWILIO_AUTH_TOKEN')

twilio_client = RateLimitedClient(account_sid, auth_token)

