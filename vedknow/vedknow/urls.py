
from django.contrib import admin
from django.urls import path, include
from stackusers import views as user_view
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls.static import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stackbase.urls')),

    # Authentication System
     path('register/', user_view.register, name="register"),
     path('login/', auth_view.LoginView.as_view(template_name="stackusers/login.html"), name='login'),
     path('logout/', auth_view.LogoutView.as_view(template_name="stackusers/logout.html"), name='logout'), 

    # # Profile system
    path('profile/', user_view.profile, name="profile"),
    path('profile/update/', user_view.profile_update, name="profile_update"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
