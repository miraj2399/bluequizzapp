
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.authtoken.models import Token


from rest_framework.decorators import api_view,permission_classes

from mainapp.models import Quiz,Question
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from .serializers import QuestionSerializer, QuizSerializer
from rest_framework import serializers
from authapp.serializer import loginSerializer, registerSerializer
from django.contrib.auth import authenticate,login, logout



# Create your views here.
'''
LOGIN
LOGOUT
REGISTER
'''


@api_view(['POST'])
@permission_classes([])
def view_login(request):
    if request.method == 'POST':
        serializer= loginSerializer(data =request.data)
        data ={}
        if serializer.is_valid():
            user = authenticate(username = serializer.data["username"], password = serializer.data["password"])
            if user is not None:
                login(request,user)
                token = Token.objects.get(user = user).key
                data['token'] = token
                return Response(data)
        else:
            return Response("Invalid credential")

@api_view(['POST'])
@permission_classes([])
def view_register(request):
    if request.method == "POST":
        serializer = registerSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            if User.objects.filter(username = serializer.data['username']).exists() or User.objects.filter(username = serializer.data['email']).exists():
                return Response("Username or Email already exist")
            user = User.objects.create_user(serializer.data['username'],serializer.data['email'],serializer.data['password'])
            token = Token.objects.get(user = user).key
            data['token'] = token
            return Response(data)
        return Response("Invalid JSON data")
    else:
        return Response("Only POST method is accepted")

@api_view(['GET'])
@permission_classes([])
def guide(request):
    urls = {
        "REGISTER":'api/register',
        "LOGIN": 'api/login',
        "DASHBOARD":  '/api_dashboard',
        "GET QUIZ":'api_get_quiz/<str:pk>/',
        "CREATE":'api_create_quiz/',
        "UPDATE":'/api_quiz_update/<str:pk>/',
        "DELETE": 'api/api_delete/<str:pk>/',
    }
    return Response(urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    quiz= Quiz.objects.filter(author = request.user)
    serializer = QuizSerializer(quiz, many = "True")
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_quiz(request,pk):
    quiz = Quiz.objects.filter(id = pk)
    if(quiz[0].author == request.user):
        serializers = QuizSerializer(quiz,many = "False")
        return Response(serializers.data)
    return Response('Only accessible to author')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.errors)
            return Response(request.data)
    return Response(request.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_question_id(request):
    if request.method == 'GET':
        qid = []
        quizes = Quiz.objects.filter(author = request.user)
        for quiz in quizes:
            for q in quiz.questions.all():
                qid.append(q.id)
    
    return Response({"qid":qid})

