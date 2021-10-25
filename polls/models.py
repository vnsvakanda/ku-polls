"""This is models files that be a template for our database."""

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """This is class for Question template."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('ending date for voting')

    def was_published_recently(self):
        """Check that question is published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def is_published(self):
        """Check that question is published."""
        now = timezone.now()
        if (now >= self.pub_date):
            return True
        return False

    def can_vote(self):
        """Check that if question in are in time that can vote."""
        now = timezone.now()
        if (now <= self.end_date and self.is_published()):
            return True
        return False

    def __str__(self):
        """Display the question text of print function."""
        return self.question_text


class Choice(models.Model):
    """This is class for Choice template."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        """Display the choice text of print function."""
        return self.choice_text

    # we want to be able to  write 'choice.votes' in our views
    # and templates to get the number of votes for a Choice.
    # We want the existing code to still work.
    @property
    def votes(self) -> int:
        count = Vote.objects.filter(choice=self).count()
        return count


class Vote(models.Model):
    # I like to explicitly specify the id
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote by {self.user.name} for {self.choice.choice_text}"
