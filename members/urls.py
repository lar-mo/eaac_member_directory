from django.urls import path

from . import views

app_name = 'members_app'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('list_members_grid/', views.list_members_grid, name='list_members_grid'),
    path('list_board/', views.list_board, name='list_board'),
    path('list_active/', views.list_active, name='list_active'),
    path('list_inactive/', views.list_inactive, name='list_inactive'),
    path('search/', views.search_results, name='search_results'),
]
