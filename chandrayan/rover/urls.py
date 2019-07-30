from django.conf.urls import url
from rover import views

app_name = 'suyog'


urlpatterns = [
    url(r'^$', views.roverfun, name='rovn'),
    url(r'^boostlink/', views.rovboost, name='boostn'),
    url(r'^register/$', views.register, name='register'),
    url(r'^flaplink/', views.rovflap, name='flapn'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    # url(r'^media/profile_pics/$', views.images, name='images'),

]
