from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_product/', views.first_step, name='first_step'),
    path('add_product/step1/', views.first_step, name='first_step'),
    path('add_product/step2/', views.second_step, name='second_step'),
    path('add_product/<int:product_id>/step3/', views.third_step, name='third_step'),
    path('add_product/step4/', views.fourth_step, name='fourth_step')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)