from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Category model to define a question type.
    """
    name = models.CharField(max_length=250, blank=True, null=True, help_text="Category name.")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

class Exam(models.Model):
    """
    Model for creating an exam.
    """

    name = models.CharField(max_length=250, blank=True, null=True, help_text="Set a name for exam.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Author of an exam.")
    duration = models.IntegerField(blank=True, null=True, help_text="Set a duration of an exam.")
    description = models.TextField(max_length=1000, blank=True, null=True, help_text="Description of an exam.")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, help_text="Set the category for an exam.", related_name="exam", null="true")

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def __str__(self) -> str:
        return self.name
