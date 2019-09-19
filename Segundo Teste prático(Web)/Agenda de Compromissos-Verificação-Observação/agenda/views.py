from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .forms import ObsForm
from .models import Commitment, Observations

# Create your views here.
def index(request):

    latest_commitment_list = Commitment.objects.order_by('schedule')[:15]

    context = {
        'latest_commitment_list': latest_commitment_list,
        }

    return render(request, 'agenda/index.html', context)


def detail(request, commitment_id):
    
    commitment = get_object_or_404(Commitment, pk=commitment_id)
    
    new_form = ObsForm()

    if request.method == "POST":
        old_form = ObsForm(request.POST or None)
        if old_form.is_valid():
            old_form = old_form.save(commit=False)
            old_form.fk_commitment = commitment
            old_form.save()

    observations = list(Observations.objects.filter(fk_commitment=commitment_id))

    context = {
        'commitment': commitment,
        'observations': observations,
        'form': new_form,
    }

    return render(request, 'agenda/detail.html', context)