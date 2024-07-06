from rest_framework import serializers
from .models import Tugas

class TugasSerializer(serializers.ModelSerializer):
    batas_waktu = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Tugas
        fields = ('id', 'judul', 'deskripsi', 'pembuat','assigned_to', 'tanggal_dibuat', 'batas_waktu')
