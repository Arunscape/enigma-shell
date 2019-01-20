registers = {"out": None}
labels = {}

def main():
    filename = ""
    # filename = input("Enter your code file name here:\n")
    if len(filename) == 0:
        filename = "codetest.eng"
    code_parse(filename)

def extract_data(line, linenum):
    tokens = line.split()
    tokens = [x.strip().lower() for x in tokens]

    # IGNORE COMMENTS
    if tokens[0][0] == "#":
        return ""

    tokenNumber = 0
    for token in tokens:
        tokenNumber += 1
        if token[0] == "#":
            tokens = tokens[0:tokenNumber-1]
            break

    # EXTRACT REGISTERS AND JUMP DESTINATIONS
    for token in tokens:
        if token[0] == "$":
            if registers.get(token[1:]) == None:
                registers[token[1:]] = 0
    if tokens[0][-1] == ":":
        if labels.get(tokens[0][-1]) == None:
            labels[tokens[0][:-1]] = linenum
        else:
            raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Label " + tokens[0][:-1] + " already in use on line " + labels.get(tokens[0][:-1]))
        del tokens[0]

    return tokens

def check_syntax(tokens, linenum):
    # CHECK THE SYNTAX FOR THE FUNCTION
    cmd = tokens[0]
    if cmd == "mv":
        validate_RIB(tokens, linenum)
    if cmd == "add" or cmd == "sub" or cmd == "mul" or cmd == "div":
        validate_RI(tokens, linenum)
    if cmd == "and" or cmd == "or" or cmd == "xor" or cmd == "nand" or cmd == "nor" or cmd == "nxor":
        validate_RB(tokens, linenum)
    if cmd == "jmp":
        validate_jmp(tokens, linenum)
    if cmd == "jmpf":
        validate_jmpf(tokens, linenum)
    
def validate_RIB(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$" and tokens[1][-1] != "b":
        try:
            inttest = int(tokens[1])
        except:
            raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register, an integer, or a binary string")
    if tokens[2][0] != "$":
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Output must be a register")

def validate_RI(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$":
        try:
            inttest = int(tokens[1])
        except:
            raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register or an integer")
    if tokens[2][0] != "$":
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Output must be a register")

def validate_RB(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$" and tokens[1][-1].lower() != "b":
        try:
            inttest = int(tokens[1])
        except:
            raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register or a binary string")
    if tokens[2][0] != "$":
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Output must be a register")

def validate_jmp(tokens, linenum):
    if len(tokens) != 2:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    try:
        labels[tokens[1]]
    except:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Jump destination " + tokens[1] + " not in " + str(labels))

def validate_jmpf(tokens, linenum):
    if len(tokens) != 5:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if labels.get(tokens[4]) == None:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Jump destination " + tokens[4] + " not in " + str(labels))

def evaluate_code(lineTokens, maxLineNum):
    lineNum = 0
    while (lineNum <= maxLineNum):
        lineNum += 1
        instruction = lineTokens.get(lineNum)
        if instruction != None:
            command = "exec_" + instruction[0] + "('"
            if len(instruction) == 2:
                command = command + instruction[1]
            if len(instruction) == 3:
                command = command + instruction[1] + "', '" + instruction[2]
            if len(instruction) == 5:
                command = command + instruction[2] + "', '" + instruction[1] + "', '" + instruction[3] + "', '" + instruction[4]
            command = command + "')"
            eval(command)

def exec_mv(v1, v2):
    print("TODO move " + v1 + " -> " + v2 + "\n")

def exec_add(v1, v2):
    print("TODO add " + v1 + " -> " + v2 + "\n")

def exec_sub(v1, v2):
    print("TODO sub " + v1 + " -> " + v2 + "\n")

def exec_mul(v1, v2):
    print("TODO mul " + v1 + " -> " + v2 + "\n")

def exec_div(v1, v2):
    print("TODO div " + v1 + " -> " + v2 + "\n")

def exec_and(v1, v2):
    print("TODO and " + v1 + " -> " + v2 + "\n")

def exec_nand(v1, v2):
    print("TODO nand " + v1 + " -> " + v2 + "\n")

def exec_or(v1, v2):
    print("TODO or " + v1 + " -> " + v2 + "\n")

def exec_nor(v1, v2):
    print("TODO nor " + v1 + " -> " + v2 + "\n")

def exec_xor(v1, v2):
    print("TODO xor " + v1 + " -> " + v2 + "\n")

def exec_nxor(v1, v2):
    print("TODO nxor " + v1 + " -> " + v2 + "\n")

def exec_jmp(lbl):
    print("TODO jmp -> " + lbl + "\n")

def exec_jmpf(cmp, v1, v2, lbl):
    print("TODO jmpf -> " + lbl + " IF " + v1 + " " + cmp + " " + v2 + "\n")

def exec_cmp(cmp, v1, v2):
    print("TODO compare " + v1 + " " + cmp + " " + v2 + "\n")
    return 1

def code_parse(filename):
    with open(filename) as f:
        inputcode = f.readlines()
    inputcode = [x.strip() for x in inputcode]

    print("")
    print("<> EXTRACTING DATA <>")
    print("")
    linenum = 0
    lineTokens = {}
    for line in inputcode:
        linenum += 1
        lineTokenized = extract_data(line, linenum)
        if len(lineTokenized) != 0:
            lineTokens[linenum] = lineTokenized
    maxLineNum = linenum

    print("Registers Used:")
    print(registers)
    print("Labels:")
    print(labels)
    print("")

    print("<> VALIDATING CODE <>")
    print("")
    print(lineTokens)
    linenum = 0
    for key, line in lineTokens.items():
        linenum += 1
        check_syntax(line, str(linenum))
    print("")
    print("<> CODE VALIDATED <>")
    print("")
    
    print("<> CODE EXECUTING <>")
    print("")
    print(lineTokens)
    print("")
    evaluate_code(lineTokens, maxLineNum)
    print("<> CODE EXECUTED SUCCESSFULLY <>")

main()