from django.db import models

class AadharModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    aadharno=models.IntegerField()

    def __str__(self):
        return "first_name={0},last_name={1},age{2},aadharno{3}".format(self.first_name, self.last_name,
                                                                                      self.age, self.aadharno)



# Create your models here.
