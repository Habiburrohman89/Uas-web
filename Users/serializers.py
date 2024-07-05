from rest_framework import serializers
from .models import Pengguna

class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ('id', 'email', 'nama_lengkap', 'tanggal_lahir', 'aktif', 'staf')
