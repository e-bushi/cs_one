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
        command = input("What would you like to do? (as: add a student, rs: remove a student, aa: add an assignment, ra: remove an assignment, c: calculate average of each student’s grades, e: exit the %s class): " % (self.name))

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
        elif command == "e":
            print("\n%s : %s \nAssignments: %s\nStudents: %s\n" % (self.name, self.meeting_time, self.assignments_roster, self.roster))
            return
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

            add_more_days = input("Adding more days? [yes] or [no:] ")
            if add_more_days == "yes":
                add_day = True
            elif add_more_days == "no":
                add_day = False
            else:
                add_day = False
        print("\n%s Class\nMeeting time[s]: %s\n" % (self.name, self.meeting_time))

    def add_student_to_roster(self):
        """Create function that allows teachers to add students to the roster."""
        student_name_id = input("What is the student's name?: ")
        is_on_time = input("Did this student arrive in class on time? [yes] or [no]: ")

        if is_on_time == "yes":
            on_time = True
        else:
            on_time = False

        self.roster[student_name_id] = Student(student_name_id, on_time)
        print("%s has been added to %s class. \n" % (student_name_id, self.name))

    def remove_student(self):
        """Remove student from roster."""
        student_name = input("Who do you want to remove from %s: " % (self.name))

        if self.roster.get(student_name) is None:
            print("%s is not in %s class" % (student_name, self.name))
        else:
            print("\n%s has been removed from %s class.\n" % (student_name, self.name))
            self.roster.pop(student_name)

    def add_assignment(self):
        """Add assignment to array in ClassRoom class."""
        assignment = input("What assignment would you like to add?: ")
        for student in self.roster:
            self.roster[student].grades[assignment] = int(input("%s's %s grade: " % (student, assignment)))

        if assignment not in self.assignments_roster:
            self.assignments_roster.append(assignment)

    def remove_assignment(self):
        """Remove assignment from assignment roster."""
        assignment = input("\nWhat assignment would you like to remove from %s class" % (self.name))

        if assignment in self.assignments_roster:
            self.assignment.pop(assignment)
            print("%s has been removed\n" % (assignment))

    def get_student_average(self):
        """Get average of student scores on assignments."""

        name = input("Whose average would you like to get?: ")

        if name in self.roster:

            if len(self.assignments_roster) > len(self.roster[name].grades):
                self.update_averages(name)
            total = 0
            number_of_assignments = 0
            for item in self.roster[name].grades:
                total += self.roster[name].grades[item]
                number_of_assignments += 1
            average = round(total / number_of_assignments, 3)
            self.roster[name].GPA = average
            print("%s's average in the class is %i" % (name, average))
        else:
            print("%s is not this %s class" % name, self.name)

    def update_averages(self, name):
        """Update average of all students in class."""
        for assignment in self.assignments_roster:
            if assignment not in self.roster[name].grades.keys():
                self.roster[name].grades[assignment] = int(input("%s's %s grade: " % (name, assignment)))
