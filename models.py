from django.contrib.auth.models import User

from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User,
        on_delete = models.CASCADE,
        related_name = 'author')
    rating_author = models.IntegerField(default=0)


    def update_rating(self):
        p = sum(post.rating_news_or_article for post in self.post.all())*3
        c =  sum(comment.rating_comment for comment in self.user.user_comments.all())
        pc = 0
        for post in self.post.all():
            pc += sum(comment.rating_comment for comment in post.comments.all())
        self.rating_author = p + c + pc
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length = 100,unique=True)


class Post(models.Model):
    TYPE_CHOICES = [
        ('news', 'Новость'),
        ('article', 'Статья'),
    ]
    author = models.ForeignKey(Author,
        on_delete = models.CASCADE,
        related_name ='post'
    )
    post_type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        default = 'news',
        verbose_name = 'type'
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    rating_news_or_article = models.IntegerField( default = 0)
    categories = models.ManyToManyField(
        Category,
        through='PostCategory',
        related_name='posts'
    )

    def like(self):
        self.rating_news_or_article += 1
        self.save()

    def dislike(self):
        self.rating_news_or_article -= 1
        self.save()

    def preview(self):
        if len(self.content) > 124:
            return self.content[:124] + '...'
        return self.content


class PostCategory(models.Model):
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE,
        related_name='post_categories'
    )
    category = models.ForeignKey(Category,
        on_delete=models.CASCADE,
        related_name='category_posts'
    )


class Comment(models.Model):
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='user_comments')
    text = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default = 0)

    def like(self):
        self.rating_comment += 1
        self.save()
    def dislike(self):
        self.rating_comment -= 1
        self.save()




















