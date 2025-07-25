# What is Cardinality in a Dataset?

# Cardinality in dataset relationships refers to the number of occurrences of an entity 
# in a relationship with another entity.
# It defines how many instances of one entity can be associated with instances of another entity.

# -------------------------
# Types of Relationships
# -------------------------

# 1. One-to-One (1:1) Relationship
#  Meaning: Each record in Table A is related to one and only one record in Table B, and vice versa.
#  Storage: Can be stored in a single table or two separate tables using a foreign key.

#  Example:
#   Table 1: Person (PersonID, Name)
#   Table 2: Passport (PassportID, PersonID)
#   - Each person has one passport.
#   - Each passport is assigned to one person.

# 2. One-to-Many (1:N) Relationship
#  Meaning: A single record in Table A can relate to many records in Table B,
#            but each record in Table B relates to only one record in Table A.
#  Storage: Requires two tables with a foreign key in the "many" side.

#  Example:
#   Table 1: Department (DeptID, DeptName)
#   Table 2: Employee (EmpID, Name, DeptID)
#   - One department can have many employees.
#   - Each employee belongs to one department.

# 3. Many-to-Many (M:N) Relationship
#  Meaning: Many records in Table A relate to many records in Table B.
#  Storage: Requires three tables – two main tables and one junction (association) table.

#  Example:
#   Table 1: Student (StudentID, Name)
#   Table 2: Course (CourseID, Title)
#   Table 3: StudentCourse (StudentID, CourseID)  ← Junction table
#   - One student can enroll in many courses.
#   - One course can have many students.
