def write_lines_to_file(filename):
    lines = []
    print("Enter your lines of text (type 'DONE' on a new line to finish):")

    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

    print(f"Text successfully written to {filename}")


if __name__ == "__main__":
    filename = "output.txt"  # Specify the file name
    write_lines_to_file(filename)
