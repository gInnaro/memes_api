from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.openapi.docs import get_swagger_ui_html
from sql import MemesDB
from minio_storage import Minio_Memes
import re

app = FastAPI()
db = MemesDB()
storage = Minio_Memes()

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )

@app.get("/memes", summary="Получить список всех мемов (с пагинацией)") #Получить список всех мемов (с пагинацией).
async def get_memes():
    data = db.unload_memes()
    return data


@app.get("/memes/{id}", summary="Получить конкретный мем по его ID") #Получить конкретный мем по его ID.
async def get_memes_id(id: int):
    data = db.one_memes(id)
    if not data:
        return "Проверти вводимые данные"
    image_bytes = storage.open_memes(data[0])
    return Response(content=image_bytes.getvalue(), media_type="image/jpeg")


@app.post("/memes", summary="Добавить новый мем (с картинкой и текстом)") #Добавить новый мем (с картинкой и текстом).
async def post_memes(name, url: str):
    url_regex = re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    if url_regex.match(url):
        if db.upload_memes(url=url, name=name):
            storage.upload_memes(url, name)
            return "Новый мем создан!"
    else:
        return "Не правильная ссылка!!!"