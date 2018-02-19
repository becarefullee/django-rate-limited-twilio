Django Rate Limited Twilio
==============

A reusable Django app for using with Twilio.  Limits the number of of text messages that can be sent to a phone number over a period of time.

Installing the App
==============

1. Add "-e git+http://compepi.cs.uiowa.edu:9000/eli/django-rate-limited-twilio.git@master#egg=django-rate-limited-twilio" to requirements
2. Install requirements with pip.
3. Add ``rate_limited_twilio`` to ``installed_apps`` in settings.py
4. Run "python manage.py migrate"
5. Add your Twilio Credentials in settings.py (``TWILIO_ACCOUNT_SID = "XXXXXXXXXXXXXXXXXX"`` ``TWILIO_AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXX"``)
6. Import ``twilio_client`` instance from ``rate_limited_twilio.client`` model, then use the ``twilio_client`` instance as regular twilio client instance
7. (Optional) The default rate limit for each number is 5 messages per 30 mins. You can change this by adding ``MESSAGES_PER_TIME_PERIOD`` (int) and ``RATE_LIMIT_TIME_PERIOD`` (timedelta) settings to settings.py.

