from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
# Create your models here.

# model for courses
class Course(models.Model):
    name = models.CharField(max_length=12) # name of the class
    isClassActive = models.BooleanField() # is the currently active, not a previously taken class
    # string representation of course
    def __str__(self):
        return f'{self.name}'

# model for paper
class Paper(models.Model):
    title = models.CharField(max_length=200, blank=False) # title of the paper, required
    author = models.CharField(max_length=200, blank=True) # author of the paper, not required
    totalPages = models.IntegerField(default=1) # number of pages in the paper (set by user), defaults to 1
    readPages = models.IntegerField(default=0) # number of pages the user has read, defaults to 0
    url = models.CharField(max_length=200, blank=True) # url link of the paper, not required
    addDate = models.DateTimeField(auto_now_add=True, null=True) # time this paper was added by the user
    dueDate = models.DateTimeField(auto_now_add=False, null=True) # time this paper is due
    comments = models.TextField(blank=True) # user added comment about paper
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="paper") # the course this paper belongs to

    # string representation of paper
    def __str__(self):
        return f'{self.title} by {self.author}, {self.totalPages} pages due {self.addDate}'

    # a paper is larger than another if it has more pages, the rest of the logic follows
    def __gt__(self, other):
        return self.totalPages > other.totalPages
    def __lt__(self, other):
        return self.totalPages < other.totalPages
    def __ge__(self, other):
        return self.totalPages >= other.totalPages
    def __le__(self, other):
        return self.totalPages <= other.totalPages
    

## extended version of user, custom user class
class User(AbstractUser):
    courses = models.ManyToManyField(Course, related_name="user") # courses the user is taking
    papers = models.ManyToManyField(Paper, related_name="user") # the papers the user has added
