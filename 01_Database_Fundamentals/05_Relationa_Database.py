# ================================
# Relational Database (SQL)
# ================================

# A relational database, also known as an SQL database, uses a relational model 
# to organize data into tables consisting of rows and columns.
# It is ideal for structured data with well-defined relationships.

# =====================================
# Key Terminologies in Relational Databases
# =====================================

# - Table → Also known as a "Relation" in SQL. It stores data in a structured format.
# - Column → Also called "Attribute" or "Field". Represents a data category.
# - Row → Also known as a "Tuple". Represents a single record in the table.
# - Cardinality → The number of rows (tuples) in a table.
# - Degree → The number of columns (attributes) in a table.
# - NULL → Represents an empty or unknown value in a cell.
# - Domain → The set or type of valid values that an attribute (column) can hold.
#   Example: A "DateOfBirth" column will have a domain of DATE type.

# =====================================
# Example:
# =====================================
# Consider a "Students" table:
#
# +------------+----------+-----------+
# | StudentID  | Name     | Age       |
# +------------+----------+-----------+
# | 101        | Alice    | 20        |
# | 102        | Bob      | NULL      |
# +------------+----------+-----------+
#
# - Table Name: Students (Relation)
# - Attributes: StudentID, Name, Age
# - Tuples: Each row is a tuple
# - Cardinality: 2 (2 rows)
# - Degree: 3 (3 columns)
# - NULL: Missing value in Age for
