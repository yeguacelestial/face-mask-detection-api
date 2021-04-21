from django.db import models

# Create your models here.
class MaskDetector(models.Model):
    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')

    def __str__(self):
        return self.image

    def get_absolute_url(self):
        return reverse("MaskDetector_detail", kwargs={"pk": self.pk})
