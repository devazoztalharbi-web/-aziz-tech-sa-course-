notebook = open("notes.txt", "r", encoding="utf-8")
content = notebook.read()
notebook.close()
print(content)
