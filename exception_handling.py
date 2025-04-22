# exception_handling.py

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer!")
else:
    print("Division result:", result)
finally:
    print("Execution finished.")
