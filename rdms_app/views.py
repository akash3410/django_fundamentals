from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Todo

# Create your views here.
def home_page(request):
    return render(request, 'rdms/home.html')

def view_by_userId(request, user_id):
    # todos = Todo.objects.filter(user_id=user_id).values()
    # return JsonResponse({'todos': list(todos)})
    
    # OR Acess todos from user module
    user = User.objects.get(pk=user_id)
    todos = user.todos.all().values()
    return JsonResponse({'todos': list(todos)})
       