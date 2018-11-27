from django.urls import path
from . import views

app_name = 'warehouse'
urlpatterns = [
    #path('', views.login, name='index'),
    #path('addpage/', views.add_page, name='add'),
    #path('add/', views.add_data, name='add_data'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('employee/<int:employee_id>/add', views.add, name='add'),
    path('employee/<int:employee_id>/gifts', views.gifts, name='gifts'),
    path('employee/<int:employee_id>/modify', views.modify, name='modify'),
    path('employee/<int:employee_id>/sell', views.sell, name='sell'),
    path('employee/<int:employee_id>/delete', views.delete, name='delete')
]
