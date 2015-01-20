from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.template import Context 
from django.template.loader import get_template

from todo.models import Item
from .forms import AddItem

# Create your views here.
def list_view(request):
	template = get_template('list.html')
	variables = Context({
		'head_title': 'ToDo App',
		'page_title': 'Tasks'

		})
	items = Item.objects.all()
	return render (request,'list.html',{'items':items})

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

def add_Task(request):
	form = AddItem(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit= False)
		save_it.save()

	return render_to_response	("add_task.html",
								locals(),
								context_instance = RequestContext(request))