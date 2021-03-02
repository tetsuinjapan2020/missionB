from django.db.backends.signals import connection_created

def connection_created_func(sender,**kwargs):
    print('DB connected')

connection_created.connect(connection_created_func)
