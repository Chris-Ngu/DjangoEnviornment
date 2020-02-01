from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    dynamic_lookup_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_view),
    path('',home_view),
    path('about/', about_view),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('product/<int:id>/', dynamic_lookup_view, name='product'),
]

