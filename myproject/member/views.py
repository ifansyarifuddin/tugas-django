from django.http import HttpResponse
from django.template import loader

def member(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def picture(request):
  template = loader.get_template('picture.html')
  return HttpResponse(template.render())