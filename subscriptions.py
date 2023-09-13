import json
from ariadne import SubscriptionType

from .store import pubsub
subscription = SubscriptionType()

@subscription.source("updateNotifications")
async def source_message(_, info):
    async with pubsub.subscribe(channel="notification_room") as subscriber:
        async for event in subscriber:
            message = json.loads(event.message)
            yield message

@subscription.field("updateNotifications")
def resolve_message(event, info):   
    return event
