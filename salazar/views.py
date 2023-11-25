from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hola mundo </h1>")
