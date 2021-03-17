from django.shortcuts import render, redirect
from .models import ResultInput
from .forms import ResultsForm

# # 1-ый вариант:
# # Очень глупый, но другой придумать я не смог
# n = 0
# ihst = []
# while len(results) != n:
#     ihst.append((results[n].time * 100) / (results[n].f1+results[n].f2+results[n].f3)*2)
#     n += 1
# print(ihst)


def index(request):
    ihst = list()
    results = ResultInput.objects.all()
    for result in ResultInput.objects.all():
        ihst.append(
            {
                'id': result.id,
                'name': result.name,
                'result': result.time * 100 / (result.f1 + result.f2 + result.f3) * 2
            }
        )
    return render(request, 'main/index.html', {'title': 'Main page', 'results': results, 'ihst': ihst})


def create(request):
    error = ""
    if request.method == "POST":
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
