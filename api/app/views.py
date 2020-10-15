from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from app.models import Person
from app.serializers import PersonSerializer

@csrf_exempt
def personApi(request, id=0):
    if request.method == "GET":
        persons = Person.objects.all()
        if persons:
            persons_serializer = PersonSerializer(persons, many=True)
            return JsonResponse(persons_serializer.data, safe=False)#to tell django we are fine if there are issues converting to json
        return JsonResponse("No Data", safe=False)
    
    elif request.method == "POST":
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == "PUT":
        person_data = JSONParser().parse(request)
        person = Person.objects.get(personid=person_data['personid'])
        person_serializer = PersonSerializer(person, data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse("Updated Succesfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == "DELETE":
        person = Person.objects.get(personid=id)
        person.delete()
        return JsonResponse("Deleted Successfully!", safe=False)