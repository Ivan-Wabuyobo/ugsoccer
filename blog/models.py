from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
       return f"{self.title}"

class Comment(models.Model):
    author = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f'{self.body}'
