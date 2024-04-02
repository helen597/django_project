from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from catalog.models import Product

content_type = ContentType.objects.get_for_model(Product)
catalog_permissions = [
    'view_product',
    'add_product',
    'change_product',
    'delete_product',
    'set_published',
    'change_description',
    'change_category'
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        moderators_group = Group.objects.create(name='catalog_moderators')
        for p in catalog_permissions:
            perm = Permission.objects.get(codename=p, content_type=content_type)
            moderators_group.permissions.add(perm)
        moderators_group.save()
