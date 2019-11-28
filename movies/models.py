from django.db import models

# Create your models here.


class Movie(models.Model):
    name=models.CharField( max_length=100,verbose_name="flim Adi")
    description=models.TextField(verbose_name="Flim Açıklama")
    image=models.CharField( max_length=50,verbose_name="Flim Resim")
    created_date=models.DateTimeField(auto_now_add=True)
    isPublished=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def get_image_path(self):
        return 'img/'+self.image
    
