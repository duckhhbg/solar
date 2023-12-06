# from django.test import TestCase

import datetime
from django.utils import timezone


# Create your tests here.

today = timezone.now()
first_day_of_month = today.replace(day=1)
last_day_of_month = first_day_of_month.replace(month=first_day_of_month.month % 12 + 1, day=1) - timezone.timedelta(days=1)

a = '2023-12-01'

print(type(a))
print(type(first_day_of_month.date()))