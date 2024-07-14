from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from sql import MemesDB, AdminDB
from minio_storage import Minio_Memes


app = FastAPI(docs_url=None)
db = MemesDB()
storage = Minio_Memes()
user = AdminDB()



@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


@app.put("/memes/{id}", summary="Обновить существующий мем") #Обновить существующий мем.
async def put_memes(id: int, name=None, url=None, username=None, password=None, ): #Обновить существующий мем.
    if not username:
        return "Проверти вводимые данные"
    if not password:
        return "Проверти вводимые данные"
    if not user.check_admin(username, password):
        return "Проверти вводимые данные"

    data = db.update_memes(id, url, name)
    if not data:
        return "Проверти вводимые данные"
    names, urls = data
    storage.upload_memes(urls, names)
    return "Мем изменён!"


@app.delete("/memes/{id}", summary="Удалить мем") #Удалить мем.
async def delete_meme(id: int, username=None, password=None): #Удалить мем.
    if not username:
        return "Проверти вводимые данные"
    if not password:
        return "Проверти вводимые данные"
    if not user.check_admin(username, password):
        return "Проверти вводимые данные"

    data = db.delete_memes(id)
    if data:
        storage.delete_memes(data[0])
        return "Удалено"
    return "Проверти вводимые данные"


