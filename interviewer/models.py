from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Test(models.Model):
    title = models.CharField(max_length=200, null=True)
    test_detail_name = models.CharField(max_length=200, null=True)
    department_name = models.CharField(max_length=200, null=True)
    test_description = models.CharField(max_length=200, null=True, blank=True)
    question_description = models.TextField(null=True)
    answer_one = models.CharField(max_length=200, null=True)
    answer_two = models.CharField(max_length=200, null=True)
    answer_three = models.CharField(max_length=200, null=True)
    answer_four = models.CharField(max_length=200, null=True)
    answer_five = models.CharField(max_length=200, null=True)
    question_image = models.ImageField(upload_to="test/", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Question(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="questions/", default='questions/1.jpg')
    description = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    tests = models.ManyToManyField(Test)
    question_title = models.CharField(max_length=200, null=True, blank=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    department_name = models.CharField(max_length=200, null=True, blank=True)
    number_of_questions = models.CharField(max_length=200, null=True, blank=True)
    question_description = models.TextField(null=True)
    question_number = models.CharField(max_length=200, null=True, blank=True)
    correct_answer = models.CharField(max_length=200, null=True, blank=True)
    question_image = models.ImageField(upload_to="test/", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('question_details', kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name








