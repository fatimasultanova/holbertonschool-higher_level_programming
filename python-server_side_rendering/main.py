from task_00_intro import generate_invitations

try:
    with open('python-server_side_rendering/template.txt', 'r', encoding='utf-8') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
    print("Process completed! You can check the output files.")

except FileNotFoundError:
    print("Error: 'python-server_side_rendering/template.txt' file not found. Please check the folder location.")
