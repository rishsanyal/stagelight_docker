import praw
from topics.models import Topic

REDDIT = praw.Reddit(
    client_id='54W7YL3N3gdwbZpf_BoXeA',
    client_secret='ZHU8F2vHEjQZa40G8hfZR2fBbq2WaA',
    user_agent='mac:com.example.myredditapp:v1.2.3 (by /u/flakyfish)',
    username='school_stagelite',
    password='USFCA1234'
)

PROMPT_FLAIR = "[WP]"


# time_filter must be one of: day, year, month, all, week, hour
# WE'RE GETTING THE SAME 3 TOPICS NIBBA, NEED TO CHECK EXISTING TOPICS TO MAKE SURE THEY'RE UNIQUE

class RedditTopicsParser:
    def __init__(
        self,
        topic_limit=3,
        subreddit='WritingPrompts',
        sort_by_time='all',
        reddit_instance=REDDIT):

        self.reddit_instance = reddit_instance
        self.sort_by_time = sort_by_time
        self.subreddit_to_parse = subreddit
        self.topic_limit = topic_limit

    def run(self):
        all_topics = self.parse_and_populate_topics()
        return all_topics

    def parse_and_populate_topics(self):

        all_topics = [i for i in self.reddit_instance.subreddit(self.subreddit_to_parse).top(self.sort_by_time, limit=self.topic_limit)]
        for topic_number, topic in enumerate(all_topics):
            topic_title = topic.title.split(PROMPT_FLAIR)[1].strip()
            new_topic = Topic.objects.create(title=topic_title)
            all_topics[topic_number] = new_topic

        return all_topics