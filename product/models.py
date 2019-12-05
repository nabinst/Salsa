from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)

    

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    product_name = models.ForeignKey(Product,  related_name='comments', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
         return 'Comment {} by {}'.format(self.body, self.name)
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    
    @property
    def comment_count(self):
        return Comment.objects.filter(product_name=self).count()
