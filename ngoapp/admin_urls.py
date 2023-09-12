from django.urls import path
from django.views.generic import TemplateView

from ngoapp.admin_views import AdminIndexView, ApproveView, RejectView, View_projects, ViewNgo, Viewproject, Viewspecificddonation, Viewspecificexpenditure, ngo_verify, user_verify



urlpatterns = [
    path('', AdminIndexView.as_view()),
    path('ngo_verify',ngo_verify.as_view()),
    path('user_verify',user_verify.as_view()),
    path('s_approve',ApproveView.as_view()),
    path('s_reject',RejectView.as_view()),
    path('view_ngo', ViewNgo.as_view()),
    path('view_pro', View_projects.as_view()),

    path('view_project', Viewproject.as_view()),
    path('v_sdonate', Viewspecificddonation.as_view()),
    path('a_sexp', Viewspecificexpenditure.as_view()),



    


]

def urls():
    return urlpatterns, 'admin', 'admin'
















