
import sys
from ariadne import load_schema_from_path,\
    make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler

from starlette.applications import Starlette

from starlette.middleware.cors import CORSMiddleware

from .mutations import mutation
from .queries import query
from .subscriptions import subscription
from .store import pubsub

from starlette.responses import PlainTextResponse
from starlette.routing import Route

async def file_update(request):
    try:
        async with request.form() as form:
            if "upload_file" in form:
                filename = form["upload_file"].filename
                print(filename, form["upload_file"].file)
                contents = form["upload_file"].file.read()
                with open(filename, "wb") as buffer:
                    buffer.write(contents)
                    buffer.close()
                return PlainTextResponse('File save')
        return PlainTextResponse('File dont save')
    except:
        print(' -file_update',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
        return PlainTextResponse('Error')

type_defs = load_schema_from_path("api/schema.graphql")
schema = make_executable_schema(type_defs, query, mutation, subscription)
graphql = CORSMiddleware( GraphQL(
    schema=schema,
    debug=True,
    websocket_handler=GraphQLTransportWSHandler(),
) , allow_origins=['*'], allow_methods=("GET", "POST", "OPTIONS"))

# Setup Starlette ASGI app with events to start and stop Broadcaster 
app = Starlette(
    debug=True, routes=[ Route('/file/', file_update, methods=['POST']),],
    on_startup=[pubsub.connect],
    on_shutdown=[pubsub.disconnect],
)