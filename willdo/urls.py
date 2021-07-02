from django.urls import path
from .import views
from .views import  WilldoDetail, WilldoCreate, WilldoDelete, WilldoUpdate, WilldoList, signupfunc, loginfunc, logoutfunc

urlpatterns = [
    path('list/', WilldoList.as_view(), name='list'),
    path('detail/<int:pk>', WilldoDetail.as_view(), name='detail'),
    path('create/', WilldoCreate.as_view(), name='create'),
    path('delete/<int:pk>', WilldoDelete.as_view(), name='delete'),
    path('update/<int:pk>', WilldoUpdate.as_view(), name='update'),
    path('description/', views.descriptionfunc, name='description'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout', logoutfunc, name='logout')
]
