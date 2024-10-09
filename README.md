# REST API для мобильного приложения


## I. Описание
Данный проект был разработан для дальнейшего обслуживания мобильного приложения, которое разрабатывают для Федерации Спортивного Туризма России (ФСТР) и предназначено для обновления базы данных горных перевалов, которая пополняется туристами. 


## II. Особенности данного REST API.
- **Структурированные данные**: API возвращает данные в формате JSON, что позволяет легко интегрировать и обрабатывать их в различных приложениях.
- **Поддержка различных уровней сложности**: API предоставляет информацию о уровне сложности локаций в разные сезоны (зима, весна, лето, осень), что помогает другим туристам планировать свои поездки в зависимости от времени года.
- **Информация о пользователях**: Каждая локация связана с пользователем, который добавил данные, включая полное имя, email и телефон. Это позволяет устанавливать связь и доверие к информации.
- **Геолокационные данные**: API хранит точные координаты (широту, долготу и высоту) для каждой локации, что позволяет пользователям найти их на карте или использовать в навигационных системах.
- **Фотографии локаций**: API предоставляет ссылки на изображения локаций, что делает информацию более наглядной и привлекательной.
- API поддерживает как запросы GET для получения данных, так и запросы POST для добавления новых локаций, что позволяет пользователям активно взаимодействовать с платформой.
- **Дата добавления**: Каждая запись содержит информацию о дате и времени добавления, что может быть полезно для отслеживания актуальности данных.
- **Кастомизация записей**: Пользователи могут добавлять различные дополнительные описания к локациям, такие как "красивое название" и "дополнительные комментарии", что позволяет делать записи более информативными.
- **Легковесность и простота**: API предназначен для быстрой передачи данных и использует простую структуру, что делает его удобным для разработчиков.

## III. Стэк
- Python 3.X
- Django
- Django REST framework
- JSON
- PostgreSQL
- Swagger
- Docker

## IV. Формат данных
Каждый объект в массиве имеет следующие поля:

- **beauty_title** (string): Красивое название локации (например, "Пик Эльбруса").
- **title** (string): Обычное название локации (например, "Эльбрус").
- **other_titles** (string): Дополнительная информация о доступности (например, "Летом не сложно добраться").
- **connect** (string): Дополнительные комментарии (например, "Остальное:").
- **date** (string): Дата добавления информации в формате ISO 8601 (например, "2024-10-01T18:46:05.969487+03:00").
- **coord_id** (object): Объект с координатами:
- **latitude** (string): Широта местоположения.
- **longitude** (string): Долгота местоположения.
- **height** (integer): Высота в метрах над уровнем моря.

- **user_id** (object): Объект с информацией о пользователе:
- **full_name** (string): Полное имя пользователя (например, "Иванов Иван Иванович").
- **email** (string): Эл. почта пользователя (например, "example@example.com").
- **phone** (string): Телефон пользователя (например, "89999999999").

- **level** (object): Уровни сложности в разные сезоны:
- **winter_level** (string): Уровень сложности для зимы (например, "1A").
- **spring_level** (string): Уровень сложности для весны (например, "1A").
- **summer_level** (string): Уровень сложности для лета (например, "1A").
- **autumn_level** (string): Уровень сложности для осени (например, "1A").

- **photo_img** (object): Объект, содержащий информацию о фотографии:
- **title** (string): Название фотографии (например, "Эльбрус").
- **img** (string($uri)): URL-адрес изображения (например, "http:example.jpg").

- **status** (string): Статус объекта (например, "NW" - "новая запись").
     Допустимые значения:
  -   new - новая запись;
  -   pending — если модератор взял в работу;
  -   accepted — модерация прошла успешно;
  -   rejected — модерация прошла, информация не принята.

## V. Параметры запросов.
Для получения информации о локациях можно использовать следующий HTTP-запросы:
### GET /api/submitdata/
Получает список всех доступных локаций.

### GET /api/submitdata/<id> 
Получить одну запись (перевал) по её id. 
Выводится вся информацию об объекте, в том числе статус модерации.

### GET /api/submitdata/?user_id__email=email
Получает список данных обо всех объектах, которые пользователь с почтой email отправил на сервер.

### POST /api/submitdata/
Добавить новый перевал на сервер.

### PATCH /submitData/<id>
Возможность отредактировать существующую запись (замена), если она в статусе **new**.
Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. 

#### Данные представлены в формате JSON и выглядят следующим образом:
    
    json 
    [
    {
    "beauty_title": "Пик Эльбруса",
    "title": "Эльбрус",
    "other_titles": "Летом не сложно добраться",
    "connect": "Остальное:",
    "date": "2024-10-01T18:46:05.969487+03:00",
    "coord_id": {
      "latitude": "43.352467",
      "longitude": "42.437872",
      "height": 5642
    },
    "user_id": {
      "full_name": "Иванов Иван Иванович",
      "email": "example@example.com",
      "phone": "89999999999"
    },
    "level": {
      "winter_level": "1A",
      "spring_level": "1A",
      "summer_level": "1A",
      "autumn_level": "1A"
    },
    "photo_img": {
      "title": "эльбрус",
      "img": "http://127.0.0.1:8000/70586_GRYZeHJ.jpg"
    },
    "status": "NW"
    }
    ]

## VI. Заключение.
Данный REST API открывает широкие возможности для получения, создания и обновления данных о новых точках. Интеграция этого API в мобильные приложения для туристов существенно повысит качество пользовательского опыта и упростит доступ к важной информации.






