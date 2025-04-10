from django.db import models

# Create your models here.
class TestModel(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'test_model'
        verbose_name = 'Test Model'
        verbose_name_plural = 'Test Models'

    
