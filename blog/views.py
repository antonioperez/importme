from django.shortcuts import render

# Create your views here.
def BlogFront(request):
    return render(request, 'blog/front.html', {'question': 'question'})