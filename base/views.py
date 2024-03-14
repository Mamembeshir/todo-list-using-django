from django.shortcuts import redirect
from .models import Task
from django.urls import reverse_lazy

from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Customlogin(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
class RegistrationPage(FormView):
    template_name='base/registration.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    def form_valid(self,form):
        user=form.save()
        if user:
            login(self.request,user) 
        return super(RegistrationPage,self).form_valid(form)
    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args,**kwargs)
    
    
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    fields='__all__'
    context_object_name='tasks'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        return context
    
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    template_name='base/create_task.html'
    fields=['title','description','completed']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)
    success_url=reverse_lazy('tasks')
    
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    template_name='base/update_task.html'
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')
    
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    template_name='base/delete_task.html'
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')
    
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    fields='__all__'
    template_name='base/task_detail.html'
    

    
