from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, Comment {}'.format(self.name, self.id)
    
