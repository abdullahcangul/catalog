from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(req):
    if req.method=='POST':
        username=req.POST["username"]
        password=req.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            messages.add_message(req,messages.SUCCESS,"basarılı bir sekilde oturum açıldı")
            return redirect("index")
        else:
            messages.add_message(req,messages.ERROR,"Kullanıcı adı veya password hatalı")
            return redirect("login")
    else:        
        return render(req,"user/login.html")

def register(req):
    if req.method=='POST':
        username=req.POST["username"]
        email=req.POST["email"]
        password=req.POST["password"]
        repassword=req.POST["repassword"]

        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(req,messages.WARNING,"kullanıcı adi daha önce alınmış")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(req,messages.WARNING,"eposta  daha önce alınmış")
                    return redirect("register") 
                else:
                    user=User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    messages.add_message(req,messages.SUCCESS,"Kayıt basarılı bir sekilde gerçekleşdi")
                    return redirect("login")

        else:
            messages.add_message(req,messages.WARNING,"Sifreler uyuşmuyor")
            redirect("register")
    else:
        return render(req,"user/register.html")
   
        
        

    
def logout(req):
    if req.method=='POST':
        auth.logout(req)
        messages.add_message(req,messages.SUCCESS,"Oturum kapatıldı")
        redirect("index")
    return render(req,"user/logout.html")