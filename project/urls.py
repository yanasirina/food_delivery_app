from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static

import authentication.urls
import core.urls
import core.order_urls


schema_view = get_swagger_view(title='API')

urlpatterns = [
    path("", schema_view),
    path("admin/", admin.site.urls),
    path("core/", include(core.urls)),
    path("auth/", include(authentication.urls)),
    path("orders/", include(core.order_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
