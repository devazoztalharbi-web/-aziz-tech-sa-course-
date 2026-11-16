candidates = ["  Write brief  ", "   ", "Edit video", ""]
for raw in candidates:
    title = raw.strip()
    if title == "":
        print("SKIP blank")
    else:
        print("KEEP", title)
