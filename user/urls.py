from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),

    # ex: /home/5/
    #path('<int:question_id>/', views.detail, name='detail'),

]