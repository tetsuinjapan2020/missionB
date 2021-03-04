# ACCESS missionB
This is the project for ACCESS companay. 

## Requriments
The projecet is based on Django REST framework,  
  
so we have to install Django and Django-REST-framework at first.  
  
Install [Django](https://github.com/django/django)  

`pip install django`  
  
  
Install [Django-REST-framework](https://www.django-rest-framework.org/)  

`pip install djangorestframework`

## Start  


`python manage.py runserver [port]`  

## The APIs for ACCESS Companay  
  
* Get the current votes count of wuhan coronavirus  
`GET {{server_ip}}:{{server_port}}/api/polls/access/missionb/wuhan_vote/`  

![image](https://github.com/tetsuinjapan2020/missionB/blob/main/img/get_result.png)  

* Vote  
`PATCH {{server_ip}}:{{server_port}}/api/polls/access/missionb/wuhan_vote/`  
  
![image](https://github.com/tetsuinjapan2020/missionB/blob/main/img/vote.png) 
