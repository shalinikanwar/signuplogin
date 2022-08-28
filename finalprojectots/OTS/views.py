from django.shortcuts import render

from OTS.models import User

from django.http import HttpResponse,HttpResponseRedirect
def signup(request):

    d1={}

    try:
    

      if request.GET['error']==str(1):

        d1['errmsg']='Username already taken'

    except:

        d1['errmsg']=''


    res=render(request,'OTS/signup.html',d1)
    return res

def saveUser(request):

    user=User()

    u=User.objects.filter(username=request.POST['username'])

    if not u:

        user.username=request.POST['username']

        user.password=request.POST['password']
        user.firstname=request.POST['firstname']
        user.lastname=request.POST['lastname']
        user.email=request.POST['email']
        user.password=request.POST['password']
        user.confirmpassword=request.POST['confirmpassword']
        if(user.password==user.confirmpassword) :
           user.save()

           url="http://localhost:8000/OTS/login/"

        #user.role="patient"
        else:
            
             url="http://localhost:8000/OTS/signup?password not same/"
            
        
    else:

        url="http://localhost:8000/OTS/signup?error=1/"
        
        

    return HttpResponseRedirect(url)


def login(request):
  
  res=render(request,'OTS/login.html')
  return res

  



def loginValidation(request):
    #u=User.objects.filter(username=request.POST['username'],password=request.POST['password'])
    try: #login successful
        u=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        request.session['username']=u.username
        request.session['email']=u.email
        
        url="http://localhost:8000/OTS/home/"
    except:
        url="http://localhost:8000/OTS/login/"
    return HttpResponseRedirect(url)





   

 
  
