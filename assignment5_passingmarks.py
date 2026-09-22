#Student marks and 70% passing benchmark

marks = [60, 45, 70, 80, 30]

passed = 0

for m in marks:
    if m >= 50:
        passed += 1

percentage = (passed / len(marks)) * 100

print("Passed students:", passed)
print("Passing percentage:", percentage)

if percentage >= 70:
    print("Class performance meets the benchmark")
else:
    print("Class performance does not meet the benchmark")