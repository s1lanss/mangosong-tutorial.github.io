from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=100)
    telegram_url = models.URLField(max_length=200, blank=True, null=True)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username

class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.account.username}"
