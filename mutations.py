import json
from ariadne import MutationType
from .store import create_like, create_posts, pubsub, Notification_list
import datetime
import base64

mutation = MutationType()



@mutation.field("posts")
async def resolve_reply(*_, **data):   
    create_posts(data["user_id"], data["user_to"],  data["text"]) 
    user=data["user_id"]
    notification={
        "avatar": "url",
        "content_id": data["user_id"],
        "created": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "id": datetime.datetime.now().isoformat(),
        "message": F"El usuario: {user} creo un post en tu muro" , 
        "type_action": "1",
        "seen": False
    }
    Notification_list.append(notification)    
    await pubsub.publish(channel="notification_room", message=json.dumps(notification))

    return True

@mutation.field("signupBase64")
def signupBase64(obj, info, encode_file):
    """ por probar: envio de imagenes en base 64- no implementado"""
    file=encode_file.split(';base64,')
    ext=file[0].split('/')[1]
    if(ext=='mpeg'): 
        ext='mp3'
    if not ext:
        return {"msg":"The field encode_file must start with: data: media_type/extension;base64"}
    decoded_data=base64.b64decode((file[1]))
    img_file = open(f'imagePr.{ext}', 'wb')
    img_file.write(decoded_data)
    img_file.close()
    return True