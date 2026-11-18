notebook = open("notes.txt", "a", encoding="utf-8")
notebook.write("اتصل على أمي\n")
notebook.close()

notebook = open("notes.txt", "r", encoding="utf-8")
print(notebook.read())
notebook.close()
