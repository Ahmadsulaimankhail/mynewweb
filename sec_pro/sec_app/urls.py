
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('books', views.showbooks, name='showbooks'),
    path('lend', views.lend_book, name='lend'),
    path('lendbooks/', views.showlend_books, name='lendbooks'),
    path('delete/<int:book_id>/', views.delete, name='delete_book'),
    path('edit/<int:book_id>/',views.edit,name='edit'),
    # path('search/',views.return_Search,name='search'),
    path('addmember/',views.addMember,name='addmember'),
    path('showMembers/',views.show_member,name='show_members'),
    path('edit_member/<int:book_id>/',views.editMember,name='editMember'),
    path('delet_member/<int:book_id>/',views.deletMember,name='deletMember'),
    path('return_form/',views.return_form,name='return_form'),
    path('show_return_book/',views.show_return_book,name='show_return_book'),
    path('return/<int:books_id>/',views.return_book,name='return_book'),


]