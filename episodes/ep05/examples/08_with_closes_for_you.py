with open("notes.txt", "a", encoding="utf-8") as notebook:
    notebook.write("راجع درس بايثون\n")

with open("notes.txt", "r", encoding="utf-8") as notebook:
    print(notebook.read())
