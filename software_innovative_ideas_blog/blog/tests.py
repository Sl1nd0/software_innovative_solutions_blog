from django.test import TestCase

# Create your tests here.
# Initialize an empty list to store errors
errors = []

try:
    # Code that may raise an exception
    result = 1 / 0  # This will raise a ZeroDivisionError
except Exception as error:
    # Append the error to the list
    errors.append(error)

print("Errors:", errors[0])