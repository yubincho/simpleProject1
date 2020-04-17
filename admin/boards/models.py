from django.db import models

from django.urls import reverse

# Create your models here.


class Board(models.Model):

    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    created_date = models.DateField(null=True, blank=True)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        # return "/%s/" % self.id
        return reverse("board_detail", args=[str(self.id)])

    @property
    def update_count(self):
        self.hit = self.hit + 1
        self.save()
