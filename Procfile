web: cd SeProject && uvicorn SeProject.asgi:application --limit-max-requests=1200 --host=0.0.0.0 --port $PORT --lifespan off
worker: python manage.py runworker channel_layer
worker: python manage.py runworker channel_layer
