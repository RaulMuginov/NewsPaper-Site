from django.db import models

# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=64)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

class CartModel(models.Model):
    pr_name = models.CharField(max_length=256)
    pr_total_price = models.FloatField()
    pr_total_count = models.IntegerField()
    pr_created_at = models.DateTimeField()

    def __str__(self):
        return self.pr_name

class News(models.Model):
    news_head = models.CharField(max_length=256)
    news_des = models.TextField(blank=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_head