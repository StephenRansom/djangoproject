# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Author Name")
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " : " + self.email

  #  def get_absolute_url(self):
  #      return reverse('post_by_author', args=[self.name])

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts_by_category', args=[self.slug])

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts_by_tag', args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Slug will be generated automatically from post title, and will be displayed when post is saved")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): #also allows admin view to populate read-only field "slug" 
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
