import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, None)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))
        output_filename = "output_{}.txt".format(index)
        with open(output_filename, 'w') as f:
            f.write(content)
