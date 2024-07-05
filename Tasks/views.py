from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tugas
from .serializers import TugasSerializer

@api_view(['GET', 'POST'])
def tugas_list(request):
    """
    List semua pengguna atau buat pengguna baru.
    """
    if request.method == 'GET':
        tugas = Tugas.objects.all()
        serializer = TugasSerializer(tugas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TugasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tugas_detail(request, pk):
    """
    Retrieve, update atau hapus seorang pengguna.
    """
    try:
        tugas = Tugas.objects.get(pk=pk)
    except Pengguna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TugasSerializer(tugas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TugasSerializer(tugas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tugas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

