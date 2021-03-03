from django.db.backends.signals import connection_created
from polls.models import Question

def connection_created_func(sender,**kwargs):
    print('DB connected')
    queryset = Question.objects.all()
    print(queryset)

connection_created.connect(connection_created_func)
