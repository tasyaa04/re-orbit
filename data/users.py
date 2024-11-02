import datetime


class User():
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.streak = 0
        self.data = {}  # dictionary to store data for the recommendation algorithm
        self.skills = []
        self.last_entry = datetime.date.today()

    def set_data(self, data):
        self.data = data

    def update_streak(self):
        self.streak += 1

    def update_skills(self, activity):
        entry = datetime.date.today()
        if (entry - self.last_entry).days == datetime.timedelta(days=1):
            self.update_streak()
        activity.update_count()
