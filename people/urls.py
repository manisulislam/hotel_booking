from django.urls import path

from . import views

urlpatterns=[
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path("edit/<int:id>/",views.editView.as_view(), name="edit_review"),
    path("delete/<int:id>/",views.deleteView.as_view(), name="delete_review"),
]