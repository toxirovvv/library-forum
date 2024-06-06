from django.db import models
from user.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='post_name', max_length=150, default='book name')
    image = models.ImageField(upload_to='images/post/', verbose_name='img', default='image.png')
    content = models.TextField(max_length=500, verbose_name='Post contenti')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Post yaratilgan vaqti.')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'post'
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    
    created_at = models.DateTimeField(auto_now=True, verbose_name='Comment yaratilgan vaqti.')
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'comment'
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
class Like(models.Model):
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_like', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.name
    
    class Meta:
        db_table = 'like'
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        unique_together = ('user', 'post')