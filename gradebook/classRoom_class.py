from student_class import Student


class ClassRoom:
    """Class that allows teachers to better track their students."""

    def __init__(self, name):
        """Initialize using parameters to set values for attributes."""
        self.name = name
        self.meeting_time = {}
        self.assignments_roster = []
        self.roster = {}
        self.numberOfStudents = len(self.roster)
        self.class_schedule()
        self.command()

    def command(self):
        """Create command function."""
        command = input("Type a command (as: add a student, rs: remove a student, aa: add an assignment, ra: remove an assignment, c: calculate average of each student’s grades, e: exit the %s class): " % (self.name))

        if command == "as":
            self.add_student_to_roster()
        elif command == "rs":
            self.remove_student()
        elif command == "aa":
            self.add_assignment()
        elif command == "ra":
            self.remove_assignment()
        elif command == "c":
            self.get_student_average()
        else:
            pass
        self.command()

    def class_schedule(self):
        """User creates class schedule."""
        days = []
        times = []
        add_day = True

        while add_day:
            weekday = input("What day is class: ")
            days.append(weekday)
            timing = input("What time does class start: ")
            times.append(timing)

            self.meeting_time[weekday] = timing

            add_more_days = input("Adding more days? [yes] or [no]\n")
            if add_more_days == "yes":
                add_day = True
            elif add_more_days == "no":
                add_day = False
            else:
                add_day = False
        print(self.meeting_time)

    def add_student_to_roster(self, name, on_time):
        """Create function that allows teachers to add students to the roster."""
        self.roster[name] = Student(name, on_time)
        print("%s has been added to %s class" % (name, self.name))

    def remove_student(self):
        """Remove student from roster."""
        student_name = input("Who do you want to remove from %s" % (self.name))

        if self.roster.get(student_name) is None:
            print("%s is not in %s class" % (student_name, self.name))
        else:
            self.roster.pop(student_name)

    def add_assignment(self, assignment):
        """Add assignment to array in ClassRoom class."""
        for student in self.roster:
            self.roster[student].grades[assignment] = int(input("%s's %s grade: " % (student, assignment)))

        if assignment not in self.assignments_roster:
            self.assignments_roster.append(assignment)

    def remove_assignment(self, assignment):
        """Remove assignment from assignment roster."""
        self.assignment.pop(assignment)

    def get_student_average(self, name):
        """Get average of student scores on assignments."""
        total = 0
        number_of_assignments = 0
        for item in self.roster[name].grades:
            total += self.roster[name].grades[item]
            number_of_assignments += 1
        average = round(total / number_of_assignments, 3)
        return average
