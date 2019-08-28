from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from .forms import Task_form
from .models import Task_model
from . import templates 



# Create your views here.



def HomeTask_view (request):                    
    queryset = Task_model.objects.all()                                             #This will return a list of objects
    context = {                                                                     #Creating a dictionary that will contain the list 
        "task_list": queryset                                                           #Key Note: this code is reusable with any module(look below)
    }
    return render(request, 'ToDo_home.html', context)                               #Rendering that queryset(that now contains the list of tasks) onto the screen



#retrieving tasks: querying db for timefrime choices
def TodayTask_view (request):
    queryset = Task_model.objects.filter(timeframe='td')                               
    context = {                                                                      
        "task_list": queryset                                                       
    }
    return render(request, 'TodayTask.html', context)                                

def WeekTask_view (request):
    queryset = Task_model.objects.filter(timeframe='wk')                            
    context = {                                                                      
        "task_list": queryset                                                       
    }
    return render(request, 'WeekTask.html', context)     

def MonthTask_view (request):
    queryset = Task_model.objects.filter(timeframe='mnth')                          
    context = {                                                                      
        "task_list": queryset                                                       
    }
    return render(request, 'MonthTask.html', context)       

def SpareTimeTask_view (request):
    queryset = Task_model.objects.filter(timeframe='sp')                            
    context = {                                                                      
        "task_list": queryset                                                       
    }
    return render(request, 'SpareTimeTask.html', context)       
    

#In order to create, delete and Update, Im going to utilize classes and djangos built-in attributes 
class TaskCreate_view(LoginRequiredMixin, CreateView):
    model = Task_model
    fields = [
            'timeframe',
            'title', 
            'date', 
            'description',
            'completed',
            'author',
        ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdate_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task_model
    fields = [
            'timeframe',
            'title', 
            'date', 
            'description',
            'completed',
        ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:                                        #ensures the current user is the author of the task 
            return True
        return False

class TaskDelete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task_model
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

def CrossoffTask_view(request, task_id):
    Task = Task_model.objects.get(pk = task_id)
    Task.completed = True
    messages.success(request, ("Well Done!"))
    Task.save()
    return HttpResponseRedirect('/')
    


def UncrossTask_view(request, task_id):
    Task = Task_model.objects.get(pk=task_id)
    Task.completed = False
    Task.save()
    return HttpResponseRedirect('/')


    
    
    
    
    






