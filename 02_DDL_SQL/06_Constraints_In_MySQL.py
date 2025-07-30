# ----------------------------------------
# CONSTRAINTS IN MySQL
# ----------------------------------------

# Constraints in databases are **rules or conditions** that must be satisfied when inserting, 
# updating, or deleting data in a table.
# They are essential for enforcing data **integrity** and preventing inconsistencies or corruption.

# Common MySQL Constraints:

# 1. NOT NULL:
#    Ensures that a column cannot have NULL values.
#    Example: name VARCHAR(100) NOT NULL

# 2. UNIQUE:
#    Ensures that all values in a column are unique across rows.
#    Example: email VARCHAR(255) UNIQUE

# 3. PRIMARY KEY:
#    A combination of NOT NULL and UNIQUE.
#    Uniquely identifies each row in a table.
#    Example: id INT PRIMARY KEY

# 4. AUTO_INCREMENT:
#    Automatically generates a sequential number for new rows.
#    Typically used with PRIMARY KEY.
#    Example: id INT AUTO_INCREMENT PRIMARY KEY

# 5. CHECK:
#    Restricts the values that can be placed in a column using logical expressions.
#    Example: age INT CHECK (age >= 18)

# 6. DEFAULT:
#    Assigns a default value to a column when no value is provided.
#    Example: status VARCHAR(20) DEFAULT 'active'

# 7. FOREIGN KEY:
#    Links a column in one table to the PRIMARY KEY in another table.
#    Maintains referential integrity between related tables.

# Referential Actions (used with FOREIGN KEY):

# - RESTRICT:
#   Prevents the action (UPDATE/DELETE) if related data exists in the child table.

# - CASCADE:
#   Automatically updates or deletes related rows in the child table when the parent row changes.

# - SET NULL:
#   Sets the foreign key column to NULL in the child table if the referenced row is deleted/updated.

# - SET DEFAULT:
#   Sets the foreign key column to its DEFAULT value upon deletion/update of the referenced row.

# Summary:
# Constraints are vital for maintaining data integrity and ensuring that only valid, consistent,
# and meaningful data is stored in the database.
