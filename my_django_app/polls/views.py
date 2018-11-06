from django.http import HttpResponse

def index(request):
  return HttpResponse("<h1>Hello! You just hit the index!!!</h1>")

