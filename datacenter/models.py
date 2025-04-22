from django.db import models
import django

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

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