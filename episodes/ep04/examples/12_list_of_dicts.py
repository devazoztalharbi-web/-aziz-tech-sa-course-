tasks = [
    {"title": "write brief", "status": "done"},
    {"title": "record voice", "status": "todo"},
    {"title": "edit video", "status": "todo"},
]
for task in tasks:
    print(task["status"].upper(), "-", task["title"])
