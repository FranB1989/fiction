from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        groups_permissions = {
            'Administrador': [
                'add_blogentry',
                'change_blogentry',
                'delete_blogentry',
                'view_blogentry',
            ],
            'Editor': [
                'add_blogentry',
                'change_blogentry',
                'delete_blogentry',
                'view_blogentry',
            ],
            'Blogger': [
                'add_blogentry',
                'change_blogentry',
                'delete_blogentry',
                'view_blogentry',
            ],
            'Regular': [
                'view_blogentry',
            ],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            self.stdout.write(f'Grupo "{group_name}" {"creado" if created else "ya existe."}')

            self.assign_permissions(group, permissions, 'blog', 'blogentry')
            if group_name == 'Administrador':
                self.assign_permissions(group, ['add_user', 'change_user', 'delete_user', 'view_user'], 'users', 'user')

        self.stdout.write(self.style.SUCCESS('Grupos y permisos creados correctamente.'))

    def assign_permissions(self, group, permissions, app_label, model_name):
        for perm in permissions:
            try:
                permission = Permission.objects.get(
                    codename=perm,
                    content_type=ContentType.objects.get(app_label=app_label, model=model_name)
                )
                group.permissions.add(permission)
                self.stdout.write(f'Permiso "{perm}" asignado al grupo "{group.name}".')
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Permiso "{perm}" no encontrado.'))
            except ContentType.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'ContentType para {app_label}.{model_name} no encontrado.'))

