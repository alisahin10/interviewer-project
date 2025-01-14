from django.db import models
from django.contrib.auth.models import User

import interviewer.models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class QuestionProfile(models.Model):
    question = models.ForeignKey(interviewer.models.Question, default=1, on_delete=models.CASCADE)

