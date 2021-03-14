from django.shortcuts import render, redirect
from .models import Results
from .forms import ResultsForm


def index(request):
    results = Results.objects.all()
    n = 0
    # 1-ый вариант
    while len(results) != n:
        ihst = (results[n].time * 100) / (results[n].f1+results[n].f2+results[n].f3)*2
        print(ihst)
        n += 1

    # 2-ой вариант
    # for i in results:
    #     ihst_2 = i[0].time * 100
    #     print(ihst_2)

    return render(request, 'main/index.html', {'title': 'Main page', 'results': results})


def create(request):
    error = ""
    if request.method == "POST":
        # from Skillbox
        person = [
            request.POST.get('name'),
            request.POST.get('age'),
            request.POST.get('time'),
            request.POST.get('f1'),
            request.POST.get('f2'),
            request.POST.get('f3')]
        print(person)

        form = ResultsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Something going wrong"

    form = ResultsForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)


def about(request):
    return render(request, 'main/about.html')
