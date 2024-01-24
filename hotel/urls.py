from django.urls import path

from . import views
urlpatterns=[
    path('hotel_detail/<int:pk>/',views.HotelDetailView.as_view(),name='hotel_detail'),
    path('book_hotel/<int:id>/',views.Book_Hotel,name='book_hotel'),
    path('book_review/<int:id>/',views.Book_Review,name='book_review'),
    path('photo_galary/',views.Photo_Galary, name='photo_galary'),
    path('contact_us/', views.Contact_Us, name='contact_us'),
]