from . import views
from django.urls import path


urlpatterns = [path('users-list/', views.users_list),
               path('add-user/', views.user_view),
               path('edit-user/', views.user_view),
               path('delete-user/', views.user_view),
               path('get-details/', views.get_details),
                ]