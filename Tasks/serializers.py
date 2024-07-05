from rest_framework import serializers
from .models import Tugas

class TugasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tugas
        fields = ('id', 'judul', 'deskripsi', 'pembuat','assigned_to', 'kategori', 'tanggal_dibuat', ' batas_waktu')
