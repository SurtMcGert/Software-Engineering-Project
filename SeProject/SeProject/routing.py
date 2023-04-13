from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import DiscussionApp.routing

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            DiscussionApp.routing.websocketURLPatterns
        )
    ),
})