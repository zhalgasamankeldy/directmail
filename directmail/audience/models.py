from django.db import models

from treebeard.mp_tree import MP_Node


class Audience(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return self.name
