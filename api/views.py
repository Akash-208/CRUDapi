from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Employee
from . serializer import EmployeeSerializer


# Create your views here.

def Home(request):
        paths = {
        'users' : "For getting all user details",
        'user/id':"for getting a specific user",
        'new':"for creating a new user",
        'update/id':'for updating the data of a user',
        'delete/id':"for deleting a specific user's datat"
    }
    return JsonResponse(paths)

@api_view(['GET'])
def Users(request):
    allUsers = Employee.objects.all()
    searlizer = EmployeeSerializer(allUsers,many=True)
    return Response(searlizer.data)

@api_view(['GET'])
def User(request,pk):
    singleUser = Employee.objects.get(id=pk)
    searlizer = EmployeeSerializer(singleUser,many=False)
    return Response(searlizer.data)

@api_view(['POST'])
def createUser(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateUser(request,pk):
    user = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=user,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request,pk):
    user = Employee.objects.get(id=pk)
    user.delete()
    return Response('Deleted Succesfully')    
    



