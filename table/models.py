from django.db import models

# Create your models here.
class TableData(models.Model):

    user_id = models.IntegerField(unique=False)
    username = models.TextField(unique=False)
    contact = models.IntegerField(unique=False)
    primary_role = models.TextField(unique=False)
    additional_role = models.TextField(unique=False)
    school_id = models.IntegerField(unique=False)
    school_name = models.TextField(unique=False)
    block_name = models.TextField(unique=False)
    district_name = models.TextField(unique=False)
    dise_code = models.IntegerField(unique=False)

    def __str__(self):
        return self.username


    class Meta:
        managed =True
        db_table = 'table_data'
        ordering = ['user_id']