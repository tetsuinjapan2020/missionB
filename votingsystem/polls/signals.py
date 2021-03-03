from django.db.backends.signals import connection_created
from polls.models import Question, Choice

default_question = "Do you agree that Wuhan coronavirus is created by China?"
#default_question = "Temp"

def connection_created_func(sender,**kwargs):
    print('DB connected')
    check_default_question()

def check_default_question():
    try:
        question = Question.objects.get(question_text=default_question)
    except:
        print('Cannot find the default question in the database.')
        question = Question.objects.create(question_text=default_question)
        agree = Choice.objects.create(choice_text='Agree', question_id=question.id)
        disagree = Choice.objects.create(choice_text='Disagree', question_id=question.id)
        question.save()
    else:
        print('The default question is in the database.')


connection_created.connect(connection_created_func)
