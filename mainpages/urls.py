from django.urls import path
# from rest_framework import routers
# from django.conf.urls import include
from .views import delete_all_foods, delete_user_likes, UpdateProfileImageView, GetImageView, like_food, generics_food_list, GetFoodByFoodName, LoginView, UserView, LogoutView, RegisterView,  generics_pk, generics_list, CalculateCalories, GetUsernameView, FoodsSearchView, user_liked_foods
from django.conf import settings
from django.conf.urls.static import static
# router = routers.DefaultRouter()
# router.register('foods', FoodsListView)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete_user/<int:pk>', generics_pk.as_view(), name='delete_user'),
    path('get/', generics_list.as_view(), name='get_users'),
    path('CalculateCalories/', CalculateCalories.as_view()),
    path('GetUsernameView/<str:username>/', GetUsernameView.as_view()),
    path('get-foods/', generics_food_list.as_view(), name='get-foods'),
    path('GetFoodView/<str:FoodName>/', GetFoodByFoodName.as_view()),
    path('foods/', FoodsSearchView.as_view()),
    path('foods-like/<int:food_id>/<int:user_id>/',
         like_food, name='like-food'),
    path('user/<int:user_id>/liked_foods/',
         user_liked_foods, name='user-liked-foods'),
    path('update-profile-image/', UpdateProfileImageView.as_view(),
         name='update-profile-image'),
    path('user-image/<int:id>/', GetImageView.as_view(), name='get-user-image'),
      path('delete-user-likes/<int:user_id>/', delete_user_likes, name='delete-user-likes'),
    path('delete-all-foods/', delete_all_foods, name='delete-all-foods'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
