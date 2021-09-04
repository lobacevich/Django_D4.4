from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name.username

    def update_rating(self):
        postR = Post.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum']
        commR = Comment.objects.filter(user=self.name).aggregate(Sum('rating'))['rating__sum']
        commPostR = 0
        for post in Post.objects.filter(author=self):
            commPostR += Comment.objects.filter(post=post).aggregate(Sum('rating'))['rating__sum']

        self.rating = postR * 3 + commR + commPostR
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    postType = models.CharField(max_length=7, choices=(('news', 'новость'), ('article', 'статья')), default='article')
    dateCreated = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=31)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.author.name.username + '/' + self.title

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:123] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.post.title + '/' + self.user.username

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
