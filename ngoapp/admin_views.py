
from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from ngoapp.models import assigneddonation, expenditure, ngo_reg, project, user_reg




class AdminIndexView(TemplateView):
    template_name = 'admin/index.html'


    
class ngo_verify(TemplateView):
    template_name = 'admin/approve_ngo.html'

    def get_context_data(self, **kwargs):
        context = super(ngo_verify,self).get_context_data(**kwargs)

        app_rj = ngo_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['app_n'] = app_rj
        return context

class user_verify(TemplateView):
    template_name = 'admin/approve_user.html'

    def get_context_data(self, **kwargs):
        context = super(user_verify,self).get_context_data(**kwargs)

        app_rj = user_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['app_u'] = app_rj
        return context
    


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})
    
class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Rejected"})
    

    

class ViewNgo(TemplateView):
    template_name = 'admin/view_ngo.html'
    
    def get_context_data(self, **kwargs):
        context = super(ViewNgo,self).get_context_data(**kwargs)

        app_user = ngo_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['ngo'] = app_user
        return context
    
    
class View_projects(TemplateView):
    template_name = 'admin/view_project.html'


    def get_context_data(self, **kwargs):
        
        id =self.request.GET['id']

        context = super(View_projects,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)
        # ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.filter(ngo_id=id)
        context['p'] = c
        return context  
    

class Viewspecificexpenditure(TemplateView):
    template_name = 'admin/view_expenditure.html'

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


    
class Viewproject(TemplateView):
    template_name = 'admin/view_projects.html'


    def get_context_data(self, **kwargs):

        context = super(Viewproject,self).get_context_data(**kwargs)
        # user = User.objects.get(pk=self.request.user.id)
        # ngo=ngo_reg.objects.get(user_id=user.id)
        c = project.objects.all()
        context['p'] = c
        return context
    


class Viewspecificddonation(TemplateView):
    template_name = 'admin/view_specificdonations.html'

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

