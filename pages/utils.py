from datetime import datetime, date, timedelta
from .models import AvailableTimes
from collections import defaultdict
import time

delt = timedelta(minutes=30)


def available_days_filter(id):
    free_weekdays = []
    available_reservation_dates = []
    days_dict = {}
    today = date.today()
    # Store available consultation object based on selected type
    consultation_type_free_days = AvailableTimes.objects.filter(advisor__type=id, state='available')

    # Store days and hours of objects
    for obj in consultation_type_free_days:
        free_weekdays.append(obj.day)
    # Store available reservations dates based on how far it from today
    for i in range(len(free_weekdays)):
        day_date = date_for_weekday(free_weekdays[i])
        delta = day_date - today
        if delta.days > 1:
            available_reservation_dates.append(day_date)
            days_dict[free_weekdays[i]] = day_date
    free_weekdays_objects = AvailableTimes.objects.filter(advisor__type=id, state='available', day__in=days_dict.keys())
    hr =  free_intervals(consultation_type_free_days)

    return consultation_type_free_days


def free_intervals(open_days):
    free_hours = []

    for dates in range(len(open_days)):
        day = date_for_weekday(open_days[dates].day)
        from_hours = open_days[dates].from_hour
        to_hours = open_days[dates].to_hour
        split_hours = convert_to_half(from_hours, to_hours)
        for i in range(split_hours + 1):
            new_from = datetime.combine(day, from_hours)
            free_hours.append(from_hours)
            added_time = (new_from + delt).time()
            from_hours = added_time

    return free_hours


def convert_to_half(from_hour, to_hour):
    h1 = timedelta(hours=from_hour.hour, minutes=from_hour.minute)
    h2 = timedelta(hours=to_hour.hour, minutes=to_hour.minute)
    hours = h2 - h1
    final = hours.seconds / 1800
    return int(final)


def date_for_weekday(day_name: str):
    day = time.strptime(day_name, "%A").tm_wday
    today = date.today()
    weekday = today.weekday()
    return today + timedelta(days=day - weekday)


def convert_hours(hours_list: list):
    hours = []
    for hour in range(len(hours)):
        hour.strftime("%H:%M:%S")
        hours.append(hour)

    return hours
