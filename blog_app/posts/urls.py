from django.urls import path , include
from . import views
app_name = "posts"
urlpatterns = [

    path('',views.details, name = 'details'),
    path('<int:pk>/',views.post_detail, name = 'post_detail'),
    

]