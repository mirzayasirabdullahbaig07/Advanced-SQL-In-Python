# What is SQL?
# SQL stands for **Structured Query Language**.
# It is a standard programming language used to **manage and manipulate data** in relational database systems.
# With SQL, you can perform operations such as:
# - Inserting new data
# - Updating existing records
# - Retrieving (querying) data
# - Deleting data from the database
#
# SQL is widely used in applications, websites, and business systems for **data storage, processing, and analytics**.
# In simple terms, **SQL is how you talk to and control databases**.

# TYPES OF SQL COMMANDS
# SQL commands are categorized into 4 major types:
# 1. DDL – Data Definition Language
# 2. DML – Data Manipulation Language
# 3. DCL – Data Control Language
# 4. TCL – Transaction Control Language

# ------------------------------------------
# 1. DDL – Data Definition Language
# DDL commands are used to define and modify the **structure of database objects** such as tables, schemas, and indexes.
# These changes are permanent and auto-committed.

# Common DDL Commands:
# - CREATE   : Creates a new table, database, view, or other database object.
# - ALTER    : Modifies the structure of an existing table (add/remove columns, change data type, etc).
# - DROP     : Deletes an entire table, database, or view.
# - TRUNCATE : Removes all rows from a table, but keeps its structure.

# ------------------------------------------
# 2. DML – Data Manipulation Language
# DML commands are used for **manipulating the data** stored in the database.
# These operations can be rolled back (i.e., not auto-committed).

# Common DML Commands:
# - INSERT   : Adds new records (rows) to a table.
# - UPDATE   : Modifies existing records in a table.
# - DELETE   : Removes records from a table.
# - SELECT   : Retrieves data from one or more tables (read-only).

# ------------------------------------------
# 3. DCL – Data Control Language
# DCL commands are used to control **access to data** and database permissions.
# These are important for **security and authorization** in multi-user environments.

# Common DCL Commands:
# - GRANT    : Gives users access privileges to the database.
# - REVOKE   : Withdraws access privileges from users.

# ------------------------------------------
# 4. TCL – Transaction Control Language
# TCL commands are used to manage **transactions** in the database, ensuring data integrity.
# A transaction is a sequence of operations performed as a single logical unit of work.

# Common TCL Commands:
# - COMMIT     : Saves all changes made during the transaction permanently in the database.
# - ROLLBACK   : Undoes changes made during the current transaction.
# - SAVEPOINT  : Sets a point within a transaction to which you can later roll back.

# Summary:
# - Use DDL to define structure
# - Use DML to manage data
# - Use DCL to manage permissions
# - Use TCL to manage transactions and ensure consistency

# Let me know if you'd like to continue with DDL commands examples next!
