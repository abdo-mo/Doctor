from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from PLT import Image

# Create your models here.

class User(AbstractUser):

    class Types(models.TextChoices):
        Patient = 'Patient', 'Patient'
        Doctor = 'Doctor', 'Doctor'
        StaffMember = 'Staff', 'Staff'

    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.Patient)

    name = models.CharField(_('name of user'), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class PatientMore(models.Model):
    # objects = PatientManager()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    job = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Patient)

class Patients(User):
    objects = PatientManager()

    @property
    def more(self):
        return self.patientmore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.Patient
        return super().save(*args, **kwargs)

class DoctorMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialist_doctor = models.CharField(max_length=100, null=True, blank=True)

class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Doctor)

class Doctors(User):
    objects = DoctorManager()

    @property
    def more(self):
        return self.doctormore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.Doctor
        return super().save(*args, **kwargs)

class StaffMore(models.Model):
    job_type = models.CharField(max_length=100, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class StaffManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.StaffMember)


class Staffs(User):
    objects = StaffManager()

    @property
    def more(self):
        return self.staffmore

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.StaffMember
        return super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'static//img//user.png', upload_to = 'static//img')
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])
