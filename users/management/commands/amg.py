from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from catalog.models import Product

content_type = ContentType.objects.get_for_model(Product)
catalog_permissions = [
    'Catalog.view_product',
    'Catalog.add_product',
    'Catalog.change_product',
    'Catalog.delete_product',
    'Catalog.set_published',
    'Catalog.change_description',
    'Catalog.change_category'
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        moderators_group = Group.objects.create('catalog_moderators')
        for perm in catalog_permissions:
            moderators_group.permissions.add(perm)
        moderators_group.save()
