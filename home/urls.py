from django.urls import path
from .import views
from .views import edit_password
from .views import change_password
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home1.as_view(), name='home1'),
    path('home2/', views.home2, name='home2'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
    path('job_page/', views.job_page.as_view(), name='job_page'),
    path('wishlist_page/', views.wishlist_page.as_view(), name='wishlist_page'),
    path('job_details/<int:pk>', views.job_details.as_view(), name='job_details'),
    path('resume/', views.resume, name='resume'),
    path('pricing/', views.pricing, name='pricing'),
    path('browse_job/', views.browse_job, name='browse_job'),
    path('signinn', views.signinn, name="signinn"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('profile/', views.profile.as_view(), name="profile"),
    path('cv/', views.cv, name="cv"),
    path('job_post/', views.job_post, name="job_post"),
    path('wishlist_post/', views.wishlist_post, name="wishlist_post"),
    path('all_cv_form/', views.all_cv_form, name="all_cv_form"),
    path('search/', views.search, name="search"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('edit_profile_form/', views.edit_profile_form, name="edit_profile_form"),
    path('profile_pic_form/', views.profile_pic_form, name="profile_pic_form"),
    path('profile_picture/', views.profile_picture.as_view(), name="profile_picture"),
    path('<int:pk>/delete_profile_picture/',
         views.delete_profile_picture.as_view(), name="delete_profile_picture"),
    path('<int:pk>/your_cv', views.your_cv.as_view(), name="your_cv"),
    path('edit_password/',edit_password.as_view(),name='edit_password'),
    path('password/',change_password.as_view(template_name = "change.html")),
    path('apply_job_form/',views.apply_job_form,name = "apply_job_form"),



]
