"""Task 2: Inheritance and Polymorphism
In this task, you will create a simple class hierarchy
to demonstrate inheritance and polymorphism.
"""

import re
from oop_task1 import Person


class Student(Person):
    """The Student class inherits from the Person class
    and adds additional attributes for phone and track.
    """

    def __init__(self, name, country, date_of_birth, phone, track):
        """Initialize the Student object with name, country,
        date of birth, phone number, and track."""
        super().__init__(name, country, date_of_birth)
        self.phone = phone
        self.track = track

    @property
    def phone(self):
        """Return the phone number of the student."""
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Validate the phone number to ensure
        it is 11 digits and starts with specific patterns."""
        if re.match(r"^01(0|1|2|5)\d{8}$", phone):
            self._phone = phone
        else:
            raise ValueError("Phone number must be 11 digits.")

    def print_track(self):
        """Print the track of the student."""
        print(f"Track : {self.track}")

    def print_name(self):
        """Print the name of the student."""
        print(f"Student Name : {self.name}")


class Teacher(Person):
    """The Teacher class inherits from the Person class and
    adds additional attributes for salary and subject.
    """

    def __init__(self, name, country, date_of_birth, subject):
        """Initialize the Teacher object with name, country,
        date of birth, salary, and subject."""
        super().__init__(name, country, date_of_birth)
        self.subject = subject

    def print_subject(self):
        """Print the subject taught by the teacher."""
        print(f"Subject : {self.subject}")

    def print_name(self):
        """Print the name of the teacher."""
        print(f"Teacher Name : {self.name}")


def print_name(human):
    """Print the name of the human, whether it is a student or a teacher."""
    human.print_name()


person1 = Person("Salem", "Egypt", "01-02-1998")
student1 = Student("Ahmed", "Egypt", "06-03-2002", "01005162237", "Python")
teacher1 = Teacher("Mohamed", "Egypt", "08-08-1949", "Mathematics")

print_name(student1)
print_name(teacher1)
