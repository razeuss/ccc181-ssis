import random
from faker import Faker
import mysql.connector

# Configure Faker
faker = Faker()

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="joshua",  # Replace with your MySQL password
    database="ssis"
)
cursor = conn.cursor()

# Fetch existing programs from the database
cursor.execute("SELECT code FROM program")
program_codes = [row[0] for row in cursor.fetchall()]

# Generate 200 students
students = []
generated_ids = set()  # Track unique student IDs

while len(students) < 200:
    year_level = random.randint(1, 5)  # Assume 1st to 5th year
    batch_year = 2024 - (5 - year_level)  # Calculate batch year based on year level
    unique_number = str(random.randint(0, 4999)).zfill(4)  # 4-digit number up to 5000, padded with zeros
    student_id = f"{batch_year}-{unique_number}"  # ID format: YYYY-XXXX

    if student_id in generated_ids:  # Skip duplicates
        continue

    generated_ids.add(student_id)  # Add to the set of used IDs
    firstname = faker.first_name()
    lastname = faker.last_name()
    program_code = random.choice(program_codes)
    gender = random.choice(["Male", "Female"])
    image_url = f"https://picsum.photos/seed/{student_id}/200/200"  # Random photo URL
    students.append((student_id, firstname, lastname, program_code, year_level, gender, image_url))

# Insert students into the database
query = """
    INSERT INTO student (id, firstname, lastname, program_code, year, gender, image_url)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(query, students)
conn.commit()

print(f"{len(students)} students inserted successfully.")

# Close the connection
cursor.close()
conn.close()
