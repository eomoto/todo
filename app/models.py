from django.db import models

class Item(models.Model):
  item_text = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)

  def __str__(self):
    return self.item_text
