from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import (
    index, event, project, official, about, gallery, review, contact, payment, account
)

urlpatterns = [
    path('', index, name='index'),
    path('review/', review, name='review'),
    path('contact/', contact, name='contact'),
    path('account/', account, name='account'),
    path('payment/', payment, name='payment'),
    path('event/', event, name='event'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('official/', official, name='official'),
    path('project/', project, name='project'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)