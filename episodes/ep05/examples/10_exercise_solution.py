# حل التمرين: كم ملاحظة في الدفتر؟
with open("notes.txt", "r", encoding="utf-8") as notebook:
    lines = notebook.readlines()

print("عندك", len(lines), "ملاحظات في الدفتر")
