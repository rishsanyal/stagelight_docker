from topics.models import Topic, Competitions
from .import_topics import RedditTopicsParser


class CompetitionUtils:
    def __init__(self, total_topics=3, sort_by_time='all', theme='TBD'):
        self.total_topics = total_topics
        self.sort_by_time = sort_by_time
        self.theme = theme

    def run(self):
        self.create_competition()

    def create_competition(self):
        parser = RedditTopicsParser()

        all_topics = parser.run()
        new_competition = \
            Competitions.objects.create(
                theme=self.theme,
                is_open=True
            )

        for topic in all_topics:
            new_competition.competition_topics.add(topic)

        new_competition.save()
        return new_competition
