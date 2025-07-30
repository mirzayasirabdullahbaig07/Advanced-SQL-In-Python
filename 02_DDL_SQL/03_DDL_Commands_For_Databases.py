# Why do we use DDL?
# DDL stands for **Data Definition Language**.
# It is used to define and modify the **structure of database objects** such as:
# - Databases
# - Tables
# - Indexes
# - Views
#
# With DDL commands, you can:
# - Create new databases and tables
# - Modify existing structures (add/remove columns)
# - Delete entire databases or tables
#
# DDL commands are auto-committed, which means the changes are saved immediately and cannot be rolled back.

# ------------------------------------------
# How to Create a New Database?

# Basic Command:
# CREATE DATABASE yasirinsights;

# - `CREATE DATABASE` is the SQL keyword (always written in UPPERCASE).
# - `yasirinsights` is the name of your database (lowercase is recommended for naming).
# - A semicolon `;` ends the SQL statement.

# Best Practice:
# - Use lowercase for database names (e.g., yasirinsights)
# - Use uppercase for SQL keywords (e.g., CREATE, DROP)

# Conditional Creation:
# CREATE DATABASE IF NOT EXISTS yasirinsights;

# This command creates the database only if it doesn’t already exist.
# Prevents errors in case the database is already present.

# ------------------------------------------
# How to Delete a Database?

# Basic Command:
# DROP DATABASE yasirinsights;

# - This will permanently delete the database named `yasirinsights` along with all its tables and data.

# Conditional Deletion:
# DROP DATABASE IF EXISTS yasirinsights;

# This will delete the database only if it exists — prevents errors when dropping a non-existent DB.

# Note:
# - Use DROP with caution. Once a database is dropped, all its data is lost permanently.
# - Always double-check the database name before dropping.
