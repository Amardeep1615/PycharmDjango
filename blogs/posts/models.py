from django.db import models

# Create your models here.
class Tag(models.Model):
    tags = models.CharField(max_length=50)
    def __str__(self):
        return self.tags

class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.URLField(blank=True)
    desc = models.TextField()
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title


class Comment(models.Model):
      comment = models.TextField()
      post = models.ForeignKey(Post,on_delete=models.CASCADE)

      def __str__(self):
          return self.comment



