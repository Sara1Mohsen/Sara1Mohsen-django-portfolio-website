from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
# Create your models here.
class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField( null=True, blank=True , upload_to='images/' , default='default.png')
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(tag, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline
    

    def save(self, *args, **kwargs):
        if not self.slug:
            has_slug = Post.objects.filter(slug=slugify(self.headline)).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs) 