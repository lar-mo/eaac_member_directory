from django.urls import path

from . import views

app_name = 'members_app'

urlpatterns = [
    path('', views.list_active, name='list_active'),
    path('list_all/', views.list_all, name='list_all'),
    path('list_all_grid/', views.list_all_grid, name='list_all_grid'),
    path('list_board/', views.list_board, name='list_board'),
    path('list_active/', views.list_active, name='list_active'),
    path('list_inactive/', views.list_inactive, name='list_inactive'),
    path('needs_review/', views.needs_review, name='needs_review'),
    path('show_member_info/<int:member_id>/', views.show_member_info, name='show_member_info'),
    path('edit_member_info/<int:member_id>/', views.edit_member_info, name='edit_member_info'),
    path('save_member_info/', views.save_member_info, name='save_member_info'),
    path('search/', views.search_results, name='search_results'),
]
