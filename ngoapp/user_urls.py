from django.urls import path
from django.views.generic import TemplateView

from ngoapp.user_views import   Donation, EditProfile, ProfileView, UserndexView, View_projects, ViewDonation, ViewNgo, Viewproject, Viewspecificddonation, Viewspecificexpenditure




urlpatterns = [
    path('', UserndexView.as_view()),
    path('profile', ProfileView.as_view()),
    path('edit_profile', EditProfile.as_view()),
    path('donation', Donation.as_view()),
    path('view_donation', ViewDonation.as_view()),
    path('view_ngo', ViewNgo.as_view()),
    path('view_pro', View_projects.as_view()),


    path('view_project', Viewproject.as_view()),
    path('v_sdonate', Viewspecificddonation.as_view()),
    path('a_sexp', Viewspecificexpenditure.as_view()),




    



    


]

def urls():
    return urlpatterns, 'user', 'user'



