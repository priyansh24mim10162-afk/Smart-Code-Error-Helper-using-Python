import traceback

# Error dictionary
errors = {
    "NameError": {
        "explanation": "You used a variable before defining it.",
        "solution": "Define the variable before using it."
    },
    "SyntaxError": {
        "explanation": "There is a syntax mistake in your code.",
        "solution": "Check for missing colons, brackets, or keywords."
    },
    "IndentationError": {
        "explanation": "Your code is not properly indented.",
        "solution": "Use proper spacing inside loops and conditions."
    },
    "TypeError": {
        "explanation": "You used incompatible data types.",
        "solution": "Ensure data types match."
    },
    "ValueError": {
        "explanation": "Invalid value provided.",
        "solution": "Enter a valid value."
    },
    "IndexError": {
        "explanation": "Index is out of range.",
        "solution": "Check list length."
    },
    "KeyError": {
        "explanation": "Key not found in dictionary.",
        "solution": "Use valid keys."
    },
    "ZeroDivisionError": {
        "explanation": "Division by zero is not allowed.",
        "solution": "Ensure denominator is not zero."
    },
    "AttributeError": {
        "explanation": "Object has no such method.",
        "solution": "Check object type and method name."
    }
}

def analyze_code():
    print("\nPaste your Python code (type 'END' in new line to finish):")

    user_code = ""
    while True:
        line = input()
        if line == "END":
            break
        user_code += line + "\n"

    try:
        exec(user_code)
        print("\n✅ No errors found. Code executed successfully!")

    except Exception as e:
        error_type = type(e).__name__

        # Handle SyntaxError separately
        if isinstance(e, SyntaxError):
            line_number = e.lineno
        else:
            tb = traceback.TracebackException.from_exception(e)
            line_number = None
            for frame in tb.stack:
                if frame.filename == "<string>":
                    line_number = frame.lineno
                    break

        print("\n❌ Error Found!")
        print("📍 Line Number:", line_number)
        print("🔍 Error Type:", error_type)

        if error_type in errors:
            print("📘 Explanation:", errors[error_type]["explanation"])
            print("💡 Solution:", errors[error_type]["solution"])
        else:
            print("📘 Explanation: Unknown error")
            print("💡 Try checking your code.")


# Main Menu
while True:
    print("\n===== SMART CODE ERROR HELPER =====")
    print("1. Analyze my code")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        analyze_code()
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Invalid choice")