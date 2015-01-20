from django.conf.urls import patterns, include, url



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/', 'todo.views.list_view', name= 'list_view'),
    url(r'^new/', 'todo.views.add_Task', name= 'add_Task'),
)
