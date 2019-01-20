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
    # TODO Check to make sure that the referenced registers are valid for the question
    command = "exec_" + tokens[0] + "('" + tokens[1] + "', '" + tokens[2] + "')"
    eval(command)

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
    # TODO Check to make sure that the referenced registers are valid for the question
    command = "exec_" + tokens[0] + "('" + tokens[1] + "', '" + tokens[2] + "')"
    eval(command)

def validate_RB(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$" and tokens[1][-1] != "b":
        try:
            inttest = int(tokens[1])
        except:
            raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register or a binary string")
    if tokens[2][0] != "$":
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Output must be a register")
    # TODO Check to make sure that the referenced registers are valid for the question
    command = "exec_" + tokens[0] + "('" + tokens[1] + "', '" + tokens[2] + "')"
    eval(command)

def validate_jmp(tokens, linenum):
    if len(tokens) != 2:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    try:
        labels[tokens[1]]
    except:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Jump destination " + tokens[1] + " not in " + str(labels))
    command = "exec_jmp('" + tokens[1] + "')"
    eval(command)

def validate_jmpf(tokens, linenum):
    if len(tokens) != 5:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if labels.get(tokens[4]) == None:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Jump destination " + tokens[4] + " not in " + str(labels))
    command = "exec_cmp" + "('" + tokens[2] + "', '" + tokens[1] + "', '" + tokens[3] + "')"
    comparatorResponse = eval(command)
    if comparatorResponse > 0:
        command = "exec_jmp('" + tokens[4] + "')"
        eval(command)

def evaluate_code(line):
    print("TODO remove all execution steps from the validate functions and put them here to allow for jumping")

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

def exec_cmp(cmp, v1, v2):
    print("TODO compare " + v1 + " " + cmp + " " + v2 + "\n")
    return 1

def code_parse(filename):
    with open(filename) as f:
        inputcode = f.readlines()
    inputcode = [x.strip() for x in inputcode]

    linenum = 0
    lineTokens = []
    for line in inputcode:
        linenum += 1
        lineTokens.append(extract_data(line, str(linenum)))
    lineTokens = list(filter(None, lineTokens))

    print("")
    print("Registers Used:")
    print(registers)
    print("Labels:")
    print(labels)
    print("")

    linenum = 0
    for line in lineTokens:
        linenum += 1
        check_syntax(line, str(linenum))
    
    print(lineTokens)
    evaluate_code(lineTokens)


main()