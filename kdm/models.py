from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.models import permalink
from django.db.models.signals import pre_save
from django.utils.text import slugify
#from django.core.urlresolvers import reverse


# Create your models here.
# class BlogManager(models.Manager):
#     def active(self, *args, **kwargs):
#         return super(BlogManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3.3 is __str__
        return self.email

class User(models.Model):
    full_name = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.full_name

def upload_location(instance, filename):
        return "%s/%s" %(instance.id, filename)





class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    # draft = models.BooleanField(default=False)
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    image = models.FileField(upload_to=upload_location, blank=True,null=True,)
    posted = models.DateTimeField(db_index=True, auto_now_add=True, auto_now=False)

    # objects = BlogManager()

    def __unicode__(self):
        return '%s' % self.title

    
    # def get_absolute_url(self):
    #     return "/blogs/view/%s/" % self.id
    def get_absolute_url(self):
        return reverse("posts:view_blog_post", kwargs={"id": self.id})


    class Meta:
        ordering = ["-posted"]


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.FileField(upload_to=upload_location, blank=True,null=True,)
    publish = models.DateTimeField(db_index=True, auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return "/work/#projects" 




def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_blog_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_blog_receiver, sender=Blog)
