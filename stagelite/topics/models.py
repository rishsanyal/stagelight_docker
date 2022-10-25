import datetime
from django.db import models

from stage.models import StageUser

DEFAULT_COMPETITION_END_TIME = 1

def get_new_vote():
    print('there')
    return Votes.objects.create().id

class BaseTopicModel(models.Model):

    last_updated = models.DateField(auto_now=True)
    creation_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True

class Votes(BaseTopicModel):
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def increment(self):
        self.upvote += 1
        self.save()

    def decrement(self):
        self.downvote -= 1
        self.save()

    def get_total_votes(self):
        return self.upvote + self.downvote

    @property
    def is_positive(self):
        return self.get_total_votes() > 0


class Topic(BaseTopicModel):
    title = models.CharField(max_length=1024,help_text='String Title of topic', unique=True)
    votes = models.ForeignKey(Votes, on_delete=models.DO_NOTHING, related_name='topic_votes')
    # genre = FUTURE REQUEST

    def save(self, *args, **kwargs):
        self.votes = Votes.objects.create()
        super(Topic, self).save(*args, **kwargs)


class UserSubmission(BaseTopicModel):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(StageUser, on_delete=models.DO_NOTHING)
    votes = models.ForeignKey(Votes, on_delete=models.DO_NOTHING, related_name='user_submission_votes')
    submission_entry = models.TextField(help_text='Submission text')
    # awards = FUTURE REQUEST
    # COMMENTS = FUTURE REQUEST


    def save(self, *args, **kwargs):
        # Hack to create votes, not sure on how to create a new object of votes
        if not self.votes:
            self.votes = Votes.objects.create()
        super(UserSubmission, self).save(*args, **kwargs)

class Competitions(BaseTopicModel):
    """
        For topic selection comeptitions and topic submission competitions.
    """
    #Shouldn't be mandatory
    submissions = models.ForeignKey(UserSubmission, on_delete=models.CASCADE, null=True)

    #Needs to be default
    votes = models.ForeignKey(Votes, on_delete=models.DO_NOTHING, related_name='competition_votes')
    winner_topic = models.OneToOneField(Topic, on_delete=models.CASCADE, null=True)
    winner_user = models.OneToOneField(StageUser, on_delete=models.DO_NOTHING, null=True)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(default=datetime.datetime.now() + datetime.timedelta(weeks=DEFAULT_COMPETITION_END_TIME))
    theme = models.CharField(max_length=128, blank=True)
    competition_topics = models.ManyToManyField(Topic, related_name='competition_topics', null=True)
    is_open = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.votes = Votes.objects.create()
        super(Competitions, self).save(*args, **kwargs)
