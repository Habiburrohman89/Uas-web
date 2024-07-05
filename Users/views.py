from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pengguna
from .serializers import PenggunaSerializer

@api_view(['GET', 'POST'])
def pengguna_list(request):
    """
    List semua pengguna atau buat pengguna baru.
    """
    if request.method == 'GET':
        pengguna = Pengguna.objects.all()
        serializer = PenggunaSerializer(pengguna, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PenggunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pengguna_detail(request, pk):
    """
    Retrieve, update atau hapus seorang pengguna.
    """
    try:
        pengguna = Pengguna.objects.get(pk=pk)
    except Pengguna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PenggunaSerializer(pengguna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PenggunaSerializer(pengguna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pengguna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

