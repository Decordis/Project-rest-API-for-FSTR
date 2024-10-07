""""
Описание тестов для PointAddModelTest:

1. setUp:
- Этот метод выполняется перед каждым тестом и создает необходимые объекты для тестирования
(координаты, пользователь, изображение и уровень).

2. test_create_point_add:
- Этот тест создает объект `PointAdd` и проверяет, что все поля установлены правильно.

3. test_title_unique_constraint:
- Проверяет уникальность поля `title`.
Если попытаться создать две записи с одинаковым значением `title`, должно возникнуть исключение.

4. test_other_titles_unique_constraint:
- Проверяет уникальность поля `other_titles`.
Как и в предыдущем тесте, должно возникнуть исключение при дублировании значения.

5. test_status_choices:
- Проверяет установку и изменение статуса. Убедитесь, что статус можно установить в любое из определенных значений.

6. test_date_auto_now_add:
- Проверяет, что поле `date` автоматически устанавливается при создании объекта.

Описание тестов для `PointAddSerializer`

1. setUp:
- Этот метод выполняется перед каждым тестом и создает необходимые объекты в базе данных, которые будут использоваться в
 последующих тестах. Здесь мы создаем экземпляры классов `Coord`, `Users`, `Image`, `LevelPoint` и `PointAdd`.
 Это позволяет избежать повторения кода в каждом тесте, так как нам нужно будет использовать эти объекты.

2. test_serializer_creates_point_add:
- **Цель**: Проверить, что сериализатор корректно создает объект `PointAdd`.
- **Описание**: Мы создаем валидные данные для сериализатора и проверяем, что он успешно валидирует эти данные с помощью
`is_valid()`. Затем мы сохраняем объект и проверяем, что у него установлен идентификатор (т.е. он создан в базе данных).
Это важно для того, чтобы убедиться, что процесс создания объекта работает без ошибок.

3. **`test_serializer_update_point_add`**:
- **Цель**: Проверить, что сериализатор корректно обновляет существующий объект `PointAdd`.
- **Описание**: Мы передаем валидные данные для обновления и проверяем, что сериализатор валидирует данные.
После сохранения мы проверяем, что поле `beauty_title` обновлено на ожидаемое значение.
Это важно для проверки работы обновления и сохранения объекта.

4. **`test_serializer_update_with_invalid_status`**:
- **Цель**: Проверить, что сериализатор вызывает ошибку валидации при попытке обновить объект с недопустимым статусом.
- **Описание**: Здесь мы устанавливаем статус объекта в "принятый" (AC) и пытаемся обновить его. Ожидаем, что будет
вызвано исключение (`ValidationError`). Это важно для проверки того,
что система защищает статус объектов и предотвращает нежелательные изменения.

5. **`test_invalid_user_data_change`**:
- **Цель**: Проверить, что изменение данных пользователя вызывает ошибку валидации.
- **Описание**: Здесь мы пытаемся изменить данные пользователя, касающиеся имени (`full_name`), и ожидаем,
что будет вызвано исключение (`ValidationError`). Это важно,
так как сериализатор должен защищать данные пользователей от изменений после их первоначальной установки.

"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from .models import PointAdd, Coord, Users, Image, LevelPoint
from .serializers import PointAddSerializer


class PointAddModelTest(TestCase):

    def setUp(self):
        # Создаем необходимые объекты для теста
        self.coord = Coord.objects.create(latitude=5.80000000, longitude=5.40000000, height=10)
        self.user = Users.objects.create(full_name='Иванов Иван Иванович', email='e@example.com', phone='89999999999')
        self.image = Image.objects.create(title='эльбрус', img='http://127.0.0.1:8000/70586_GRYZeHJ.jpg')
        self.level_point = LevelPoint.objects.create(winter_level='1A', spring_level='1A', summer_level='1A', autumn_level='1A')

    def test_create_point_add(self):
        # Создаем экземпляр модели PointAdd
        point = PointAdd.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Летом не сложно добраться',
            connect='Остальное:',
            coord_id=self.coord,
            user_id=self.user,
            photo_img=self.image,
            level=self.level_point
        )

        # Проверяем, что объект был создан
        self.assertIsInstance(point, PointAdd)
        self.assertEqual(point.beauty_title, 'Пик Эльбруса')
        self.assertEqual(point.title, 'Эльбрус')
        self.assertEqual(point.other_titles, 'Летом не сложно добраться')
        self.assertEqual(point.connect, 'Остальное:')
        self.assertEqual(point.user_id, self.user)
        self.assertEqual(point.coord_id, self.coord)
        self.assertEqual(point.photo_img, self.image)
        self.assertEqual(point.level, self.level_point)
        self.assertEqual(point.status, PointAdd.NEW)  # Проверка статуса по умолчанию

    def test_title_unique_constraint(self):
        # Проверка уникальности поля title
        PointAdd.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Летом не сложно добраться',
            connect='Остальное:',
            coord_id=self.coord,
            user_id=self.user,
            photo_img=self.image,
            level=self.level_point
        )
        with self.assertRaises(Exception):
            PointAdd.objects.create(
                beauty_title='Пик Эльбруса-2',
                title='Эльбрус',  # Дублируем уникальное значение
                other_titles='Другое описание',
                connect='Другое остальное',
                coord_id=self.coord,
                user_id=self.user,
                photo_img=self.image,
                level=self.level_point
            )

    def test_other_titles_unique_constraint(self):
        # Проверка уникальности поля other_titles
        PointAdd.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Летом не сложно добраться',
            connect='Остальное:',
            coord_id=self.coord,
            user_id=self.user,
            photo_img=self.image,
            level=self.level_point
        )
        with self.assertRaises(Exception):
            PointAdd.objects.create(
                beauty_title='Пик Эльбруса-3',
                title='Другой Эльбрус',
                other_titles='Летом не сложно добраться',  # Дублируем уникальное значение
                connect='Другое остальное',
                coord_id=self.coord,
                user_id=self.user,
                photo_img=self.image,
                level=self.level_point
            )

    def test_status_choices(self):
        # Проверка статусов
        point = PointAdd.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Летом не сложно добраться',
            connect='Остальное:',
            coord_id=self.coord,
            user_id=self.user,
            photo_img=self.image,
            level=self.level_point
        )
        point.status = PointAdd.ACCEPTED
        point.save()
        self.assertEqual(point.status, PointAdd.ACCEPTED)

    def test_date_auto_now_add(self):
        # Проверка поля date - должно быть установлено автоматически
        point = PointAdd.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Летом не сложно добраться',
            connect='Остальное:',
            coord_id=self.coord,
            user_id=self.user,
            photo_img=self.image,
            level=self.level_point
        )
        # Дата должна быть установлена
        self.assertIsNotNone(point.date)


class PointAddSerializerTest(APITestCase):
    def setUp(self):
        # Создаем необходимые объекты для теста
        self.coord = Coord.objects.create(latitude=5.80000000, longitude=5.40000000, height=10)
        self.user = Users.objects.create(full_name='Иванов Иван Иванович', email='e@example.com', phone='89999999999')
        self.image = Image.objects.create(title='эльбрус', img='http://127.0.0.1:8000/70586_GRYZeHJ.jpg')
        self.level_point = LevelPoint.objects.create(winter_level='1A', spring_level='1A', summer_level='1A', autumn_level='1A')
        self.point = PointAdd.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Летом не сложно добраться',
            connect='Остальное:',
            coord_id=self.coord,
            user_id=self.user,
            photo_img=self.image,
            level=self.level_point
        )

    def test_serializer_creates_point_add(self):
        data = {
            'beauty_title': 'Пик Эльбруса',
            'title': 'Эльбрус',
            'other_titles': 'Летом не сложно добраться',
            'connect': 'Остальное:',
            'coord_id': {'latitude': '5.80000000', 'longitude': '5.40000000', 'height': 10},
            'user_id': {'full_name': 'Иванов Иван Иванович', 'email': 'e@example.com', 'phone': '89999999999'},
            'level': {'winter_level': '1A', 'spring_level': '1A', 'summer_level': '1A', 'autumn_level': '1A'},
            'photo_img': {'title': 'эльбрус', 'img': 'http://127.0.0.1:8000/70586_GRYZeHJ.jpg'},
            'status': 'NW',
        }

        serializer = PointAddSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        point = serializer.save()
        # Проверяем, что объект создан
        self.assertIsNotNone(point.id)

    def test_serializer_update_point_add(self):
        data = {
            'beauty_title': 'Пик Эльбруса',
            'title': 'Эльбрус',
            'other_titles': 'Летом не сложно добраться',
            'connect': 'Остальное:',
            'coord_id': {'latitude': '5.80000000', 'longitude': '5.40000000', 'height': 10},
            'user_id': {'full_name': 'Иванов Иван Иванович', 'email': 'e@example.com', 'phone': '89999999999'},
            'level': {'winter_level': '1A', 'spring_level': '1A', 'summer_level': '1A', 'autumn_level': '1A'},
            'photo_img': {'title': 'эльбрус', 'img': 'http://127.0.0.1:8000/70586_GRYZeHJ.jpg'},
            'status': 'NW',
        }

        serializer = PointAddSerializer(instance=self.point, data=data)
        self.assertTrue(serializer.is_valid())
        updated_point = serializer.save()
        self.assertEqual(updated_point.beauty_title, 'Пик Эльбруса')

    def test_serializer_update_with_invalid_status(self):
        self.point.status = 'AC'  # Устанавливаем статус, который не разрешает обновление
        self.point.save()
        data = {
            'beauty_title': 'Пик Эльбруса',
            'title': 'Эльбрус',
            'other_titles': 'Летом не сложно добраться',
            'connect': 'Остальное:',
            'coord_id': {'latitude': '5.80000000', 'longitude': '5.40000000', 'height': 10},
            'user_id': {'full_name': 'Иванов Иван Иванович', 'email': 'e@example.com', 'phone': '89999999999'},
            'level': {'winter_level': '1A', 'spring_level': '1A', 'summer_level': '1A', 'autumn_level': '1A'},
            'photo_img': {'title': 'эльбрус', 'img': 'http://127.0.0.1:8000/70586_GRYZeHJ.jpg'},
        }

        serializer = PointAddSerializer(instance=self.point, data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_invalid_user_data_change(self):
        data = {
            'beauty_title': 'Пик Эльбруса',
            'title': 'Эльбрус',
            'other_titles': 'Летом не сложно добраться',
            'connect': 'Остальное:',
            'coord_id': {'latitude': '5.80000000', 'longitude': '5.40000000', 'height': 10},
            'user_id': {'full_name': 'Другой Иванов', 'email': 'e@example.com', 'phone': '89999999999'},  # Изменили имя
            'level': {'winter_level': '1A', 'spring_level': '1A', 'summer_level': '1A', 'autumn_level': '1A'},
            'photo_img': {'title': 'эльбрус', 'img': 'http://127.0.0.1:8000/70586_GRYZeHJ.jpg'},
        }

        serializer = PointAddSerializer(instance=self.point, data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)