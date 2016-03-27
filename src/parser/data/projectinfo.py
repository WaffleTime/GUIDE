
class ProjectInfo(object):
    def __init__(self):
        # The name of the project.
        self.name = ""

        # Maps strings to strings.
        # This contains information about the project.
        # "root_dir" is a required key that must be included for each project.
        self.info = {}