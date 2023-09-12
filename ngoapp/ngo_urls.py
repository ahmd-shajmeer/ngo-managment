from django.urls import path
from django.views.generic import TemplateView

from ngoapp.ngo_views import  AddExpenditure, Addproject, Assigndonation, NgoIndexView, ViewDonation, Viewassigneddonation, Viewproject, Viewspecificddonation, Viewspecificexpenditure




urlpatterns = [
    path('', NgoIndexView.as_view()),
    path('view_donations', ViewDonation.as_view()),
    path('add_project', Addproject.as_view()),
    path('view_project', Viewproject.as_view()),
    path('n_donate', Assigndonation.as_view()),
    path('v_adonate', Viewassigneddonation.as_view()),
    path('v_sdonate', Viewspecificddonation.as_view()),
    path('a_exp', AddExpenditure.as_view()),
    path('a_sexp', Viewspecificexpenditure.as_view()),


  

    


]

def urls():
    return urlpatterns, 'ngo', 'ngo'



