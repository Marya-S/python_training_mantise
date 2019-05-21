from sys import maxsize


class Project:
    def __init__(self, projectname, description=None, id=None):
        self.name = projectname
        self.description = description
        self.id = id

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
