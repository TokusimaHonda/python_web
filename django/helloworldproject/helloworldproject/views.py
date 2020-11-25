from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnobject = HttpResponse('<h1>日向坂</h1>')
    return returnobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'