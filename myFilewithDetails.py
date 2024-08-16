try:
    with open('demofile.txt', 'r') as file:
        content = file.read() # process content
        print("File Available")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied to open file!")
except Exception as e:
    print("Error:", e)
