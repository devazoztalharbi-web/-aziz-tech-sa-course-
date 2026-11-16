# Pause exercise solution:
# clean names, append tasks, skip blank, and handle missing status key.

def clean_title(raw):
    return raw.strip().lower().replace("!", "")


tasks = []
raw_items = ["  Plan outline! ", "", "  Film intro  ", "   "]
for raw in raw_items:
    title = clean_title(raw)
    if title == "":
        print("SKIP blank")
        continue
    tasks.append({"title": title, "status": "todo"})

# Missing key demo: use .get so one bad row does not crash the list view.
tasks.append({"title": "broken row"})  # no status on purpose
print("=== YOUR LIST ===")
for task in tasks:
    status = task.get("status", "MISSING")
    print(status.upper(), "-", task["title"])
print("saved tasks with status:", len([t for t in tasks if "status" in t]))
