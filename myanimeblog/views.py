from django.shortcuts import render

# Create your views here.


def frontpage(request):
    return render(request, 'myanimeblog/frontpage.html')

def about(request):
    return render(request, 'myanimeblog/about.html')