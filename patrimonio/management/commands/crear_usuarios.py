from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from patrimonio.models import LugarPatrimonial

class Command(BaseCommand):
    help = 'Crea usuarios y asigna permisos'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creando usuarios y asignando permisos... ")

        #Grupo de gestores
        grupo_gestores, _ = Group.objects.get_or_create(name='Gestores de Patrimonio')

        #Permisos para el grupo de gestores
        content_type = ContentType.objects.get_for_model(LugarPatrimonial)
        permiso_add = Permission.objects.get(content_type=content_type, codename='add_lugarpatrimonial')
        permiso_change = Permission.objects.get(content_type=content_type, codename='change_lugarpatrimonial')

        grupo_gestores.permissions.set([permiso_add, permiso_change])

        #superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@patrimonio.cl', 'admin123')
            self.stdout.write("Usuario superuser 'admin' ya existía.")

        #Usuario gestor
        usuario_gestor, creado = User.objects.get_or_create(username='gestor', email='gestor@patrimonio.cl')
        usuario_gestor.set_password('gestor123')
        usuario_gestor.groups.set([grupo_gestores])
        usuario_gestor.save()
        self.stdout.write(self.style.SUCCESS("Usuario Gestor creado: gestor / gestor123 (Grupo: Gestores de Patrimonio)"))


        #Usuario lector (sin permisos de gestión)
        usuario_lector, creado = User.objects.get_or_create(username='lector', email='lector@patrimonio.cl')
        usuario_lector.set_password('lector123')
        usuario_lector.groups.clear()  # No pertenece a ningún grupo
        usuario_lector.save()
        self.stdout.write(self.style.SUCCESS("Usuario Lector creado: lector / lector123 (Sin permisos de gestión)"))