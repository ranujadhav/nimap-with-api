from django.urls import path
from.import views
from.views import ClientCreate,ClientList,ClientUpdate,ClientDelete
urlpatterns=[
  
    path('userreg',views.userreg,name='userreg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'), 
    path('clientreg',views.clientreg,name='clientreg'),
    path('clientlogin',views.clientlogin,name='clientlogin'),
    path('clientcreate',ClientCreate.as_view()),
    path('clientlist',ClientList.as_view()),
    path('<pk>/jupdate',ClientUpdate.as_view()),
    path('<pk>/jdelete',ClientDelete.as_view()),
    path('project',views.project,name='project'),
    path('assign',views.assign,name='assign'),
    path('home',views.home,name='home'),
    path('projectinsert',views.projectinsert,name='projectinsert'),
  


]   