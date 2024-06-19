from django.urls import path
from .views import SellerDashboardView, SellerProfileView, CreateBookView, EditProfileView, BookDeletedView

app_name = 'sellers'

urlpatterns = [
    path('dashboard/', SellerDashboardView.as_view(), name='dashboard'),
    path('profile/', SellerProfileView.as_view(), name='profile'),
    path('create-book/', CreateBookView.as_view(), name='create_book'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('book-delete/<int:book_id>/', BookDeletedView, name='book_delete'),
]