class Project:
    def __init__(self, projectname, description=None):
        self.name = projectname
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description
