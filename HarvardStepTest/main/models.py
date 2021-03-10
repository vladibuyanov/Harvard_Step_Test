from django.db import models


# Create your models here.
class Results(models.Model):
    name = models.CharField('Name', max_length=50)
    age = models.IntegerField('Age')
    time = models.IntegerField('Time')
    f1 = models.IntegerField('f1')
    f2 = models.IntegerField('f2')
    f3 = models.IntegerField('f3')
    result = models.IntegerField('Result')

    def __str__(self):
        return self.name
