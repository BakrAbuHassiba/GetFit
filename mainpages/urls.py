from django.urls import path
# from rest_framework import routers
# from django.conf.urls import include
from .views import FoodsView, GetFoodView, LoginView, UserView, LogoutView, RegisterView,  generics_pk, generics_list, CalculateCalories, GetUsernameView, FoodsListView

# router = routers.DefaultRouter()
# router.register('foods', FoodsListView)

urlpatterns = [
    # path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete_user/<int:pk>', generics_pk.as_view(), name='delete_user'),
    path('get/', generics_list.as_view(), name='get_users'),
    path('CalculateCalories/', CalculateCalories.as_view()),
    path('GetUsernameView/<str:username>/', GetUsernameView.as_view()),
    path('Foods/', FoodsView.as_view()),
    path('GetFoodView/<str:FoodName>/', GetFoodView.as_view()),
    path('foods/', FoodsListView.as_view())


]
