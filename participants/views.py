from django.shortcuts import render
from .forms import PaticipantForm
from .models import Participant

#Registration Page
def register_participant(request):
    form = ParticipantForm()
    if request.method == 'POST';
    form = ParticipantForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('thank_you') #redirect to thank you page
    return render(request, 'participants/register.html', {'form': form})

#Admin Dashboard 
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    participants = Participant.objects.all()
    return render(request,'participants/dashboard.html', {'participants': participants})