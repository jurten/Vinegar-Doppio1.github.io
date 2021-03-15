from django.shortcuts import render
from .forms import TurnForm
from .models import Turn

# Create your views here.
def turn_detailed_view(request):
    form = TurnForm
    if request.method == "POST":
        form = TurnForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "turn_form.html", context)
