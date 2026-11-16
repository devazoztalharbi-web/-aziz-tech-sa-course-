line = "write brief | record voice | edit video"
parts = line.split("|")
print(parts)
trimmed = []
for part in parts:
    trimmed.append(part.strip())
print(trimmed)
joined = " / ".join(trimmed)
print(joined)
