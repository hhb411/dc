from django.db import models

class Data(models.Model):
    class Meta:
        db_table = 'data_ltc_day'
    time = models.CharField(primary_key=True, max_length=12)
    # open = models.DecimalField(max_digits=12, decimal_places=None)
    # low = models.DecimalField()

    # def __str__(self):
    #     return self.title
