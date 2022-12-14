from django.urls import include, path
from recipes.views import (DownloadShoppingCart, IngredientViewSet,
                           RecipeViewSet, TagViewSet, fav_recipe,
                           shopping_cart)
from rest_framework.routers import DefaultRouter
from users.views import (MeDetail, Subscriptions, UserDetail, UserListCreate,
                         subscribe)

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('recipes/<int:recipe_id>/favorite/', fav_recipe, name='favorite'),
    path('recipes/<int:recipe_id>/shopping_cart/',
         shopping_cart, name='shopping'),
    path('recipes/download_shopping_cart/',
         DownloadShoppingCart.as_view(), name='download'),

    path('users/', UserListCreate.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='profile'),
    path('users/me/', MeDetail.as_view(), name='me'),
    path('users/<int:author_id>/subscribe/', subscribe, name='subscribe'),
    path('users/subscriptions/',
         Subscriptions.as_view(), name='subscriptions'),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('', include(router.urls)),
]
