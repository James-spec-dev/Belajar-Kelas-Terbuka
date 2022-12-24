from django.db import models

# Create your models here.
class ModelPost(models.Model):
	judul = models.CharField(max_length=100)
	body = models.TextField()
	author = models.CharField(max_length=100)

	LISTKATEGORI=(
		('jurnal','jurnal'),
		('olahraga','olahraga'),
		('ekonomi','ekonomi'),
		)
	category = models.CharField(
		max_length=100,
		choices=LISTKATEGORI,
		default='jurnal',
		)

	def __str__(self):
		return "{},{}".format(self.id, self.judul)