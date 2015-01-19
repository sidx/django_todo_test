from django.shortcuts import render
from django.shortcuts import render_to_response
from todo.models import Item

# Create your views here.
def list_view(request):
	items = Item.objects.all()
	return render_to_response('list_view.html',{'items'.items})

def todo_add(request):
	if request.method == "POST":
		item_name = request.POST['item']
		new_item = Item()
		new_item.title = item_name
		new_item.description = description
		new_item.due_date = due_date
		new_item.priority = priority
		new_item.status = status
		new_item.save()
		return redirect('/')


def todo_del(request, item_id):
	item = Item.objects.get(id=item_id)
	task.delete()
	return redirect('/')
	
