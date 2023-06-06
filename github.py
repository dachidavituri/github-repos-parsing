class Github:
    def __init__(self, name, access_level, language, stars, description, update_date):
        self.name = name
        self.access_level = access_level
        self.language = language
        self.stars = stars
        self.description = description
        self.update_date = update_date

    def __str__(self):
        return f"name: {self.name}, access_level: {self.access_level}, language: {self.language}, " \
               f"stars: {self.stars}, description: {self.description}, update_date: {self.update_date}"