"""ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# from products.views import (ProductListView,
#                             product_list_view,
#                             ProductDetailView,
#                             product_detail_view,
#                             ProductFeaturedListView,
#                             ProductFeaturedDetailView,
#                             ProductDetailSlugView
#                             )

from .views import home_page, about_page, contact_page, login_page, register_page
urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page),
    path('contact/', contact_page, name='contact'),
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search')),
    path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
    # url(r'^products-fbv/$', product_list_view),
    # url(r'^products/$', ProductListView.as_view()),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view())

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)