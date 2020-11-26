from django.db import models


class POST(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        self.title