import asyncio
from broadcaster import Broadcast

pubsub = Broadcast("memory://")

posts_list={1:{
            "user_id":87,
            "userto": 89,
            "text": 'Prueba texto',
            "likes": [85,86]
        }}
Notification_list=[]

queue = asyncio.Queue()

def create_posts(user_id,user_to, text):
    post_id=len(posts_list) + 1
    post = {
            "user_id":user_id,
            "userto": user_to,
            "text": text,
            "likes": []
        }
    posts_list[post_id] = post
    return post

def create_like(post_id):
    if  posts_list.get(post_id):        
        posts_list[post_id]["likes"].append()
        return True
    return False