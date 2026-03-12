"""Create a class called Person with the following attributes: name, country, and date_of_birth."""

from datetime import datetime


class Person:
    """The Person class represents an individual with a name, country, and date of birth. 
    It provides methods to calculate the person's age and print their name and country."""

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        """Calculate and return the age of the person based on their date of birth."""
        today = datetime.today()
        birth_date = datetime.strptime(self.date_of_birth, "%d-%m-%Y")
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age

    def print_name(self):
        """Print the name of the person."""
        print(f"Name : {self.name}")

    def print_country(self):
        """Print the country of the person."""
        print(f"Country : {self.country}")


person1 = Person("Ahmed", "Egypt", "06-03-2002")
person1.print_name()
person1.print_country()
print(f"Age : {person1.calculate_age()}")
