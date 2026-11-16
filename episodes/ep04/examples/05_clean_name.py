raw = "  Write BRIEF!!!  "
clean = raw.strip()
clean = clean.lower()
clean = clean.replace("!", "")
print("raw:", repr(raw))
print("clean:", clean)
