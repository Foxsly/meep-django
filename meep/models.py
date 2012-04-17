from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __unicode__(self):
        return self.username

class Topic(models.Model):
    title = models.TextField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Message(models.Model):
    title = models.TextField()
    post = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User)
    msg_topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.post
