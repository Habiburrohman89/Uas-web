from django.db import models
from Users.models import Pengguna
from Kategori.models import Kategori

class Tugas(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    pembuat = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='tugas_dibuat')
    assigned_to = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='tugas_ditugaskan')
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    batas_waktu = models.DateField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='tugas')


    def __str__(self):
        return self.judul
