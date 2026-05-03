students = []


# menu display kept simple for now
def showMenu():
    print("\n==== Student Record Manager ====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search by ID")
    print("4. Statistics")
    print("5. Save File")
    print("6. Load File")
    print("7. Exit")


def addStudent():
    sid = input("Enter Student ID: ")
    studentName = input("Enter Name: ")

    # age input
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except:
            print("Please enter valid age.")

    mark = -1

    # keep asking until valid
    while mark < 0 or mark > 100:
        try:
            mark = float(input("Enter Marks (0-100): "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
        except:
            print("Invalid number.")
            mark = -1

    data = {
        "id": sid,
        "name": studentName,
        "age": age,
        "marks": mark
    }

    students.append(data)
    print("Student added.")


def displayStudents():
    if len(students) == 0:
        print("No student records yet.")
        return

    print("\n--- Students List ---")
    print("ID\tName\t\tAge\tMarks")

    for item in students:
        print(
            str(item["id"]) + "\t" +
            str(item["name"]) + "\t\t" +
            str(item["age"]) + "\t" +
            str(item["marks"])
        )


def searchStudent():
    findId = input("Enter ID to search: ")
    found = False

    for s in students:
        if s["id"] == findId:
            print("\nRecord Found")
            print("ID   :", s["id"])
            print("Name :", s["name"])
            print("Age  :", s["age"])
            print("Marks:", s["marks"])
            found = True
            break

    if found == False:
        print("Student not found.")


def showStats():
    if len(students) == 0:
        print("Nothing to calculate.")
        return

    markList = []

    for x in students:
        markList.append(x["marks"])

    high = max(markList)
    low = min(markList)

    avg = sum(markList) / len(markList)

    print("\n--- Stats ---")
    print("Highest Marks :", high)
    print("Lowest Marks  :", low)
    print("Average Marks :", round(avg, 2))


def saveFile():
    f = open("students.txt", "w")

    for row in students:
        line = row["id"] + "," + row["name"] + "," + str(row["age"]) + "," + str(row["marks"])
        f.write(line + "\n")

    f.close()
    print("Saved successfully.")

    # maybe json later


def loadFile():
    global students
    students = []

    try:
        f = open("students.txt", "r")

        for line in f:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(",")

            temp = {
                "id": parts[0],
                "name": parts[1],
                "age": int(parts[2]),
                "marks": float(parts[3])
            }

            students.append(temp)

        f.close()
        print("Data loaded.")

    except:
        print("File not found or invalid file.")


def startProgram():
    running = True

    while running:
        showMenu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            addStudent()

        elif choice == "2":
            displayStudents()

        elif choice == "3":
            searchStudent()

        elif choice == "4":
            showStats()

        elif choice == "5":
            saveFile()

        elif choice == "6":
            loadFile()

        elif choice == "7":
            print("Closing program...")
            running = False

        else:
            print("Wrong choice. Try again.")


if __name__ == "__main__":
    startProgram()