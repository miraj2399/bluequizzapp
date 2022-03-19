from turtle import title
from rest_framework import serializers
from mainapp.models import Quiz,Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields =  ['question_text','option_1','option_2','option_3','option_4','option_correct','id','author']

    author= serializers.HiddenField(default=serializers.CurrentUserDefault())

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields  = ['id','title','questions']
    questions = QuestionSerializer(many = True, read_only = False)
    