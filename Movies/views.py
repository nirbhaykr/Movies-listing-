from rest_framework import viewsets
from rest_framework.response import Response
from Movies.serailizer import MovieSerializer
from Movies.models import Movies
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST,\
     HTTP_200_OK

# Create your views here.


class MovieChangeViewSet(viewsets.ModelViewSet):
    """
        Class for handling Movie request
    """
    serializer_class = MovieSerializer
    model = Movies
    queryset = Movies.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Movie added successfully"},\
                             status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(instance=self.get_object(), data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Movie updated successfully"},\
                             status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            if request.query_params.get('name'):
                self.object_list = Movies.objects.filter(name__icontains=\
                                             request.query_params.get('name'))
            else:
                self.object_list = Movies.objects.all()
        except:
            self.object_list = []

        page = self.paginate_queryset(self.object_list)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(self.object_list, many=True)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()
            return Response({"Message": "Movie deleted successfully"},\
                                            status=HTTP_200_OK)
        except:
            return Response({"Message": "Movie deleted failed"},\
                             status=HTTP_400_BAD_REQUEST)
