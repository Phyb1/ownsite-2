from django.urls import path
from  .import views
app_name = 'SiteApp'
urlpatterns = [
    path('', views.index , name='index'),
    path('blogs', views.blogIndex, name='blogIndex'),
    path('blogs/<int:blog_id>', views.blogReader, name='blogReader'),
    path('blog/comment/<int:blog_id>', views.comment, name='comment'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
     path('contact/', views.contact, name='contact'),
]