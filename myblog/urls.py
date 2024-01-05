from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index ,name = 'index'),
    path('details/<int:id>',views.details ,name = 'details'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('about_me/', views.about_me, name='about_me'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)