def clean_title(raw):
    text = raw.strip().lower()
    text = text.replace("!", "")
    return text

name = clean_title("  Ship CLIP!  ")
print("stored:", name)
print("upper again:", name.upper())
