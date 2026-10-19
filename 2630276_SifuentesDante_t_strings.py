# ============================================================
# STRING PRACTICE IN PYTHON
# ============================================================
# Portada
# Name: Dante Cecilio Sifuentes Martinez.
# Student ID: 2630276.
# Group: IM 1-3.
# File name: 2630276_SifuentesDante_t_strings.py
#
# ============================================================
# RESUMEN EJECUTIVO
# ============================================================
# A string in Python is a text sequence data type and is immutable.
# Strings can be concatenated, measured, sliced, searched, and replaced.
# Indexing allows access to individual characters, while slicing extracts
# parts of a string. Methods such as lower(), upper(), strip(), split(),
# replace(), and join() make text processing easier.
# Input validation is important because it prevents empty, malformed,
# or unexpected data from being processed.
# Normalizing text with strip() and lower() makes comparisons more reliable.
# This program covers six string problems with descriptions, inputs,
# outputs, validations, and three test cases for each problem.
#
# ============================================================
# PRINCIPLES AND GOOD PRACTICES
# ============================================================
# - Strings are immutable: a change creates a new string.
# - Normalize input with strip() and lower() before comparing when needed.
# - Avoid magic numbers in indexes; document what each slice extracts.
# - Use string methods instead of rewriting basic text-processing logic.
# - Validate clearly: first check that input is not empty, then check format.
# - Use readable variable names and understandable error messages.
#
# ============================================================
# PROBLEM 1: FULL NAME FORMATTER
# ============================================================
# Description:
# Receives a person's full name in one string.
# The program normalizes spaces and letter case, then displays
# the name in Title Case and its initials.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - The name must not be empty after strip().
# - The name must contain at least two words.
# - A string containing only spaces is not accepted.
#
# Test cases:
# 1) Normal: "juan carlos tovar" -> "Juan Carlos Tovar", "J.C.T."
# 2) Border: " Ana   Lopez " -> "Ana Lopez", "A.L."
# 3) Error: "Juan" -> Error: full name must contain at least two words.
# ============================================================

def problem_1_full_name_formatter():
    full_name = input("\nEnter full name: ").strip()

    if not full_name:
        print("Error: input cannot be empty.")
        return

    words = full_name.split()

    if len(words) < 2:
        print("Error: full name must contain at least two words.")
        return

    formatted_name = " ".join(words).title()
    initials = "".join(word[0].upper() + "." for word in words)

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ============================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR
# ============================================================
# Description:
# Validates a basic email structure.
# A valid email must contain exactly one '@', have a dot after '@',
# and contain no whitespace.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - "Domain: <domain_part>" when valid
#
# Validations:
# - The email must not be empty after strip().
# - The email must contain exactly one '@'.
# - The email must not contain spaces.
# - A dot must exist after the '@'.
#
# Test cases:
# 1) Normal: "student@example.com" -> valid, domain "example.com"
# 2) Border: "a@b.c" -> valid, domain "b.c"
# 3) Error: "student example.com" -> invalid
# ============================================================

def problem_2_email_validator():
    email_text = input("\nEnter email: ").strip()

    if not email_text:
        print("Valid email: false")
        print("Error: input cannot be empty.")
        return

    if " " in email_text:
        print("Valid email: false")
        print("Error: email must not contain spaces.")
        return

    if email_text.count("@") != 1:
        print("Valid email: false")
        print("Error: email must contain exactly one '@'.")
        return

    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]

    if not domain_part or "." not in domain_part:
        print("Valid email: false")
        print("Error: domain must contain at least one '.'.")
        return

    local_part = email_text[:at_index]
    if not local_part:
        print("Valid email: false")
        print("Error: email must contain text before '@'.")
        return

    print("Valid email: true")
    print(f"Domain: {domain_part}")


# ============================================================
# PROBLEM 3: PALINDROME CHECKER
# ============================================================
# Description:
# Determines whether a phrase reads the same forward and backward.
# Spaces and letter case are ignored.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - Normalized phrase
#
# Validations:
# - The phrase must not be empty after strip().
# - At least 3 characters are required after removing spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "abcba" -> true
# 3) Error: "a" -> error because the minimum length is 3
# ============================================================

def problem_3_palindrome_checker():
    phrase = input("\nEnter phrase: ").strip()

    if not phrase:
        print("Error: input cannot be empty.")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("Error: phrase must contain at least 3 characters after cleaning spaces.")
        return

    reversed_phrase = normalized_phrase[::-1]

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {'true' if normalized_phrase == reversed_phrase else 'false'}")


