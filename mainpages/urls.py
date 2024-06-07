from django.urls import path
from .views import DeleteUserDataView, GetUserInfoView, delete_all_recipes, delete_user_likes, UpdateProfileImageView, GetImageView, like_recipe, GetRecipes, GetRecipesByRecipeName, LoginView,  LogoutView, RegisterView, CalculateCalories, GetUsernameView, RecipesSearchView, user_liked_recipes

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('recipe-search/', RecipesSearchView.as_view()),
    path('calculate-calories/', CalculateCalories.as_view()),
    path('delete-user-data/', DeleteUserDataView.as_view(), name='delete-user-data'),
    path('get-username/<int:user_id>/', GetUsernameView.as_view()),
    path('get-user-info/<int:id>/', GetUserInfoView.as_view()),
    path('get-recipes/', GetRecipes.as_view(), name='get-foods'),
    path('get-recipe-by-name/<str:FoodName>/',
         GetRecipesByRecipeName.as_view()),
    path('foods-like/<int:food_id>/<int:user_id>/',
         like_recipe, name='like-food'),
    path('user/<int:user_id>/liked_foods/',
         user_liked_recipes, name='user-liked-foods'),
    path('update-profile-image/', UpdateProfileImageView.as_view(),
         name='update-profile-image'),
    path('user-image/<int:id>/', GetImageView.as_view(), name='get-user-image'),
    path('delete-user-likes/<int:user_id>/',
         delete_user_likes, name='delete-user-likes'),
    path('delete-all-foods/', delete_all_recipes, name='delete-all-foods'),

]
