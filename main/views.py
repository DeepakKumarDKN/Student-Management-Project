from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import(
  DetailView,
  ListView, CreateView,UpdateView,DeleteView
)
from .models import Student, College
# Create your views here.
class Index(View):
  def get(self, request):
    return HttpResponse('GET Request')
  
  def post(self,request):
    return HttpResponse('Post Request')
  
class CollegeDetail(DetailView):
  models = College
  template_name = 'college_Detail.html'
  context_object_name = 'object'
  
  def get_queryset(self):
    return College.objects.all()
  
class CollegeList(ListView):
  models = College
  template_name = 'college_list.html'
  context_object_name = "colleges"
  
  def get_queryset(self):
    return College.objects.all()
  
class CollegeCreate(CreateView):
  models = College
  template_name = 'college_create.html'
  context_object_name = 'college_create'
  fields = '__all__'
  success_url = '/college'
  
  # def get_success_url(self):
  #   return reverse('create_college')
  def get_queryset(self):
    return College.objects.all()
  
class CollegeUpdate(UpdateView):
  models = College
  template_name = 'college_create.html'
  fields = "__all__"
  success_url = '/college'
  
  def get_queryset(self):
    return College.objects.all()
  
class StudentCreate(CreateView):
  models = Student
  template_name ="student_create.html"
  fields = "__all__"
  success_url = "/"
  
  def get_queryset(self):
    return Student.objects.all()

class StudentDelete(DeleteView):
  model = Student
  template_name ="confirm.html"
  success_url = "/college"

