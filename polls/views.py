# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('polls/gioithieu.html', )
def  view_2(request):
	return HttpResponse("Hello, world. Wellcome my page 2. ")