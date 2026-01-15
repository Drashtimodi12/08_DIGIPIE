from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} | {self.age} | {self.email} | {self.contact} | {self.created_at}"

    
class UserLoginActivity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="activities")
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    total_seconds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} | {self.login_time} | {self.logout_time} | {self.total_seconds}"