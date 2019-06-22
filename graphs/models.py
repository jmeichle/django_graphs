from django.db import models

# Create your models here.

class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # A timestamp reprensenting when this object was last updated.
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']


class Graph(TimestampedModel):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date published')

class Node(TimestampedModel):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

class Edge(TimestampedModel):
    src_node = models.ForeignKey(Graph,
        on_delete=models.PROTECT,
        related_name='%(class)s_src_node'
    )
    dst_node = models.ForeignKey(Graph,
        on_delete=models.PROTECT,
        related_name='%(class)s_dst_node'
    )

