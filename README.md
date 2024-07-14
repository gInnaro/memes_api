# memes_api
 
Это тестовое задание
API создано на базе библиотеки FastApi, Базой данной Postgres, и хранилищем файлов Minio.

Сам API разбит на 4 файла.
- public.py
- private.py
- sql.py
- memes_storage.py

<<<<<<< HEAD
Функционал API
●  GET /memes: Получить список всех мемов (с пагинацией).
●  GET /memes/{id}: Получить конкретный мем по его ID.
●  POST /memes: Добавить новый мем (с картинкой и текстом).
●  PUT /memes/{id}: Обновить существующий мем.                                        
●  DELETE /memes/{id}: Удалить мем.
=======
Функионал API:
- GET /memes: Получить список всех мемов (с пагинацией).
- GET /memes/{id}: Получить конкретный мем по его ID.
- POST /memes: Добавить новый мем (с картинкой и текстом).
- PUT /memes/{id}: Обновить существующий мем.                                  
- DELETE /memes/{id}: Удалить мем.
>>>>>>> 91c0fee544cbbe942170a9b429dcfb387bfebf6e

Сам API разбит на две части. Первая часть Public.py отвечает за публичные действия с API. А именно с помощью него можно получить полный список мемов, добавлять новые мемы и посмотреть конкретный мем по ID.
Вторая часть, а именно Private.py, отвечают уже за редактирование и удаление мемов.

Так же есть документация, для каждого свой. Они доступны по ссылке. А именно http://localhost:8000/docs#/ для публичной части, и http://localhost:8001/docs#/ для приватной.

Следующий файл sql.py, отвечает за отправку запросов в бд.
И крайний файл memes_storage.py, отвечает за работу с хранилищем Minio.

Для запуска проекта нужно скачать сам архив и распаковать его в папку. Потом ввести в консоле docker-compose up --build и начнется скачивание и запуск Docker.
После первого запуска нужно получить ключ доступа для Minio. Открываем адрес http://localhost:9001/access-keys в браузере, и нажимаем на кнопку Create access key. ![chrome_VarYoyd8kH](https://github.com/user-attachments/assets/90dd1623-af83-4986-91de-310888f4a6be)
Тут мы видим нужные нам две строки, а именно Access Key и Secret Key. Их нам нужно записать в файл minio_storage.py. 
![chrome_0ck3V1NkOk](https://github.com/user-attachments/assets/05d31ec1-0c43-4b74-a177-112f3ad07b5b)
![pycharm64_lSt8GNI2CT](https://github.com/user-attachments/assets/1d7c460f-865d-4c9c-adc0-821ece958de4)</br>
Дальше нужно придумать название для Ключа, и нажать кнопку Create. После нажатия появится предложение сохранить ключи, тут уже зависит от вас.
После этого нужно перезапустить docker.
