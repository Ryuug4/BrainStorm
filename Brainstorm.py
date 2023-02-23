import sys

# Read the Brainfuck code from a file
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} filename")
    sys.exit(1)
with open(sys.argv[1]) as f:
    code = f.read()

# Initialize the tape
tape = [0]

# Initialize the pointer
pointer = 0

# Loop through the Brainfuck code
i = 0
while i < len(code):
    if code[i] == "+":
        tape[pointer] += 1
    elif code[i] == "-":
        tape[pointer] -= 1
    elif code[i] == ">":
        pointer += 1
        if pointer == len(tape):
            tape.append(0)
    elif code[i] == "<":
        pointer -= 1
        if pointer < 0:
            tape.insert(0, 0)
            pointer = 0
    elif code[i] == ".":
        print(chr(tape[pointer]), end="")
    elif code[i] == ",":
        tape[pointer] = ord(input()[0])
    elif code[i] == "[":
        if tape[pointer] == 0:
            # Skip to the matching ]
            level = 1
            while level != 0:
                i += 1
                if code[i] == "[":
                    level += 1
                elif code[i] == "]":
                    level -= 1
    elif code[i] == "]":
        if tape[pointer] != 0:
            # Backtrack to the matching [
            level = 1
            while level != 0:
                i -= 1
                if code[i] == "[":
                    level -= 1
                elif code[i] == "]":
                    level += 1
            # Move the instruction pointer back one step to re-evaluate the [ instruction
            i -= 1
    i += 1
