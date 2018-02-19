from celery.decorators import periodic_task

from .models import RateLimitedPhoneNumber
from .utils import get_setting


@periodic_task(run_every=(get_setting('RATE_LIMIT_TIME_PERIOD')))
def reset_rate_limits():
    """
    Reset the number of messages that can be sent to all phone numbers
    every RATE_LIMIT_TIME_PERIOD
    """
    for rate_limit in RateLimitedPhoneNumber.objects.all():
        rate_limit.messages_remaining = get_setting('MESSAGES_PER_TIME_PERIOD')
        rate_limit.save()
