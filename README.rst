Django Rate Limited Twilio
==============

A reusable Django app for using with Twilio.  Limits the number of of text messages that can be sent to a phone number over a period of time.

Installing the App
==============

1. Add "-e git+http://compepi.cs.uiowa.edu:9000/eli/django-rate-limited-twilio.git@master#egg=django-rate-limited-twilio" to requirements
2. Install requirements with pip.
3. Add ``rate_limited_django_twilio to`` ``installed_apps`` in settings.py
4. Run "python manage.py migrate"
5. Replace all instances of ``django_twilio.client.twilio_client`` (that need to be rate limited) with ``rate_limited_django_twilio.client.twilio_client``
6. (Optional) Add ``MESSAGES_PER_TIME_PERIOD`` (int) and ``RATE_LIMIT_TIME_PERIOD`` (timedelta) settings to settings.py.

