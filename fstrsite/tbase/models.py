from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8, unique=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, unique=True)
    height = models.IntegerField(unique=True)


class Image(models.Model):
    title = models.CharField()
    img = models.ImageField(default='70586.jpg')
    # img = models.ImageField(default='static/images/70586.jgp')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     with open('static/images', 'rb') as p:
    #         self.img.save(p)


class LevelPoint(models.Model):
    LEVEL_1A = '1A'
    LEVEL_1B = '1Б'
    LEVEL_2A = '1A'
    LEVEL_2B = '1Б'
    LEVEL_3A = '1A'
    LEVEL_3B = '1Б'

    LEVEL_CHOICES = (
        ('1A', '1A'),
        ('1Б', '1Б'),
        ('2A', '2A'),
        ('2Б', '2Б'),
        ('3A', '3A'),
        ('3Б', '3Б'),
    )

    winter_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)
    spring_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)
    summer_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)
    autumn_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)


class PointAdd(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'

    STATUS_CHOICES = (
        ('NW', 'New'),
        ('AC', 'Accepted'),
        ('PN', 'Pending'),
        ('RJ', 'REJECTED'),
    )

    beauty_title = models.CharField(max_length=250,)
    title = models.CharField(max_length=250, unique=True)
    other_titles = models.CharField(max_length=250, unique=True)
    connect = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField(Coord, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    photo_img = models.OneToOneField(Image, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    level = models.ForeignKey(LevelPoint, on_delete=models.CASCADE)




