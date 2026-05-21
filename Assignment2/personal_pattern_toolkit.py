def get_valid_number():

    while True:
        number = int(input("Enter a number between 3 and 9: "))

        if 3 <= number <= 9:
            return number
        else:
            print("Invalid input. Please enter a number between 3 and 9.")



def generate_personal_code(student_id, keyword):

    first_letter = keyword[0].upper()
    last_letter = keyword[-1].upper()

    code = f"{first_letter}-{student_id}-{last_letter}"

    return code



def count_character_frequency(name):

    frequency = {}

    name = name.lower().replace(" ", "")

    for char in name:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency



def find_unique_vowels_consonants(text):

    vowels = set("aeiou")

    unique_vowels = set()
    unique_consonants = set()

    text = text.lower().replace(" ", "")

    for char in text:

        if char.isalpha():

            if char in vowels:
                unique_vowels.add(char)
            else:
                unique_consonants.add(char)

    return unique_vowels, unique_consonants



def check_balanced_brackets(expression):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:

        if char in "([{":
            stack.append(char)

        elif char in ")]}":

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0



def process_keyword_queue(keyword):

    queue = []

    for char in keyword:
        queue.append(f"Analyse {char}")

    print("\nQueue Processing:")

    while queue:

        task = queue.pop(0)

        print("Processing:", task)


def print_number_pattern(number):

    print("\nNumber Pattern:")

    for i in range(1, number + 1):

        for j in range(1, i + 1):
            print(j, end=" ")

        print()


def recursive_digit_sum(student_id):

    if len(student_id) == 1:
        return int(student_id)

    return int(student_id[0]) + recursive_digit_sum(student_id[1:])



def display_summary():

    print("\n===== Personal Pattern Toolkit =====")


display_summary()

student_id = input("Enter Student ID: ")

full_name = input("Enter Full Name: ")

keyword = input("Enter Keyword: ")

number = get_valid_number()

bracket_expression = input("Enter bracket expression: ")


personal_code = generate_personal_code(student_id, keyword)

print("\nPersonal Code:", personal_code)


frequency = count_character_frequency(full_name)

print("\nCharacter Frequency:")

for char, count in frequency.items():
    print(char, ":", count)


combined_text = full_name + keyword

vowels, consonants = find_unique_vowels_consonants(combined_text)

print("\nUnique Vowels:", ", ".join(sorted(vowels)))

print("Unique Consonants:", ", ".join(sorted(consonants)))


balanced = check_balanced_brackets(bracket_expression)

if balanced:
    print("\nBalanced Brackets: Yes")
else:
    print("\nBalanced Brackets: No")


process_keyword_queue(keyword)


print_number_pattern(number)


digit_sum = recursive_digit_sum(student_id)

print("\nRecursive Digit Sum of Student ID:", digit_sum)