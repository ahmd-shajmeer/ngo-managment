from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from ngoapp.models import UserType, ngo_reg, user_reg


# from restaurantapp.models import UserType, customer_reg, restaurant_reg
# from college.models import UserType, shop_reg,user_reg



class IndexView(TemplateView):
    template_name = 'index.html'


class UserReg(TemplateView):
    template_name = 'user_reg.html'

class NgoReg(TemplateView):
    template_name = 'ngo_reg.html'

    def post(self, request, *args, **kwargs):

        name = request.POST['nname']
        oname = request.POST['oname']

        ph = request.POST['phone']
        em = request.POST['email']
        department = request.POST['address']
        image = request.FILES['licence']
        username = request.POST['username']
        password = request.POST['password']
        im = FileSystemStorage()
        images = im.save(image.name, image)
        
        try:
            user = User.objects.create_user(first_name=name,email=em,password=password,username=username,last_name='0')
            user.save()
            se=ngo_reg()
            se.user=user
            se.oname=oname
            se.licence=images

            se.phone=ph
            se.address=department
            se.save()

            usertype = UserType()
            usertype.user = user
            usertype.type ='ngo'
            usertype.save()
            return render(request, 'index.html', {'message': "successfully Registered"})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})
        

class UserReg(TemplateView):
    template_name = 'user_reg.html'

    def post(self, request, *args, **kwargs):

        name = request.POST['name']

        ph = request.POST['phone']
        em = request.POST['email']
        department = request.POST['address']
        image = request.FILES['ID']
        photo = request.FILES['photo']

        username = request.POST['username']
        password = request.POST['password']
        im = FileSystemStorage()
        images = im.save(image.name, image)
        pm = FileSystemStorage()
        photo = pm.save(photo.name, photo)
        
        try:
            user = User.objects.create_user(first_name=name,email=em,password=password,username=username,last_name='0')
            user.save()
            se=user_reg()
            se.user=user
            se.idproof=images
            se.photo=photo
            se.phone=ph
            se.address=department
            se.save()

            usertype = UserType()
            usertype.user = user
            usertype.type ='user'
            usertype.save()
            return render(request, 'index.html', {'message': "successfully Registered"})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})


class login_view(TemplateView):
    template_name="login.html"
    def post(self,request,*args,**kwargs):
            uname=request.POST['username']
            password =request.POST['password']
            user=auth.authenticate(username=uname,password=password)
            if user is not  None:
                login(request,user)
                if user.last_name=='1':
                    if user.is_superuser:
                        return redirect('/admin')
                    elif UserType.objects.get(user_id=user.id).type=="ngo":
                        return redirect('/ngo')
                    elif UserType.objects.get(user_id=user.id).type == "user":
                        return redirect('/user')
                    
                    
                    else:
                        return render(request,'login.html',{'message':" User Account Not Authenticated"})

                else:
                    return render(request,'login.html',{'message':" User Account Not Authenticated"})
            else:
                return render(request,'index.html',{'message':"Invalid Username or Password"})



