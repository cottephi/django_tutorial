from django.urls import path
from .views import blog_list, blog_detail, blog_delete

urlpatterns = [
    path("", blog_list),
    path("posts/<post_id>/", blog_detail),
    path("posts/<post_id>/delete/", blog_delete)
]
