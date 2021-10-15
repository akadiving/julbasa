from django.db import models
from django.contrib.auth.models import User
from .utils import path_and_rename
from exam.models import Exam
from exam.models import Category
# Create your models here.


class Question(models.Model):
    """
    Question model that stores a body of question and its author
    """

    levels = (
        (1,1),(2,2),(3,3),(4,4),(5,5),
        (6,6),(7,7),(8,8),(9,9),(10,10)
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, help_text="Author of the question.")
    body = models.TextField(max_length=1000, help_text="Question text.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when question was created")
    difficulty = models.IntegerField(choices=levels, default=levels[4], help_text="Choose the difficulty of the question")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="question", help_text="List of questions for this exam.", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, help_text="Category of question.", null=True, blank=True)


    def __str__(self) -> str:
        return self.body

    class Meta:
        ordering =['-created_at',]
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Answer(models.Model):
    """
    Answer model that has many-to-one relation with question
    """
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
    body = models.TextField(max_length=500, blank=True, null=True, help_text="Choice body")
    image = models.ImageField(upload_to = path_and_rename, null=True, blank=True, help_text="Choose image")
    right_answer = models.BooleanField(default=False, null=True, help_text="Check the right answer")

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self) -> str:
        return self.body

    def get_image(self):
        if self.image:
            return self.image.url
        return ''
