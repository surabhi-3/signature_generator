from django.shortcuts import render

def index(request):
    signature = None
    font = None
    if request.method == "POST":
        name = request.POST.get('name')
        font = request.POST.get('font')
        signature = name
    return render(request, 'generator/index.html', {'signature': signature, 'font': font})
