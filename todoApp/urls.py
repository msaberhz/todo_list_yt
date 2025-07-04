
from django.urls import path
from . import views





urlpatterns = [
   path('', views.home, name='home'),
   path('addTask', views.addTask, name='addTask'),
   # path('is_completed/<int:pk>/', views.is_completed, name='is_completed'),
   path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
   path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
   path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

   #edit_task
   path('edit/<int:pk>/', views.edit, name='edit'),
   
   
]
