assignments = ["Math", "Science", "English"]
print("Assignments:", assignments)

new_assignment = input("Enter a new assignment: ")
assignments.append(new_assignment)
completed = input("Enter completed assignment to remove: ")

if completed in assignments:
    assignments.remove(completed)
    print("Assignment removed.")
else:
    print("Assignment not found.")

print("Updated Assignments:", assignments)