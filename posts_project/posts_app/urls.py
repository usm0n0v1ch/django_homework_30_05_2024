from django.urls import path
from posts_app import views

urlpatterns = [
    path('', views.show_posts, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<int:pk>/', views.post_info, name='post_info'),
    path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/edit_post', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete_post', views.delete_post, name='delete_post'),
    path('category', views.show_category, name='category'),
    path('category/<int:pk>/delete_category', views.delete_category, name='delete_category'),
    path('category/add_category', views.add_category, name='add_category'),
    path('category/<int:pk>/edit_category', views.edit_category, name='edit_category'),
    path('category/<int:pk>/category_info', views.category_info, name='category_info'),
    path('create-dummy-posts/', views.create_posts, name='create_dummy_posts'),
    path('update-post-titles/', views.update_post_titles, name='update_post_titles'),
    path('delete-odd-id-posts/', views.delete_id_posts, name='delete_odd_id_posts'),
]
