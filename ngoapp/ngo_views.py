
from tkinter import PROJECTING
from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from ngoapp.models import   assigneddonation, expenditure, ngo_reg, project, udonation




class NgoIndexView(TemplateView):
    template_name = 'ngo/index.html'

class ViewDonation(TemplateView):
    template_name = 'ngo/view_donations.html'


    def get_context_data(self, **kwargs):

        context = super(ViewDonation,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        
        c = udonation.objects.filter(ngo_id=ngo.id, status='not used yet')
        context['fe'] = c
        return context
    


class Addproject(TemplateView):
    template_name = 'ngo/add_project.html'


    
    def post(self, request, *args, **kwargs):

        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)


        pname=request.POST['pname']
        amt = request.POST['amount']
        des = request.POST['pdes'] 
        photo = request.FILES['image']
        pm = FileSystemStorage()
        photos = pm.save(photo.name, photo)
       
        try:
            
            se=project()
            se.ngo_id=ngo.id
            se.pname=pname
            se.amount=amt
            se.pdes=des
            se.photo=photos
            se.save()

            return render(request, 'ngo/index.html', {'message': "Project Added Successfully "})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'ngo/index.html',{'message':messages})

    
class Viewproject(TemplateView):
    template_name = 'ngo/view_projects.html'


    def get_context_data(self, **kwargs):

        context = super(Viewproject,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.filter(ngo_id=ngo.id)
        context['p'] = c
        return context
    

class Assigndonation(TemplateView):
    template_name = 'ngo/assign_donation.html'


    def get_context_data(self, **kwargs):

        id =self.request.GET['id']
        context = super(Assigndonation,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.filter(ngo_id=ngo.id)

        context['id']=id
        context['p'] = c
        return context
    
    def post(self, request, *args, **kwargs):

        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        

        pid=request.POST['id']
        did = request.POST['did']
        n=udonation.objects.get(id=did)
        # des = request.POST['pdes'] 
        # photo = request.FILES['image']
        # pm = FileSystemStorage()
        # photos = pm.save(photo.name, photo)
       
       
            
        se=assigneddonation()
        se.donation_id=did
        se.project_id=pid
        se.amount=n.amount
        se.ngo_id=ngo.id
            # se.pdes=des
            # se.photo=photos
        se.save()
        n.status='used'
        n.project_id=pid
        n.save()

        return render(request, 'ngo/index.html', {'message': "Donation Assigned Successfully "})
    

class Viewassigneddonation(TemplateView):
    template_name = 'ngo/view_assigneddonations.html'


    def get_context_data(self, **kwargs):

        context = super(Viewassigneddonation,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        
        c = assigneddonation.objects.filter(ngo_id=ngo.id)
        context['fe'] = c
        return context
    
class Viewspecificddonation(TemplateView):
    template_name = 'ngo/view_specificdonations.html'

    def get_context_data(self, **kwargs):
        
        id =self.request.GET['id']
        context = super(Viewspecificddonation,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        
        c = assigneddonation.objects.filter(project_id=id)
        p=project.objects.get(id=id)

        price = 0
        for i in c:
            price = price + int(i.amount)


        context['asz'] = price
        context['fe'] = c
        context['p'] = p
        return context

class AddExpenditure(TemplateView):
    template_name = 'ngo/add_expenditure.html'


    def get_context_data(self, **kwargs):

        # id =self.request.GET['id']
        context = super(AddExpenditure,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.filter(ngo_id=ngo.id)

        context['id']=id
        context['p'] = c
        return context
    
    def post(self, request, *args, **kwargs):

        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)


        pid=request.POST['id']
        etype = request.POST['etype']
        amount = request.POST['amount']
        edes = request.POST['edes']
    
        photo = request.FILES['image']
        pm = FileSystemStorage()
        photos = pm.save(photo.name, photo)
       
        try:
            
            se=expenditure()
            se.project_id=pid
            se.etype=etype
            se.amount=amount
            se.edes=edes
            se.bill=photos
            se.save()
           

            return render(request, 'ngo/index.html', {'message': "Expenditure Added Successfully "})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'ngo/index.html',{'message':messages})

class Viewspecificexpenditure(TemplateView):
    template_name = 'ngo/view_expenditure.html'

    def get_context_data(self, **kwargs):
        
        id =self.request.GET['id']
        context = super(Viewspecificexpenditure,self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        ngo=ngo_reg.objects.get(user_id=user.id)
        
        c = expenditure.objects.filter(project_id=id)
        p=project.objects.get(id=id)

        price = 0
        for i in c:
            price = price + int(i.amount)


        context['a'] = price

        context['p'] = p

        context['ex'] = c
        return context