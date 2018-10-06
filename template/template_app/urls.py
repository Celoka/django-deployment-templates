from django.urls import path
from template_app import views


app_name = 'template_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/',views.user_login,name='user_login')
    # path('other/', views.other, name='other')
]
