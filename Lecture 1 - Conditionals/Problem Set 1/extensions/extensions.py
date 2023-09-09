def filetype():
    f = input("File Name: ").strip().lower()
    if str(f).endswith(".gif"):
        print("image/gif")
    elif str(f).endswith(".jpeg") or str(f).endswith(".jpg"):
        print("image/jpeg")
    elif str(f).endswith(".png"):
        print("image/png")
    elif str(f).endswith(".pdf"):
        print("application/pdf")
    elif str(f).endswith(".txt"):
        print("text/plain")
    elif str(f).endswith(".txt"):
        print("text/plain")
    elif str(f).endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

filetype()

