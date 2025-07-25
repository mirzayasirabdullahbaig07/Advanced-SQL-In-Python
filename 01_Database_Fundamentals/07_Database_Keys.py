# What are Database Keys?

# Keys in DBMS
# A key in a database is an attribute or a set of attributes that uniquely identifies a tuple (row) in a table.
# Keys ensure data integrity and consistency by enforcing uniqueness and establishing relationships between tables.

# -------------------------
# Types of Database Keys
# -------------------------

# 1. Super Key:
# A super key is a set of one or more columns (attributes) that can uniquely identify any row in a table.
# Example:
#   Table: Students (RollNo, Name, Email)
#   Super Keys: [RollNo], [Email], [RollNo + Email], etc.

# 2. Candidate Key:
# A candidate key is a minimal super key – meaning it has no redundant attributes.
# It’s the smallest possible combination of attributes that uniquely identifies rows.
# Example:
#   Table: Students (RollNo, Email)
#   Candidate Keys: [RollNo], [Email] (if both are unique)

# 3. Primary Key:
# A primary key is a chosen candidate key that uniquely identifies each row in a table.
# It cannot have NULL values and must be unique.
# Example:
#   Table: Students (RollNo, Name)
#   Primary Key: [RollNo]

# 4. Alternate Key:
# Alternate keys are candidate keys that are not selected as the primary key.
# Example:
#   Table: Students (RollNo, Email)
#   Primary Key: RollNo
#   Alternate Key: Email

# 5. Composite Key:
# A composite key is a primary key formed by combining two or more attributes.
# Used when a single attribute isn't enough to uniquely identify a row.
# Example:
#   Table: CourseRegistrations (StudentID, CourseID)
#   Composite Key: [StudentID + CourseID]

# 6. Surrogate Key:
# A surrogate key is an artificial or auto-generated key used to uniquely identify each row.
# It has no business meaning and is typically an auto-incremented ID.
# Example:
#   Table: Orders (OrderID, CustomerName, Date)
#   Surrogate Key: OrderID (auto-generated)

# 7. Foreign Key:
# A foreign key is a field in one table that refers to the primary key in another table.
# It creates a relationship between two tables.
# Example:
#   Table 1: Customers (CustomerID, Name)
#   Table 2: Orders (OrderID, CustomerID)
#   Foreign Key: Orders.CustomerID → Customers.CustomerID
