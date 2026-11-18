notebook = open("notes.txt", "w", encoding="utf-8")
notebook.write("موعد الدكتور الساعة 5\n")
notebook.close()

notebook = open("notes.txt", "r", encoding="utf-8")
print(notebook.read())
notebook.close()
