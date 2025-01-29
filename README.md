# Проект домашней работы по изучению Django-REST

## Описание:

Домашняя работа по DRF


## Функционал:


## Установка:

1. Клонируйте репозиторий:
```
git clone github.com/BazilioSan/RestHW
```
2. Установите зависимости:

pip install -r requirements.txt

3. Запустите команду: 
```
python3 manage.py runserver
```

Для запуска с использованием контейнеризации:
1. Убедитесь, что Docker установлен на ваш компьютер, или установите из дистрибутива, полученного на сайте https://www.docker.com/.

2. Для запуска процесса первичного создания контейнеров в терминале перейдите в корневую папку проекта и выполните команду: 
```
docker-compose up -d --build
```

3. После завершения процесса развертывания и запуска приложений в контейнерах docker в терминале появится сообщение:
 ✔ Service web                     Built                                                                                                                                                                                                                                                                243.3s 
 ✔ Service celery-beat             Built                                                                                                                                                                                                                                                                  1.7s 
 ✔ Service celery                  Built                                                                                                                                                                                                                                                                  1.6s 
 ✔ Network resthw_default          Created                                                                                                                                                                                                                                                                0.0s 
 ✔ Volume "resthw_app_code"        Created                                                                                                                                                                                                                                                                0.0s 
 ✔ Volume "resthw_static_volume"   Created                                                                                                                                                                                                                                                                0.0s 
 ✔ Volume "resthw_postgres_data"   Created                                                                                                                                                                                                                                                                0.0s 
 ✔ Container resthw-redis-1        Started                                                                                                                                                                                                                                                                2.1s 
 ✔ Container resthw-db-1           Started                                                                                                                                                                                                                                                                2.1s 
 ✔ Container resthw-web-1          Started                                                                                                                                                                                                                                                                1.6s 
 ✔ Container resthw-celery-1       Started                                                                                                                                                                                                                                                                2.1s 
 ✔ Container resthw-celery-beat-1  Started 

Теперь к приложению можно обращаться через http://localhost:8000/

4. В браузере по адресу http://localhost:8000/swagger/ можно ознакомиться с описанием API.

5. Последующие запуски можно осуществлять командой:
```
docker-compose up
```
6. Остановить работу контейнеров можно командой:
```
docker-compose up
```
7. Установите параметры доступа

Особые параметры доступа отсутствуют

## Использование:

Уточняется

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

