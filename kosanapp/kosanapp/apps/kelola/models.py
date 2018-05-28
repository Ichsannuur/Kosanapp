from django.db import models


class query_kosan(models.Model):
	nama_kosan = models.CharField(max_length=50)
	alamat_kosan = models.CharField(max_length=100)
	fasilitas = models.ForeignKey('fasilitas.Fasilitas', on_delete=models.CASCADE)

	def __str__(self):
		return self.nama_kosan