# خطأ متعمد لطيف: نسينا \n في آخر كل ملاحظة
notebook = open("shopping.txt", "w", encoding="utf-8")
notebook.write("خبز")
notebook.write("بيض")
notebook.write("تمر")
notebook.close()

notebook = open("shopping.txt", "r", encoding="utf-8")
print(notebook.read())
notebook.close()
