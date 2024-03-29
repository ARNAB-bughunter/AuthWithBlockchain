from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Base.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'Base.views.handler404'
handler500 = 'Base.views.handler500'