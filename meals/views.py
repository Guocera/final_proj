from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import PlanForm

def demo(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      calories = form.cleaned_data['calories']
      return HttpResponseRedirect('/meals/')
  else:
    form = PlanForm()

  return render(request, 'meals/demo.html', {'form': form})

def index(request):
  context = {
    'first_name': "Hatim"
  }
  return render(request, 'meals/index.html', context)