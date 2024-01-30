# PClubSoftwareDiv

#THIS PROJECT IS CREATED FOR INDUCTION TASK OF PPROGRAMMING CLUB IIT INDORE SOFTWARE DIVISION

#CONTENTS IS AS FOLLOW

#PROBLEM STATEMENT

We were asked to create an app or a website which can detect PROXY

#RESOURCES USED

DJANGO,Bootstarp and a little ChatGPT

#BASIC IDEA

The basic idea is that the web will take attendance of user and in the form of his roll no and a password and also register the ip addreess of the device from which the user is marking the attendance and if it is found that same ip address is received by the admin it will mark the entry with red.We were also asked to allow admin to add csv files but due to lack of time I was not able to do that.

#BRIEF EXPLANATION

For the implementation of the idea I have used Djnago framework of python and also took details like nav bar from bootstrap, I started by adjusting url.py and setting.py files then created the model Present which can take inputs from user and register them in the sql lite database , next I declared a function with some help from chatgpt that check if a new entry is received and if it is same as previous one it will mark both as red.In this way proxy can be detected.

#How to RUN

Download all the files and open them in VSCode and run the command python manage.py runserver in terminal then click on generated link and the webiste will be opened, in case you are not able to run it on your device or facing technical issues I have also attached a video demo file.

#DEMO LINK

https://drive.google.com/file/d/1YC8WdivfRxJUbFscmAOpENqN6uO7Xrr8/view?usp=sharing

In the demo you can see that 500 ip address was not marked as red but I updated my code after that so both entries with same ip address will be marked red

#CREDITS

Django

Code with Harry 

Bootstrap

ChatGPT
