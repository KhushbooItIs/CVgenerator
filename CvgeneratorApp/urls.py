
from django.urls import path
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('save_profile/',views.save_profile,name='save_profile'),
    path('<int:id>/',views.resume,name='resume'),
    path('download/<int:id>/',views.download_resume,name='download_resume'),

]
