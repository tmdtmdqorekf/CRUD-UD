from django.db import models
# from django import os
# from django import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
    
    # def delete(self, *args, **kargs):
    #     if self.upload_files:
    #         os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
    #     super(Blog, self).delete(*args, **kargs)