import os
import sys

sys.path.append(rf'{os.path.abspath('shop/')}')
from fastapi import FastAPI
from uvicorn import run as uvi_run
from fastapi.responses import RedirectResponse

from shop import router_users, router_items, router_orders
from shop.generation_db import generation

app = FastAPI()


@app.get('/generation_db/', tags=['Наполнение БД сгенерированными данными'], response_model=dict)
async def generation_db():
    await generation()
    return {'message': 'Successful DB population'}


app.include_router(router_users.router)
app.include_router(router_items.router)
app.include_router(router_orders.router)


@app.get('/', tags=['Redirect to Swagger UI'], response_class=RedirectResponse)
async def redirect_index():
    return "http://127.0.0.1:8000/docs"


if __name__ == "__main__":
    uvi_run("main:app", host="127.0.0.1", port=8000, reload=True)
