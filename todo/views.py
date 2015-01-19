from django.shortcuts import render
from django.shortcuts import render_to_response
from todo.models import Item

# Create your views here.
def list_view(request):
	items = Item.objects.all()
	return render_to_response('list_view.html',{'items'.items})