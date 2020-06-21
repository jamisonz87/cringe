from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    thread_type = models.CharField(max_length=10, default='Question')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_latest_date(self):
        if self.reply_set.count() > 0:
            return self.reply_set.latest('date_created').date_created

        return self.date_created

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(null=False, default='')
    date_created = models.DateTimeField(auto_now_add=True)