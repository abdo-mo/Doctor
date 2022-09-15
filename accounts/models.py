from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_patient = models.BooleanField(null=True)
    is_doctor = models.BooleanField(null=True)
    
    def __str__(self):
        return self.username

class Patients(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    job = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     image = models.ImageField(default = 'static//img//user.png', upload_to = 'static//img')
#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super(Profile, self).save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
# User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])
