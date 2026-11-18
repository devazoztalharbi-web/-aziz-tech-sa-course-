# خطأ متعمد: اسم الدفتر غلط (note بدل notes)
notebook = open("note.txt", "r", encoding="utf-8")
print(notebook.read())
notebook.close()
