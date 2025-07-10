from django.shortcuts import render

# Create your views here.
# function-based view
def home_view(request):
    return render(request,'pages/home.html')

def about_me_view(request):
    return render(request,'pages/about_me.html')
