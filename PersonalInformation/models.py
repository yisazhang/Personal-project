from django.db import models

class Personal(models.Model):
    name = models.CharField(max_length=8)
    sex = models.CharField(max_length=8)
    birth_date = models.DateField()
    work_date = models.DateField()
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    tell = models.CharField(max_length=11)
    mail = models.CharField(max_length=32,null=True)
    wendy = models.CharField(max_length=10)
    paper = models.CharField(max_length=10)
    card_id = models.CharField(max_length=60)

    class Meta:
        db_table = 'personal'