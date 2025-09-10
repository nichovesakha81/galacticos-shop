from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495804',
        'name': 'Nicholas Vesakha',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)