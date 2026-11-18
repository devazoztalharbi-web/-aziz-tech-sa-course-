# حل الواجب: دفتر أسماء + آخر اسم انضاف
name = input("وش اسمك؟ ")

with open("names.txt", "a", encoding="utf-8") as names_book:
    names_book.write(name + "\n")

with open("names.txt", "r", encoding="utf-8") as names_book:
    lines = names_book.readlines()

print("عدد الأسماء:", len(lines))
print("آخر اسم انضاف:", lines[-1].strip())
