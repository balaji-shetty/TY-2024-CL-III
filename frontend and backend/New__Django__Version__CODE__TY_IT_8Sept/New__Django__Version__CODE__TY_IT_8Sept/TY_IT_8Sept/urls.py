from django.contrib import admin
from django.urls import path
from student.views import view_hello, view_record, view_hello_20

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello1/', view_hello, name='home'),
    path('hello20/', view_hello_20),
    path('record1/', view_record),
    path('', view_hello, name='default_home'),  # Handle root path (`/`)
]
