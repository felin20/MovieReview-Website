from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home1/', views.home1, name='home1'),
    path('search/', views.search, name='search'),
    path('welcome/', views.welcome, name='welcome'),
    path('ulogin/', views.ulogin, name='ulogin'),
    path('movlist/', views.movlist, name='movlist'),
    path('det/<str:Moviename>/', views.mdetail, name='det'),
    path('register/', views.register, name='reg'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('adrev/', views.adrev, name='adrev'),
    path('editto/<int:id>/', views.editto, name='editto'),
    path('todelete/<int:id>/', views.todelete, name='todelete'),
    path('my-reviews/', views.MyReviewsView.as_view(), name='myrev'),
    path('edit-review/<int:id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:id>/', views.delete_review, name='delete_review')
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development
urlpatterns += staticfiles_urlpatterns()
