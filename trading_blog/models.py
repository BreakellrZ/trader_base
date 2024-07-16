from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Status if post is published or in the draft.
STATUS = ((0, "Draft"), (1, "Published"))

# Currency Watchlist
WATCHLIST = (
    ('eur/usd', 'EUR/USD'),
    ('gbp/usd', 'GBP/USD'),
    ('usd/cad', 'USD/CAD'),
    ('eur/gbp', 'EUR/GBP'),
    ('treasuries', 'TREASURIES'),
    ('bond yields', 'BOND YIELDS'),
    ('s&p500', 'S&P500'),
    ('nasdaq100', 'NASDAQ100'),
    ('dxy', 'DXY'),
)

# Type of news events
NEWS_EVENTS = (
    ("None", "None"),
    ("High Impact News", "H"),
    ("Medium Impact News", "M"),
    ("Low Impact News", "L"),
)


# Create your models here.
# Journal Model
class Journal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trading_blog_posts"
    )
    content = models.TextField()
    date = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    watchlist = models.CharField(
        max_length=50, choices=WATCHLIST, default="dxy")
    news_events = models.CharField(choices=NEWS_EVENTS, default="None")
    news = models.CharField(max_length=50, blank=True)
    chart_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return (f"This is a  {self.title} post which includes -\n"
                f"{self.watchlist} & {self.news_events}"
                )


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Journal, on_delete=models.CASCADE, related_name="journal_comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return (f"This comment is from the {self.post} \n"
                f"post - - The Author is {self.author}")


