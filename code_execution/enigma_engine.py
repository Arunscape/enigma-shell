import requests

import time

from flask import Flask 
from flask import request
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route('/', methods=['GET','POST'])
def test():
    if request.method == "POST":
        return request.json
    else:
        return "Hello WORLD"

URL = "http://35.233.140.84:80"

registers = {"out": []}
labels = {}

def main():
    while True:
        try:
            print("Trying POST...")
            response.headers.add_header("Access-Control-Allow-Origin", "*")
            response = requests.post(url = URL, data = {})
            print("GOT IT GOT IT GOT IT")
            print("--------------------")
            print("")
            print(response)
            print("")
            print("--------------------")
            code_parse(response)
        except:
            print("Mission failed, we'll get 'em next time")
            time.sleep(0.5)

def extract_data(line, linenum):
    tokens = line.split()
    tokens = [x.strip().lower() for x in tokens]

    if len(tokens) == 0:
        return ""

    # IGNORE COMMENTS
    if tokens[0][0] == "#":
        return ""

    tokenNumber = 0
    for token in tokens:
        tokenNumber += 1
        if token[0] == "#":
            tokens = tokens[0:tokenNumber-1]
            break

    # EXTRACT REGISTERS, JUMP DESTINATIONS AND NOPS
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
        validate_mv(tokens, linenum)
    if cmd == "add" or cmd == "sub" or cmd == "mul" or cmd == "div":
        validate_RI(tokens, linenum)
    if cmd == "and" or cmd == "or" or cmd == "xor":
        validate_RB(tokens, linenum)
    if cmd == "jmp":
        validate_jmp(tokens, linenum)
    if cmd == "jmpf":
        validate_jmpf(tokens, linenum)
    
def validate_mv(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$":
        if tokens[1][-1].lower() == "b":
            try: 
                int(tokens[1][:-1], 2)
            except:
                raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register, an integer, or a binary string")
        else:
            try:
                int(tokens[1])
            except:
                raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register, an integer, or a binary string")
    if tokens[2][0] != "$":
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Output must be a register")

def validate_RI(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$":
        try:
            int(tokens[1])
        except:
            raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register or an integer")
    if tokens[2][0] != "$":
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Output must be a register")

def validate_RB(tokens, linenum):
    if len(tokens) != 3:
        raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Invalid command")
    if tokens[1][0] != "$":
        if tokens[1][-1].lower() == "b":
            try:
                int(tokens[1][:-1], 2)
            except:
                raise ValueError("INVALID SYNTAX ON LINE " + linenum + ": Input must be a register or a binary string")
        else:
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
            command = command + "', '" + str(lineNum) + "')"
            lineNum = int(eval(command))

def exec_mv(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    if v1 != "ERR" and v2.lower() != "$out":
        try:
            v1 = int(v1)
        except:
            if v1[-1].lower() != "b":
                raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
            else:
                try:
                    int(v1[:-1], 2)
                except:
                    raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    if v2 == "$out":
        registers[v2[1:]].append(v1)
    else:
        registers[v2[1:]] = v1
    print("move " + str(v1) + " -> " + str(v2) + "\n")
    return lnm

def exec_add(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    try:
        v1 = int(v1)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    val2 = registers.get(v2[1:])
    try:
        val2 = int(val2)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + str(lnm))
    result = v1 + val2
    if v2 == "$out":
        registers[v2[1:]].append(result)
    else:
        registers[v2[1:]] = result
    print("add " + str(v1) + " + " + str(val2) + " = " + str(result) + " -> " + str(v2) + "\n")
    return lnm

def exec_sub(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    try:
        v1 = int(v1)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    val2 = registers.get(v2[1:])
    try:
        val2 = int(val2)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + str(lnm))
    result = -v1 + val2
    if v2 == "$out":
        registers[v2[1:]].append(result)
    else:
        registers[v2[1:]] = result
    print("sub " + str(val2) + " - " + str(v1) + " = " + str(result) + " -> " + str(v2) + "\n")
    return lnm

def exec_mul(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    try:
        v1 = int(v1)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    val2 = registers.get(v2[1:])
    try:
        val2 = int(val2)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + str(lnm))
    result = v1 * val2
    if v2 == "$out":
        registers[v2[1:]].append(result)
    else:
        registers[v2[1:]] = result
    print("mul " + str(v1) + " * " + str(val2) + " = " + str(result) + " -> " + str(v2) + "\n")
    return lnm

def exec_div(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    try:
        v1 = int(v1)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    val2 = registers.get(v2[1:])
    try:
        val2 = int(val2)
    except:
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + str(lnm))
    result = int(val2 / v1)
    if v2 == "$out":
        registers[v2[1:]].append(result)
    else:
        registers[v2[1:]] = result
    print("div " + str(val2) + " / " + str(v1) + " = " + str(result) + " -> " + str(v2) + "\n")
    return lnm

def convert_to_binary(number):
    val = str(bin(number)[2:])
    if val[0] == "b":
        return val[1:] + "b"
    else:
        return val + "b"

def exec_and(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    if (v1[-1].lower() == "b"):
        try:
            int(v1[:-1], 2)
        except:
            raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + lnm)
    else: 
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + lnm)
    val2 = registers.get(v2[1:])
    if (val2[-1].lower() == "b"):
        try:
            int(val2[:-1], 2)
        except:
            raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + lnm)
    else: 
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + lnm)
    val2 = int(val2[:-1], 2)
    val2 = int(v1[:-1], 2) & val2
    res = convert_to_binary(val2)
    print(str(v1) + " AND " + str(registers.get(v2[1:])) + " -> " + str(res) + "\n")
    registers[v2[1:]] = res
    return lnm

