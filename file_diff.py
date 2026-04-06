import difflib

file1 = input("Enter first file: ")
file2 = input("Enter second file: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    diff = difflib.ndiff(lines1, lines2)

    print("\nDifferences:\n")
    for line in diff:
        if line.startswith("- "):
            print(f"Removed: {line[2:].strip()}")
        elif line.startswith("+ "):
            print(f"Added: {line[2:].strip()}")

except FileNotFoundError:
    print("One or both files not found.")
