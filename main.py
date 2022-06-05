import sys
import re

def main():
    if len(sys.argv) < 2:
        return -1
    variables = {}
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    for line in lines:
        if re.match("SAY ", line.upper()):
            string = line[4:]
            if string[-1] == '\n':
                string = string[:-1]
            var_finder = r"var\([a-zA-z]+\)"
            var = re.search(var_finder, string)
            while var:
                str_var = string[var.start():var.end()]
                string = re.sub(re.escape(str_var), variables[str_var[4:-1]], string)
                var = re.search(var_finder, string)
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
            try:
                value = float(value)
            except:
                pass
            variables[name] = value
if __name__ == "__main__":
    main()
