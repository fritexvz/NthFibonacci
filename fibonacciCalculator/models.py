from django.db import models

# Create your models here.


class FibonacciNumbers(models.Model):
	position = models.IntegerField()
	value = models.IntegerField()
	time = models.FloatField(null=True, blank=True, default=None)
	date = models.DateTimeField()
	method = models.CharField(max_length=50)
class Meta:
	db_table = "fibonaccinumbers"
