tasks = [
    {"title": "write brief", "status": "done"},
    {"title": "record voice", "status": "todo"},
    {"title": "edit video", "status": "todo"},
    {"title": "publish clip", "status": "done"},
]
counts = {}
for task in tasks:
    status = task["status"]
    if status in counts:
        counts[status] = counts[status] + 1
    else:
        counts[status] = 1
print(counts)
