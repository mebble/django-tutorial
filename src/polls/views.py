from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    return HttpResponse("Hey, you're at the poollss!")
