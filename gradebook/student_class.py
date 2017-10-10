
class Student():
    """Create class that allows teachers to create students objects."""

    def __init__(self, name, on_time):
        """Initialize using parameters to set values for attribute."""
        self.name = name
        self.grades = {}
        self.GPA = 0
        self.on_time = True
        self.number_of_assignments = 0
        self.excused_absences = 0
