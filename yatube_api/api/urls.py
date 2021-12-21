from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/docs/redoc/', TemplateView.as_view(
         template_name='redoc.html'), name='redoc'
         ),
    path('v1/', include(router.urls)),
]
