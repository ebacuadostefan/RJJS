from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.index_gender),
    path('gender/create', views.create_gender),
    path('gender/store', views.store_gender),
    path('gender/show/<int:gender_id>', views.show_gender),
    path('gender/edit/<int:gender_id>', views.edit_gender),
    path('gender/update/<int:gender_id>', views.update_gender),
    path('gender/delete/<int:gender_id>', views.delete_gender),
    path('gender/destroy/<int:gender_id>', views.destroy_gender),
    path('users', views.index_user),
    path('user/create', views.create_user),
    path('user/store', views.store_user),
]
