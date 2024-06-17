from django.shortcuts import render,redirect
from django.views import View



class Main(View):
    def get(self,request):
        
        
        return render(request=request,template_name='chat/main.html')
    
    
class Login(View):
    def get(self,request):
        return render(request=request,template_name='chat/login.html')
    
    
        
    

class Register(View):
    def get(self,request):
        return render(request=request,template_name='chat/register.html')

   
    
    




    
    
class Home(View):
    def get(self,request):
       
       
        return render(request=request,template_name='chat/home.html')
        



class ChatPerson(View):
    def get(self,request,id):
        
       
        return render(request=request,template_name='chat/chat_person.html')