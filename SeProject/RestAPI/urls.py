from django.urls import include, path
from rest_framework import routers
from RestAPI.views import PoiViewSet, UserViewSet, DiscussionBoardViewSet, ChatMessageViewSet, BadgeViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'poi', PoiViewSet)
router.register(r'user', UserViewSet)
router.register(r'discussionboard', DiscussionBoardViewSet)
router.register(r'chatmessage', ChatMessageViewSet)
router.register(r'badge', BadgeViewSet)
router.register(r'userprofile', UserProfileViewSet)

urlpatterns = [
   path('', include(router.urls)),
]