from typing import NewType, Tuple

Section = NewType("Section", str)
StudentNumber = NewType("StudentNumber", str)
LastName = NewType("LastName", str)
SecondLastName = NewType("SecondLastName", str)
FirstName = NewType("FirstName", str)
Email = NewType("Email", str)
RUT = NewType("RUT", str)
Curriculum = NewType("Curriculum", str)
Student = NewType(
    "Student",
    Tuple[Section, StudentNumber, LastName, SecondLastName, FirstName, Email, RUT, Curriculum],
)
