print("=== دفتر ملاحظاتي ===")
note = input("اكتب ملاحظتك: ")

with open("notes.txt", "a", encoding="utf-8") as notebook:
    notebook.write(note + "\n")
print("انحفظت ✅")

print("--- كل ملاحظاتك ---")
with open("notes.txt", "r", encoding="utf-8") as notebook:
    for number, line in enumerate(notebook, start=1):
        print(number, "-", line.strip())
