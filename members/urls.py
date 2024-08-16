# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]