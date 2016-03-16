from django.conf.urls import include, url
from django.contrib import admin
from dates import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about$', views.About.as_view(), name='about'),

    url(r'^register$', views.User_Register.as_view(), name='register'),
    url(r'^login$', views.User_Login.as_view(), name='login'),
    url(r'^logout$', views.User_Logout.as_view(), name='logout'),

    url(r'^add$', views.AddDate.as_view(), name='add'),
    url(r'^search$', views.SearchDate.as_view(), name='search'),
    url(r'^area$', views.SearchDate_Area.as_view(), name='search_area'),
    url(r'^results$', views.SearchDate.as_view(), name='results'),
    url(r'^search_by$', views.Search_By.as_view(), name='search_by'),
]
