from django.shortcuts import render
from .forms import PaticipantForm
from .models import Participant
from django.contrib.auth.decorators import login_required
from reportlab.pdfgrn import canvas

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


@login_required
def admin_dashboard(request):
    participants = Participant.objects.all()
    return render(request,'participants/dashboard.html', {'participants': participants})

@login_required
def print_neck_tags(request):
    response = HttpsResponse(content_type='application/pdf')
    response['Content-Disoposition'] = 'inline; filename="neck_tags.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    participants = Participant.objects.all()
    
    x, y = 50, 750
    for participant in participants
    p.drawString(x, y, f"Name: {participant.first_name} {participant.last_name}")
    p.drawString(x, y-15, f"Occupation: {participant.occupation}")
    p.drawString(x, y-30, f"Company: {participant.company}")
    y-= 50
    if y < 50:
        y = 750
        p.showPage()
        
    p.save()
    return response