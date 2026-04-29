import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # 2. Boş olub-olmadığını yoxla
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template
        
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            content = content.replace(f"{{{key}}}", str(value))
        
        output_filename = f"output_{i}.txt"
        
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")