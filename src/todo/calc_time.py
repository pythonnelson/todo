import datetime
from .models import *

currentDatetime = datetime.datetime.now()
#newTime = (datetime.datetime.combine(datetime.date(1, 1, 1), start_time) + datetime.timedelta(minutes=30)).time()

print(currentDatetime)