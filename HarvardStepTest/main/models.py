from django.db import models


# Create your models here.
class ResultInput(models.Model):
    name = models.CharField('Name', max_length=50)
    age = models.IntegerField('Age')
    time = models.IntegerField('Time')
    f1 = models.IntegerField('f1')
    f2 = models.IntegerField('f2')
    f3 = models.IntegerField('f3')

    def __str__(self):
        return self.name

    @property
    def result(self):
        result = self.time * 100 / (self.f1 + self.f2 + self.f3) * 2
        return result


