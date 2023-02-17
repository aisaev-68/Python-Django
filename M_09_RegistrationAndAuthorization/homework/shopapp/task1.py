from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.db import models

from shopapp.models import Product

author_group, created = Group.objects.get_or_create(name="Author")


content_type = ContentType.objects.get_for_model(Product)
post_permission = Permission.objects.filter(content_type=content_type)
print([perm.codename for perm in post_permission])


for perm in post_permission:
    if perm.codename == "delete_post":
        author_group.permissions.add(perm)

    elif perm.codename == "change_post":
        author_group.permissions.add(perm)

    else:
        author_group.permissions.add(perm)


user = User.objects.get(username="test")
user.groups.add(author_group)  # Add the user to the Author group
