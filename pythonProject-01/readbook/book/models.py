from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:story_category', args=[self.slug])

class Story(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="stories")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:story_detail', args=[self.id])
