
from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from ngoapp.models import assigneddonation, expenditure, ngo_reg, project, udonation,  user_reg




class UserndexView(TemplateView):
    template_name = 'user/index.html'

class ProfileView(TemplateView):
    template_name = 'user/view_profile.html'


    def get_context_data(self, **kwargs):

        context = super(ProfileView,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)

        c = user_reg.objects.get(user_id=user.id)
        context['fe'] = c
        return context
    

class EditProfile(TemplateView):
    template_name = 'user/edit_profile.html'


    def get_context_data(self, **kwargs):

        context = super(EditProfile,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)

        c = user_reg.objects.filter(user_id=user.id)
        context['fe'] = c
        return context
    
    def post(self, request, *args, **kwargs):

        name = request.POST['name']
        id = request.POST['uid'] 
        id2 = request.POST['rid']
        ph = request.POST['phone']
        em = request.POST['email']
        department = request.POST['address']
        image = request.FILES['ID']
        username = request.POST['username']
        im = FileSystemStorage()
        images = im.save(image.name, image)
        photo = request.FILES['photo']
        pm = FileSystemStorage()
        photos = pm.save(photo.name, photo)
        
        try:
            i = User.objects.get(pk=id)
            u = user_reg.objects.get(pk=id2)
            i.first_name=name
            i.email=em
            i.username=username
            i.save()
           
            u.idproof=images
            u.phone=ph
            u.photo=photos
            u.address=department
            u.save()

          
            return render(request, 'user/index.html', {'message': "Updated Successfully"})
        except:
            messages = "Can't update"
            return render(request,'user/index.html',{'message':messages})

    

class Donation(TemplateView):
    template_name = 'user/donation.html'


    def get_context_data(self, **kwargs):

        context = super(Donation,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)

        c = ngo_reg.objects.all()
        context['fe'] = c
        return context
    
    def post(self, request, *args, **kwargs):

        user = User.objects.get(pk=self.request.user.id)
        reg=user_reg.objects.get(user_id=user.id)

        nid=request.POST['id']
        ph = request.POST['amount']
        em = request.POST['amt'] 
       
        try:
           
            se=udonation()
            se.reg_id=reg.id
            se.amt=em
            se.amount=ph
            se.ngo_id=nid
            se.status="not used yet"
            se.save()

            return render(request, 'user/index.html', {'message': "Successfully Donated"})
        except:
            messages = "Cant donate"
            return render(request,'user/index.html',{'message':messages})


class ViewDonation(TemplateView):
    template_name = 'user/view_donation.html'


    def get_context_data(self, **kwargs):

        context = super(ViewDonation,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        reg=user_reg.objects.get(user_id=user.id)


        c = udonation.objects.filter(reg_id=reg.id)
        context['fe'] = c
        return context
    
class ViewNgo(TemplateView):
    template_name = 'user/view_ngo.html'
    
    def get_context_data(self, **kwargs):
        context = super(ViewNgo,self).get_context_data(**kwargs)

        app_user = ngo_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['ngo'] = app_user
        return context
    
class View_projects(TemplateView):
    template_name = 'user/view_project.html'


    def get_context_data(self, **kwargs):
        
        id =self.request.GET['id']

        context = super(View_projects,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)
        # ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.filter(ngo_id=id)
        context['p'] = c
        return context  


class Viewproject(TemplateView):
    template_name = 'user/view_projects.html'


    def get_context_data(self, **kwargs):

        context = super(Viewproject,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)
        # ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.all()
        context['p'] = c
        return context
    

class Viewspecificddonation(TemplateView):
    template_name = 'user/view_specificdonations.html'

    def get_context_data(self, **kwargs):
        
        id =self.request.GET['id']
        context = super(Viewspecificddonation,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)
        # ngo=ngo_reg.objects.get(user_id=user.id)
        
        c = assigneddonation.objects.filter(project_id=id)
        p=project.objects.get(id=id)

        price = 0
        for i in c:
            price = price + int(i.amount)


        context['asz'] = price
        context['fe'] = c
        context['p'] = p

        return context


class Viewspecificexpenditure(TemplateView):
    template_name = 'user/view_expenditure.html'

    def get_context_data(self, **kwargs):
        
        id =self.request.GET['id']
        context = super(Viewspecificexpenditure,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)
        # ngo=ngo_reg.objects.get(user_id=user.id)
        
        c = expenditure.objects.filter(project_id=id)
        p=project.objects.get(id=id)

        price = 0
        for i in c:
            price = price + int(i.amount)


        context['a'] = price
        context['p'] = p
        context['ex'] = c


        return context

