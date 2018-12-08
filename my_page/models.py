from django.db import models


'''
定义的是样品的种类，每个种类的基本信息
'''
class Protein(models.Model):
    pro_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    zh_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return self.en_name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    species_name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    info = models.TextField()
    pro_name = models.ForeignKey(Protein,on_delete= models.DO_NOTHING)

    def __str__(self):
        return 'Protein :{}'.format(self.pro_name)

