import sys
import re

def main():
    if len(sys.argv) < 2:
        return -1
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    in_python = False
    variables = {}
    for line in lines:
        if not in_python:
            line = vars_to_value(line, variables)
        if re.match("SAY ", line.upper()):
            string = line[4:]
            if string[-1] == '\n':
                string = string[:-1]
            print(string)
        elif re.match("SET ", line.upper()):
            name_end = line[4:].index(' ') + 4
            name = line[4:name_end]
            if re.match(" TO ", line[name_end:].upper()):
                value = line[name_end + 4:]
            else:
                value = line[name_end + 1:]
            if value[-1] == '\n':
                value = value[:-1]
            nice = r"[^0-9\+\-\/\* ]"
            if re.search(nice, value):
                pass
            else:
                value = eval(value)
                variables[name] = value
        elif re.match("PYTHON", line.upper()):
            if in_python:
                exec(py_code[py_code.index('\n'):])
            py_code = ""
            in_python = not in_python
        if in_python:
            py_code = py_code + line
def vars_to_value(string, variables):
    try:
        var_finder = r"var\([a-zA-Z]+\)"
        var = re.search(var_finder, string)
        finished = string
        while var:
            str_var = finished[var.start():var.end()]
            finished = re.sub(re.escape(str_var), str(variables[str_var[4:-1]]), finished)
            var = re.search(var_finder, finished)
    except KeyError:
        ty, val, trace = sys.exc_info()
        print(f"Unkown Variable: {val}")
        exit()
    return finished
if __name__ == "__main__":
    main()
