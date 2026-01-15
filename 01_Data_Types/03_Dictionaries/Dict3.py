details = {
    "person": {
        "name": "Drashti",
        "skills": ["Python", "Django", "MySQL"]
    }
}

# Print name
print(details["person"]["name"])        # Drashti
print("------------------------")

# Add new skill "HTML"
details["person"]["skills"].append("HTML")
print(details)      # {'person': {'name': 'Drashti', 'skills': ['Python', 'Django', 'MySQL', 'HTML']}}
print("------------------------")

# Count skills
print(len(details['person']['skills']))         # 4


