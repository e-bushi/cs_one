from classRoom_class import ClassRoom
from student_class import Student


class School:
    """School class use to create a classes."""

    def __init__(self, name, classRoster={}, classArray=[]):
        """Create school objects."""
        self.name = name
        self.classRoster = classRoster
        self.classArray = classArray

    def create_class(self):
        """Use to make creating classes intuitive."""
        if self.classRoster == {}:
            create = input("Would you like to create a class? [yes] or [no]: ")
        elif self.classRoster != {}:
            create = input("Would you like to create another class? [yes] or [no]: ")

        if create == "yes":
            name_of_class = input("What is the name of your class: ")
            self.classArray.append(name_of_class)
            self.classRoster[name_of_class] = ClassRoom(name_of_class)
            self.create_class()
        else:
            access = input("Would you like to access an existing class? [yes] or [no]: ")
            if access == "yes":
                existing_class = input("what class would you like to access: ")

                if existing_class not in self.classRoster:
                    print("Sorry that class doesn't exist")
                    self.create_class()

                self.classRoster[existing_class].command()
                self.create_class()
