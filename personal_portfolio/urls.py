from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio, name='portfolio'),
    path('blog/', include('blog.urls')),
    path('sendemail', views.sendemail, name='sendemail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
