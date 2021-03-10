from django.shortcuts import render, redirect
from .models import Results
from .forms import ResultsForm


def index(request):
    results = Results.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', 'results': results})


def create(request):
    error = ""
    if request.methods == "POST":
        form = ResultsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Something is wrong"

    form = ResultsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def about(request):
    return render(request, 'main/about.html')
