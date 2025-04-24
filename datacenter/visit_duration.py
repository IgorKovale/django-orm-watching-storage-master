import django
from datacenter.models import Visit

def get_duration(visit):
    time_now = django.utils.timezone.localtime()
    enter_localtime = django.utils.timezone.localtime(visit.entered_at)
    if visit.leaved_at is None:
        duration = time_now-enter_localtime
    else:
        leaved_localtime=django.utils.timezone.localtime(visit.leaved_at)
        duration = leaved_localtime-enter_localtime
    return duration

def format_duration(duration):
    total_seconds = duration.total_seconds()
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 3600) % 60
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    duration_minutes = duration.total_seconds()/60
    return duration_minutes > minutes