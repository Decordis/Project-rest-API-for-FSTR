from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    height = models.IntegerField()


class Image(models.Model):
    title = models.CharField()
    img = models.ImageField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open('static/images', 'rb') as p:
            self.img.save(p)


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

    beauty_title = models.CharField(max_length=250,)
    title = models.CharField(max_length=250, unique=True)
    other_titles = models.CharField(max_length=250, unique=True)
    connect = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField(Coord, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    photo_img = models.OneToOneField(Image, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=LEVEL_1A)
    winter_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)
    spring_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)
    summer_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)
    autumn_level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1A)


