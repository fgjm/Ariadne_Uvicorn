''' Rutas principales para consultas mutaciones y suscripciones(socket)'''

from api import app, graphql

app.mount("/graphql/", graphql)

app.add_websocket_route("/graphql/", graphql)
