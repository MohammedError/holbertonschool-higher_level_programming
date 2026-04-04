#!/usr/bin/env python3
"""Task 0: Creating a Simple Templating Program"""
import os


def generate_invitations(template, attendees):
      """Generate invitation files from a template and list of attendees."""
      # Check input types
      if not isinstance(template, str) or not isinstance(attendees, list):
                print("Error: template must be a string and attendees must be a list of dictionaries.")
                return

      # Validate attendees is a list of dicts
      for item in attendees:
                if not isinstance(item, dict):
                              print("Error: template must be a string and attendees must be a list of dictionaries.")
                              return

            # Handle empty template
            if not template.strip():
                      print("Template is empty, no output files generated.")
                      return

    # Handle empty attendees list
    if len(attendees) == 0:
              print("No data provided, no output files generated.")
              return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
              output = template
              for placeholder in ["name", "event_title", "event_date", "event_location"]:
                            value = attendee.get(placeholder, None)
                            if value is None:
                                              value = "N/A"
                                          output = output.replace("{" + placeholder + "}", str(value))

              output_filename = f"output_{index}.txt"
              with open(output_filename, "w") as f:
                            f.write(output)
                
