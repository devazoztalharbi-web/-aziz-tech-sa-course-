def clean_title(raw):
    return str(raw).strip().lower().replace("!", "").replace("?", "")

def add_task(tasks, raw_title, status="todo"):
    title = clean_title(raw_title)
    if title == "":
        print("SKIP blank title"); return
    tasks.append({"title": title, "status": status})

def show_tasks(tasks):
    print("=== TASK LIST ===")
    if not tasks:
        print("(empty)"); return
    for i, task in enumerate(tasks, start=1):
        print(i, task["status"].upper(), "-", task["title"])

def count_status(tasks):
    counts = {}
    for task in tasks:
        s = task["status"]
        counts[s] = counts.get(s, 0) + 1
    return counts

tasks = []
add_task(tasks, "  Write BRIEF!  ")
add_task(tasks, "Record Voice")
add_task(tasks, "   ")
add_task(tasks, "Edit Video", "done")
show_tasks(tasks)
print("counts:", count_status(tasks))
