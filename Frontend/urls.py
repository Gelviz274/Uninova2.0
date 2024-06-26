from django.urls import path
from .views import *#iniciar_sesion,registrarse, Inicio, Admin_Inicio, Prueba, activate, cerrar_sesion, edit_user, perfil_usuario
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('crear_proyecto/', crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:proyecto_id>/', ver_proyecto, name='ver_proyecto'),
    path('crear_proyecto/',crear_proyecto,name='crear_proyecto'),
    path('edit_user/', edit_user, name='edit_user'),
    path('Admin-Inicio/',Admin_Inicio,name='inicio_admin'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('inicio/',Inicio,name='inicio'),
    path('', RedirectView.as_view(url='/inicio/', permanent=True)),
    path('<str:username>/', perfil_usuario, name='ver_perfil'),
    path('completar-perfil/<str:username>/', completar_perfil, name='completar_perfil'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)