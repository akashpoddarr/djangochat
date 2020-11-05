from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator,OriginValidator
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                url(r"^(?P<username>[\w.@+-]+)", ChatConsumer),
            ]
        )
    ),
})