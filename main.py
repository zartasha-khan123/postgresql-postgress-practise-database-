import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DATABASE_URL ko environment se read kar rahe hain
DATABASE_URL = os.getenv("DATABASE_URL_UNPOOLED")

# SQLAlchemy engine create kar rahe hain
engine = create_engine(DATABASE_URL)

user_list=[]


def main():
    with engine.connect() as connection:
        connection.execute(text(
            """
            CREATE TABLE IF NOT EXISTS postsql_user_table (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
            """
        ))
        connection.commit()
        
        # Optional: Sample data insert karne ke liye (commented by default)
        connection.execute(text("""
            INSERT INTO postsql_user_table 
            (name, email)
            VALUES 
            ('zartasha','zara@gmail.com'),
            ('Ahmed','ahmed@gmail.com'),
            ('Ali','ali@gmail.com'),
            ('alexbhai','alexbhai@gmail.com');
        """))
        connection.commit()
        
        
        result = connection.execute(text("SELECT * FROM postsql_user_table;")).mappings()
        
        print("Users in database:")
        
        for row in result:
            user_list.append(dict(row))
            
        print("✅",user_list)  # Row ko dictionary mein convert karke print kar rahe hain
        
        # Script ko run karne ke liye
if __name__ == "__main__":
    main()