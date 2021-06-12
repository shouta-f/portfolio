from django.urls import path
from .views import WilldoList, WilldoDetail, WilldoCreate, WilldoDelete, WilldoUpdate, signupfunc

urlpatterns = [
    path('list/', WilldoList.as_view(), name='list'),
    path('detail/<int:pk>', WilldoDetail.as_view(), name='detail'),
    path('create/', WilldoCreate.as_view(), name='create'),
    path('delete/<int:pk>', WilldoDelete.as_view(), name='delete'),
    path('update/<int:pk>', WilldoUpdate.as_view(), name='update'),
    path('signup/', signupfunc, name='sign'),
]
