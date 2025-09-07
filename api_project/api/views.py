from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Read: anyone; Write: authenticated users.
    (Built-in class; shown here for clarity.)
    """
    pass

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # keep the list endpoint open if desired

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

