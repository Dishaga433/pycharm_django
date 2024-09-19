from django.shortcuts import render

from todo_app.form import TodoForm
from todo_app.models import Todo1


# Create your views here.
def dash(request):
     return render(request,"dashboard.html")

def index(request):
     data = TodoForm()
     if request.method=="POST":
          Todo1 = TodoForm(request.POST)
          if Todo1.is_valid():
               Todo1.save()

     return render(request,"index.html",{"form":data})

#read
def read(request):
     data=Todo1.objects.all()
     return render(request,"view.html",{'data':data})