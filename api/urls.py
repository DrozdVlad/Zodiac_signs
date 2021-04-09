from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('client/<str:id>/details', views.ClientDetailListView.as_view(), name='client_details'),
    path('client/create/', views.ClientCreate.as_view(), name='client_create'),
    path('client/<int:pk>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client_delete'),
]
