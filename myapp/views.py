from django.shortcuts import render
from django.http import HttpResponse

def initial_load(request):
    return HttpResponse("This is landing Page")

def home_page(request, username=None):
    if username == None:
        username = "Marry"
    page_name = {'name': "Home Page", "username": username}
    return render(request, "home.html", page_name)

def about(request):
    page_name = "about page"
    link_site = [
        "Facebook: fb.me/example",
        "Youtube: youtube.com/userid",
        "LinkedIn: linkedin.com/username",
        "Instagram: instagram.com/username"
    ]
    return render(request, "about.html", {"name": page_name, "link_site": link_site})

def work(request):
    return render(request, "work.html")

def images(request):
    return render(request, "images.html")
