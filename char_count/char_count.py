def analyze_text_file():
    try:
        with open("char_count.txt", 'r') as file:
            char_count = 0
            word_count = 0
            space_count = 0
            line_count = 0

            for line in file:
                line_count += 1
                char_count += len(line)
                words = line.split()
                word_count += len(words)
                space_count += len(words) - 1

            print("File analysis summary:")
            print("Character count:", char_count)
            print("Word count:", word_count)
            print("Space count:", space_count)
            print("Line count:", line_count)

    except FileNotFoundError:
        print("File not found!")

# Usage
analyze_text_file()
input()