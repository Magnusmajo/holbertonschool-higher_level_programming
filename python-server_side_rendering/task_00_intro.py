#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    # Verify that template is a string and attendees is a list of dictionaries
    if not isinstance(template, str) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Invalid inputs. Make sure to enter a valid list.")
        return

    # Check if the template is empty
    if not template.strip():
        print("Error: The template is empty, no output files generated.")
        return

    # Check if the list of attendees is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template.replace("{name}", attendee.get("name", "N/A"))
        processed_template = processed_template.replace("{event_title}", attendee.get("event_title", "N/A"))
        processed_template = processed_template.replace("{event_date}", attendee.get("event_date", "N/A"))
        processed_template = processed_template.replace("{event_location}", attendee.get("event_location", "N/A"))

        # Generate the output filename
        output_filename = f"output_{i}.txt"

        try:
            # Check if the file already exists
            if os.path.exists(output_filename):
                print(f"Warning: File {output_filename} already exists. Skipping...")
                continue

            # Write to the output file
            with open(output_filename, "w") as output_file:
                output_file.write(processed_template)

            print(f"File {output_filename} generated successfully.")
        except Exception as e:
            print(f"Error generating file {output_filename}: {str(e)}")
