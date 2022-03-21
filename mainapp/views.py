import re
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .models import Question,Quiz
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    else:
        return redirect('auth/')

def createquiz(request):
    if request.method == 'POST':
        number = request.POST.get('number_of_question',0)
        title = request.POST.get('title')
        context = {'range':range(1,int(number)+1),'title':title,'number':number}
        return render(request,'createquiz2.html',context)
    return render(request,'createquiz1.html')



def dashboard(request):
    quizes = Quiz.objects.filter(author = request.user)
    return render(request,'dashboard.html',{'quizes':quizes})


def savequiz(request):
    if request.method == 'POST':
        i = 1
        quiz = Quiz()
        quiz.title = request.POST.get('title')
        quiz.author = request.user
        quiz.save()
        while(request.POST.get(str('question_'+str(i)),'')!=''):
            question = Question()
            question.question_text= request.POST.get('question_'+str(i))
            question.option_1 = request.POST.get("question_"+str(i)+"_opt1","")
            question.option_2 = request.POST.get("question_"+str(i)+"_opt2","")
            question.option_3 = request.POST.get("question_"+str(i)+"_opt3","")
            question.option_4 = request.POST.get("question_"+str(i)+"_opt4","")
            question.option_correct= request.POST.get('question_'+str(i)+'_correct')
            question.author = request.user
            question.save()
            quiz.questions.add(question)
            i = i+1
        quiz.save()
    return redirect('dashboard')



def takequiz(request,quiz_id):
    
    
    quiz_id = int(quiz_id)
    quiz = Quiz.objects.get(pk =quiz_id)
    if request.method == 'POST':
        correct = 0
        total = 0
        for question in quiz.questions.all():
            if str(question.option_correct) == request.POST[str(question.id)]:
                correct +=1
                total+=1
            else:
                total+=1
        wrong = total - correct
        return render(request,'result.html',{'wrong':wrong,'correct':correct})

    return render (request,'takequiz.html',{'quiz':quiz})

def quizresult(request,quiz_id):

   
    


    return JsonResponse({"3":request.POST.get(3,0)})