
# Ariadne GrahpQL

Consultas, mutaciones y suscripciones en Ariadne(grapgql), Starlette(Rutas), Broadcast(envio en tiempo real - websocket)
Carga de archivos en base64 y multipart(From-data)

prueba de generar notificaciones al crear un post con user_to

## Installation

Install project with python 3.9 and virtualenv

```bash
  virtualenv .venv  
```

```bash
  python -m venv .venv 
  .venv\Scripts\activate
  pip install -r requirements.txt
  uvicorn app:app --port 5006 --reload
```
## subir archivos por Graphql

la mutacion de guardar jpg y mp4 en base 64 se probo con encode Base 64 de la pagina:
https://base64.guru/converter/encode/video 

Por probar: cargar videos por graphql (multipart/form-data)

https://stackoverflow.com/questions/68150672/upload-file-with-graphql-ariadne-flask-graphql-error-graphql-error-graphqler

## Pylint one file
```bash
pip install pylint
python -m pylint .\app.py
```
## Pylint multiple file

pip install pylint-runner

en la carpeta raíz
pylint_runner



**Server:** Python, uvicorn, ariadne, broadcast, Starlette


