# Flore — Онлайн-магазин цветов

Flore — учебный проект для демонстрации работы с FastAPI, PostgreSQL и Docker.  
Проект реализует базовые CRUD API для пользователей, букетов и заказов.

---

## Структура проекта

flore/
├─ backend/
│ ├─ app/
│ │ ├─ api/v1/
│ │ │ ├─ auth.py
│ │ │ ├─ bouquets.py
│ │ │ └─ orders.py
│ │ ├─ crud.py
│ │ ├─ db/
│ │ │ ├─ base.py
│ │ │ └─ session.py
│ │ ├─ main.py
│ │ ├─ models.py
│ │ ├─ schemas.py
│ │ └─ core/
│ │ └─ security.py
│ ├─ mock_service.py
│ └─ requirements.txt
├─ docker-compose.yml
├─ Dockerfile
├─ seed.sql
└─ README.md


---

## Используемые технологии

- **Backend:** FastAPI (Python)  
- **База данных:** PostgreSQL  
- **Миграции:** SQLAlchemy + автоматическое создание таблиц  
- **Контейнеризация:** Docker, docker-compose  
- **Mock-сервисы:** FastAPI mock-service  
- **Тесты:** pytest  
- **Документация:** OpenAPI / Swagger  

---

## Установка и запуск

1. Клонируем репозиторий:

```bash
git clone https://github.com/Evelina079/flore.git
cd flore

2.Запускаем контейнеры через Docker Compose:

docker-compose up --build

Контейнеры:

backend: FastAPI, порт 8000

postgres: база данных, порт 5432

mock-service: фейковый внешний сервис, порт 9000 (если используется)

3. Seed-данные (пример):

docker exec -it flore-db-1 psql -U flore -d flore_db -f /seed.sql


4. Доступ к API:

FastAPI: http://localhost:8000

Swagger / OpenAPI: http://localhost:8000/docs

## Примеры запросов (cURL)
Просмотр всех букетов
curl -X GET "http://localhost:8000/api/v1/bouquets/"

## Создание заказа
curl -X POST "http://localhost:8000/api/v1/orders/" \
-H "Content-Type: application/json" \
-d '{"user_id":1,"total_price":1500,"delivery_address":"ул. Ленина, 10"}'

##Тестирование

1.Установите зависимости для тестов:

pip install -r backend/requirements.txt
pip install pytest


2.Запустите тесты:

pytest

## Документация API

Документация автоматически генерируется FastAPI и доступна по адресу:

http://localhost:8000/docs


Там можно посмотреть все эндпоинты, модели данных и попробовать запросы прямо в браузере.


---

