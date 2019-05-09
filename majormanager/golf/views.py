from django.http import HttpResponse

def index(request):
  return HttpResponse("Golf Major Manager")