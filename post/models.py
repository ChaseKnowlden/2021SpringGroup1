from django.db import models
from person.models import Person

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id')
    posterid = models.IntegerField()
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(max_length=max, verbose_name='Description')
    likeNum = models.IntegerField()
    likedBy = models.TextField(max_length=max, default="[]")
    createdDate = models.DateTimeField(
        auto_now_add=True, verbose_name="Created Date")

    def __str__(self) -> str:
        data = {
            "id": self.id,
            "posterid": self.posterid,
            "title": self.title,
            "description": self.description,
            "likenum": self.likeNum,
            "likedby": self.likedBy,
            "date": self.createdDate
        }
        return data