def exec_or(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    if (v1[-1].lower() == "b"):
        try:
            int(v1[:-1], 2)
        except:
            raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + lnm)
    else: 
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + lnm)
    val2 = registers.get(v2[1:])
    if (val2[-1].lower() == "b"):
        try:
            int(val2[:-1], 2)
        except:
            raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + lnm)
    else: 
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + lnm)
    val2 = int(val2[:-1], 2)
    val2 = int(v1[:-1], 2) | val2
    res = convert_to_binary(val2)
    print(str(v1) + " OR " + str(registers.get(v2[1:])) + " -> " + str(res) + "\n")
    registers[v2[1:]] = res
    return lnm

def exec_xor(v1, v2, lnm):
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    if (v1[-1].lower() == "b"):
        try:
            int(v1[:-1], 2)
        except:
            raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + lnm)
    else: 
        raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + lnm)
    val2 = registers.get(v2[1:])
    if (val2[-1].lower() == "b"):
        try:
            int(val2[:-1], 2)
        except:
            raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + lnm)
    else: 
        raise RuntimeError("INVALID VALUE: " + str(v2) + " at line " + lnm)
    val2 = int(val2[:-1], 2)
    val2 = int(v1[:-1], 2) ^ val2
    res = convert_to_binary(val2)
    print(str(v1) + " XOR " + str(registers.get(v2[1:])) + " -> " + str(res) + "\n")
    registers[v2[1:]] = res
    return lnm

def exec_jmp(lbl, lnm):
    dest = labels.get(lbl)
    if dest == None:
        raise RuntimeError("INVALID VALUE: " + str(lbl) + " at line " + str(lnm))
    print("jump to " + str(lbl) + " -> from line " + str(lnm) + " to line " + str(dest) + "\n")
    return dest-1

def exec_jmpf(cmpr, v1, v2, lbl, lnm):
    dest = labels.get(lbl)
    if dest == None:
        raise RuntimeError("INVALID VALUE: " + str(lbl) + " at line " + str(lnm))
    if v1[0] == "$":
        v1 = registers.get(v1[1:])
    try:
        v1 = int(v1)
    except:
        if v1[-1].lower() == "b":
            v1 = v1[:-1]
            v1 = int(v1, 2)
        else:
            raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    val2 = None
    if v2[0] == "$":
        val2 = registers.get(v2[1:])
    else:
        val2 = v2
    try:
        val2 = int(val2)
    except:
        if val2[-1].lower() == "b":
            val2 = val2[:-1]
            val2 = int(val2, 2)
        else:
            raise RuntimeError("INVALID VALUE: " + str(v1) + " at line " + str(lnm))
    print("jump to " + str(lbl) + " -> from line " + str(lnm) + " to line " + str(dest) + " IF " + str(v1) + " " + str(cmpr) + " " + str(val2) + "\n")
    command = "exec_cmp('" + str(cmpr) + "', '" + str(v1) + "', '" + str(val2) + "')"
    compareResult = int(eval(command))
    if compareResult:
        return dest-1
    else:
        return lnm

def exec_cmp(cmpr, v1, v2):
    command = "int(" + str(v1) + ") " + str(cmpr) + " int(" + str(v2) + ")"
    result = eval(command)
    print("compare " + str(v1) + " " + str(cmpr) + " " + str(v2) + " -> " + str(result) + "\n")
    return result

def code_parse(file):    
    inputcode = [x.strip() for x in file.split("\n")]

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
    evaluate_code(lineTokens, maxLineNum)
    print("<> CODE EXECUTED SUCCESSFULLY <>")
    print("")
    print("<> OUTPUT VALUES <>")
    print(registers.get("out"))
    tmp = registers.get("out")
    registers['out'] = []
    return tmp

# main()
