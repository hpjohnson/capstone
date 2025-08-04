from django.db import models
from django.contrib.auth.models import User

#options for integer fields
DIFFICULTY = ((-1, "None Specified"), (0, "Easy"), (1, "Medium"), (2, "Hard"), (3, "Insane"))
STATUS = ((0, "Draft"), (1, "Pending Approval"), (2, "Approved"), (3, "Disapproved"))

# Create your models here.
class Question(models.Model):
    questionID = models.BigAutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="question_post")
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    updateCount = models.IntegerField(default=0)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=-1)
    approved = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
