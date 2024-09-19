import sys
import random
import string

def generate_text(first_symbol, length):
    #random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length-1))
    random_chars = 'cat ' * (length - 1)
    return first_symbol + random_chars

def write_to_file(content, filename="generated_text.txt"):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <first_symbol> <length>")
        sys.exit(1)

    first_symbol = sys.argv[1]
    length = int(sys.argv[2])

    text = generate_text(first_symbol, length)
    write_to_file(text)
    print(f"Generated file 'generated_text.txt' with length {length}")