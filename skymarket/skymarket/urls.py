from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ads.views import AdViewSet, CommentViewSet

users_router = routers.SimpleRouter()
users_router.register("api/users", UserViewSet, basename="users")

ads_router = routers.SimpleRouter()
ads_router.register("api/ads", AdViewSet, basename="ads")

comments_router = routers.SimpleRouter()
comments_router.register("api/ads/(?P<ad_id>[^/.]+)/comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(users_router.urls)),
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),

    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
