import imp


import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # 질문내용 최대 200자로 세팅
    pub_date = models.DateTimeField('date published') # 생성날짜
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_Data >= timezone.now() - datetime.timedelta(dats=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # ForeignKey : Question이라는 데이터 모델을 참조하겠다
    choice_text = models.CharField(max_length=200) # 선택지에 해당하는 질문
    votes = models.IntegerField(default=0) # 투표수
    def __str__(self):
        return self.choice_text
    
