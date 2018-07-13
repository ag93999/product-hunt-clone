from django.urls import path, include
from products import views


urlpatterns = [
    # ex: products/create/
    path('create/', views.create, name='create'),
    # ex: products/id/
    path('<int:product_id>', views.detail, name='detail'),
    # ex: products/id/upvote/
    path('<int:product_id>/upvote/', views.upvote, name='upvote'),
]