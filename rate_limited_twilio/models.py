from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


@python_2_unicode_compatible
class RateLimitedPhoneNumber(models.Model):
    """
    A RateLimitedPhoneNumber is defined uniquely by their phone
    number.
    :param char phone_number: Unique phone number in `E.164
        <http://en.wikipedia.org/wiki/E.164>`_ format.
    :param int messages_remaining: The number of messages we
        can send this phone number before the limit is hit.
    """
    phone_number = PhoneNumberField(unique=True)
    messages_remaining = models.PositiveIntegerField()

    def __str__(self):
        return '{phone_number}'.format(
            phone_number=str(self.phone_number)
        )
