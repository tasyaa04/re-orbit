class Activity():
    def __init__(self, activity_id, user_id, activity_name,):
        self.user_id = user_id
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.skill_level = 'beginner'
        self.count = 0
        self.total_count = 0

    def update_count(self):
        skill_levels = {'beginner': 10, 'intermediate': 15, 'advanced': 20, 'expert': 25}
        self.count += 1
        self.total_count += 1
        if self.count == skill_levels[self.skill_level]:
            self.count = 0
            self.upgrade_level()

    def upgrade_level(self):
        if self.skill_level == 'beginner':
            self.skill_level = 'intermediate'
        elif self.skill_level == 'intermediate':
            self.skill_level = 'advanced'


