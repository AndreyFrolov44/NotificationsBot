# Бот напоминаний

Менеджер заполняет таблицу GoogleSheet, указывает 

|tel_id|текст|дата|время| время на ответ|
|------|-----|----|-----|---------------|

Сотруднику приходит сообщение с прикрепленной инлайн клавиатурой (кнопка: выполнено / не сделано)
 

`.env`
```
REDIS_HOST=
REDIS_PORT=

TOKEN=

TABLE_ID=
```

## Запуск
```
docker-compose up --build
```