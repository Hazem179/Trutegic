from datetime import datetime, date, timedelta
from .models import AvailableTimes
from collections import defaultdict

free_days = []
available_days = []
available_hours = []
days_set = []
hours_set = []
reservations = defaultdict(list)
delt = timedelta(minutes=30)


def available_days_filter(id):
    today = date.today()
    available_days_db = AvailableTimes.objects.filter(advisor__type=id, state='available')

    for time in available_days_db:
        free_days.append(time.day)
        available_hours.append(time.from_hour)

    for i in range(len(free_days)):
        delta = free_days[i] - today
        if delta.days > 1:
            available_days.append(free_days[i])

    open_days = AvailableTimes.objects.filter(advisor__type=id, state='available', day__in=available_days)
    for dates in range(len(open_days)):
        day = open_days[dates].day
        key = day.strftime("%m/%d/%Y")
        from_hours = open_days[dates].from_hour
        to_hours = open_days[dates].to_hour
        split_hours = convert_to_half(from_hours, to_hours)
        for i in range(split_hours):
            new_from = datetime.combine(day, from_hours)
            hours_set.append(from_hours)
            added_time = (new_from + delt).time()
            from_hours = added_time
            days_set.append(day)
    print(hours_set)


    return available_days


def convert_to_half(from_hour, to_hour):
    h1 = timedelta(hours=from_hour.hour, minutes=from_hour.minute)
    h2 = timedelta(hours=to_hour.hour, minutes=to_hour.minute)
    hours = h2 - h1
    final = hours.seconds / 1800
    return int(final)
