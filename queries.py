
from ariadne import QueryType
query = QueryType()

from .store import Notification_list, posts_list


@query.field("getPosts")
def resolve_getPosts(*_):
    return posts_list.values() # Last 10 messages


@query.field("getNotifications")
def resolve_getNotifications(*_):
    return Notification_list 