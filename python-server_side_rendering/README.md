In this project, you will build a Flask application that serves web pages using server-side rendering techniques. You will start by creating basic templates and gradually move towards integrating dynamic content from multiple data sources. By the end of the project, you will have a comprehensive understanding of SSR, templating, and how to build efficient, scalable web applications.

## Tasks

### 0. Creating a Simple Templating Program

In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.

Objective
Understand how to use string templating in Python.
Implement file operations for reading templates and writing output files.
Handle various edge cases and errors gracefully.
Instructions
Create the Template:

Use the provided template with placeholders for name, event_title, event_date, and event_location.
Define the Data:

Use the provided list of objects as your data source.
Write the Templating Function:

Define a function named generate_invitations that takes two parameters: template and attendees.
Check Input Types:

Verify that template is a string and attendees is a list of dictionaries.
If template is not a string or attendees is not a list of dictionaries, log an error message and terminate the function.
Handle Empty Inputs:

Check if the template is empty and log an error message if it is.
Check if the attendees list is empty and log an error message if it is.
Process Each Attendee:

Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
If a value is missing, replace it with “N/A”.
Generate Output Files:

Write the processed template to output files named output_X.txt, where X is the index of the attendee starting from 1.
Specific Error Handling Behaviors:
Empty Template: If the template is empty, log an error message, “Template is empty, no output files generated.” and terminate without creating any files.
Empty List of Objects: If the list of objects is empty, log a message, “No data provided, no output files generated.” and terminate without creating any files.
Missing Data in Object: If an object is missing data for any of the placeholders, replace the missing data with the text “N/A” in the output file. For example, if event_date is missing, it should appear as “event_date: N/A” in the output.
Invalid Input Types: If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.

-------------------                  -------------------
Template File: template.txt
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
Example Data for Testing:
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
Example Main File to Test the Program:
<!-- Main file content -->
from task_00_intro import generate_invitations

<!-- Read the template from a file -->
with open('template.txt', 'r') as file:
    template_content = file.read()

<!-- List of attendees -->
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

<!-- Call the function with the template and attendees list-->
generate_invitations(template_content, attendees)
Hints:
Use Python’s string replace method to substitute placeholders with actual values.
Use os.path.exists to check if a file already exists before writing.
Use try and except blocks to handle potential errors gracefully.
--------------                         ----------------