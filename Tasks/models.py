from django.db import models
from Users.models import Pengguna

class Tugas(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    pembuat = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='tugas_dibuat')
    assigned_to = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='tugas_ditugaskan')
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    batas_waktu = models.DateField()

    def __str__(self):
        return self.judul
