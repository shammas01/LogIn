from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import auth,messages
 
    

# Create your views here.
def log(request):
    if request.method=='POST':
        usr=request.POST['username']
        pswd=request.POST['password']
        
        aut=auth.authenticate(request, username=usr,password=pswd)
        if aut is not None:
            login(request,aut)
            return redirect('home')
        else:
            print('username or password error')
            messages.warning(request,'wrong usernsmr or password..!')

    return render(request ,'login.html')
    

def home(request):
    return render(request, 'home.html')



# def login(request):

#     if request.post:
#         name = request.name
#         password =request.password

#         login(name,password)
#         if login:
#             redirect