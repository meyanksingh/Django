from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index, name='index'),
    path('login',views.login_page, name='login'),
    path('',views.register, name='register'),
    path('logout',views.logout_view, name='logout'),
    path('delete/<id>/',views.delete_recipe, name='delete_recipe' ),
    path('update/<id>/',views.update_recipe, name='update_recipe' )
]
