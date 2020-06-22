from django.db import models

class Note(models.Model):
	judul = models.CharField(max_length = 100)
	isi = models.TextField()
	def __str__(self):
		return "{}".format(self.id)