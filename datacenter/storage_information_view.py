from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_duration import format_duration
from datacenter.visit_duration import get_duration
from django.shortcuts import render
import django

def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        non_closed_visit = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': django.utils.timezone.localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
