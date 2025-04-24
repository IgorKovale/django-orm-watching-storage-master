from django.utils.timezone import localtime


def get_duration(visit):
    time_now = localtime()
    enter_localtime = localtime(visit.entered_at)
    if not visit.leaved_at:
        duration = time_now-enter_localtime
    else:
        leaved_localtime=localtime(visit.leaved_at)
        duration = leaved_localtime-enter_localtime
    return duration

def format_duration(duration):
    total_seconds = duration.total_seconds()
    seconds_in_hour = 3600
    seconds_in_minute=60
    hours = total_seconds // seconds_in_hour
    minutes = (total_seconds % seconds_in_hour) // seconds_in_minute
    seconds = (total_seconds % seconds_in_hour) % seconds_in_minute
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    duration_minutes = duration.total_seconds()/60
    return duration_minutes > minutes