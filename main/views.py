from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(name)
        print(message)
    return render(request, 'main/index.html')
