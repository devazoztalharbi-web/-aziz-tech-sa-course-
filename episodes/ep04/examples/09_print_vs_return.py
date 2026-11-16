def show_only(raw):
    print("shown:", raw.strip())

def give_back(raw):
    return raw.strip()

a = show_only("  Task A  ")
print("a is:", a)

b = give_back("  Task B  ")
print("b is:", b)
print("b upper:", b.upper())
