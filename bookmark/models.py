from django.db import models
from django.urls import reverse
# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length =100)
    url = models.URLField('site URL')

    def __str__(self):
        #객체를 출력할 때 나타날 값(admin에서) / 항상 문자열을 반환해야함
        return "이름 : " + self.site_name +", 주소 : " + self.url
    
    def get_absolute_url(self):
        return reverse('detail', args=[int(self.id)])
    
    