# ============================================================
# PROBLEM 4: SENTENCE WORD STATS
# ============================================================
# Description:
# Receives a sentence, normalizes spaces, separates words, and displays
# the total word count, first word, last word, shortest word,
# and longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - The sentence must not be empty after strip().
# - At least one valid word must remain after split().
#
# Test cases:
# 1) Normal: "Python is easy to learn"
# 2) Border: " Hello " -> one word
# 3) Error: "   " -> invalid empty sentence
# ============================================================

def problem_4_sentence_word_stats():
    sentence = input("\nEnter sentence: ").strip()

    if not sentence:
        print("Error: sentence cannot be empty.")
        return

    words = sentence.split()

    if not words:
        print("Error: no valid words were found.")
        return

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ============================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
# ============================================================
# Description:
# Classifies a password as weak, medium, or strong.
#
# Rules used:
# - Weak: length < 8 or very simple.
# - Medium: length >= 8 and has mixed letters and/or digits.
# - Strong: length >= 8 and has uppercase, lowercase, digit,
#   and at least one non-alphanumeric symbol.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - Password cannot be empty.
# - Length is checked with len().
#
# Test cases:
# 1) Normal: "Hola1234" -> medium
# 2) Border: "A1b!" -> weak because length is less than 8
# 3) Error: "" -> invalid empty password
#
# Note:
# A password of 8+ characters with all required character categories
# is classified as strong. Other valid non-empty passwords are medium
# when they are not weak.
# ============================================================

def problem_5_password_strength_classifier():
    password_input = input("\nEnter password: ")

    if not password_input:
        print("Error: password cannot be empty.")
        return

    password_length = len(password_input)

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    if password_length < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif has_upper or has_lower or has_digit:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")


# ============================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER
# ============================================================
# Description:
# Receives a product name and price and creates a fixed-width label.
# The complete label must contain exactly 30 characters.
#
# Base format:
# Product: <NAME> | Price: $<PRICE>
#
# If the label is shorter than 30 characters, spaces are added at the end.
# If it is longer than 30 characters, it is cut with label[:30].
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'
#
# Validations:
# - Product name must not be empty after strip().
# - Price must be convertible to a positive number.
#
# Test cases:
# 1) Normal: product_name="Keyboard", price_value="499.90"
# 2) Border: product_name="A", price_value="1"
# 3) Error: product_name="Mouse", price_value="-10"
# ============================================================

LABEL_WIDTH = 30


def problem_6_product_label_formatter():
    product_name = input("\nEnter product name: ").strip()
    price_input = input("Enter price: ").strip()

    if not product_name:
        print("Error: product name cannot be empty.")
        return

    if not price_input:
        print("Error: price cannot be empty.")
        return

    try:
        price_value = float(price_input)
    except ValueError:
        print("Error: price must be a valid number.")
        return

    if price_value <= 0:
        print("Error: price must be positive.")
        return

    if price_value.is_integer():
        price_text = f"{price_value:.0f}"
    else:
        price_text = f"{price_value:.2f}"

    label = f"Product: {product_name} | Price: ${price_text}"

    if len(label) < LABEL_WIDTH:
        label = label + (" " * (LABEL_WIDTH - len(label)))
    else:
        label = label[:LABEL_WIDTH]

    print(f'Label: "{label}"')
    print(f"Length: {len(label)}")


# ============================================================
# MAIN PROGRAM
# ============================================================
# Each problem is kept in a separate function so the code is organized,
# readable, and easy to explain.
# ============================================================

def main():
    print("==========================================")
    print("       PYTHON STRING PRACTICE")
    print("==========================================")
    print("Run each problem one at a time.")

    problem_1_full_name_formatter()
    problem_2_email_validator()
    problem_3_palindrome_checker()
    problem_4_sentence_word_stats()
    problem_5_password_strength_classifier()
    problem_6_product_label_formatter()

    print("\nAll six problems have been completed.")


if __name__ == "__main__":
    main()


# ============================================================
# CONCLUSIONS
# ============================================================
# String handling is essential for receiving and displaying data.
# Methods such as strip(), lower(), split(), and join() help normalize
# and organize text before it is processed.
# Normalizing text makes comparisons more consistent and reduces errors
# caused by extra spaces or different letter cases.
# Clear validations prevent invalid or unwanted data from entering
# the main processing logic.
# Strings are immutable, so operations such as replace() create a new string.
# Slicing is useful for extracting or trimming parts of a string.
# These exercises demonstrate practical string operations used in Python.
#
# ============================================================
# REFERENCES
# ============================================================
# References:
# 1) Python documentation - Built-in Types: Text Sequence Type — str
# 2) Python documentation - Common String Operations
# 3) Python documentation - Built-in Functions: len()
# 4) Python documentation - String Methods
# 5) Python documentation - Input and Output