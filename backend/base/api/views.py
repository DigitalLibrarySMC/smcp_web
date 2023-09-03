from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import personSerializer
from base.models import person
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/parishmembers',
        'GET /api/results',
    ]
    return Response(routes)
@api_view(['GET'])
def getPersons(request):
    persons = person.objects.all()
    serializer = personSerializer(persons,many=True)
    print(serializer)
    return Response(serializer.data)