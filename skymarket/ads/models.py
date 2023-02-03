from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_image/', null=True)

    class Meta:
        ordering = ["created_at"]

    @property
    def phone(self):
        return self.author.phone

    @property
    def author_first_name(self):
        return self.author.first_name

    @property
    def author_last_name(self):
        return self.author.last_name


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    @property
    def author_first_name(self):
        return self.author.first_name

    @property
    def author_last_name(self):
        return self.author.last_name

    @property
    def author_image(self):
        return self.author.image
