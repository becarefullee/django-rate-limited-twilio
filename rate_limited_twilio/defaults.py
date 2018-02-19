import datetime

# The number of messages that can be sent to a single phone
# number over RATE_LIMIT_TIME_PERIOD
MESSAGES_PER_TIME_PERIOD = 5

# The period of time after which we refresh the number of
# messages each phone number can receive
RATE_LIMIT_TIME_PERIOD = datetime.timedelta(minutes=30)
