# ddl_commands.py

"""
DDL (Data Definition Language) Commands for SQL Tables
These commands define the structure of the database schema.
"""

# 1. CREATE TABLE
create_table_query = """
CREATE TABLE users (
    user_id INTEGER,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);
"""

# 2. TRUNCATE TABLE
truncate_table_query = """
TRUNCATE TABLE users;
"""

# 3. DROP TABLE
drop_table_query = """
DROP TABLE users;
"""

