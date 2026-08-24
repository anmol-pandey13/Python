# Lists and Dictionaries

skills = ["Python", "Git", "Pandas", "NumPy"]

print("My skills:")
for skill in skills:
    print("-", skill)

# Add a new skill
skills.append("Streamlit")

print("\nUpdated skills:")
print(skills)

student = {
    "name": "Anmol",
    "semester": 3,
    "project": "Fake Weather Sensor"
}

print("\nStudent Information:")
print("Name:", student["name"])
print("Semester:", student["semester"])
print("Project:", student["project"])