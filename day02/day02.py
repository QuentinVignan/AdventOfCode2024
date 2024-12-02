def read_file(path):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            line = line.replace('\n' , '')
            lines.append(line)

    return lines


def detect_safe_simple(num_list):
    inc_dec = False # true: increase false:decrease
    first_check = False
    select = None
    for n in num_list:
        if select == None:
            select = int(n)
        else:
            if select == int(n):
                return False
            if select > int(n) and first_check == False:
                inc_dec = True
                first_check = True
            elif select < int(n) and first_check == False:
                inc_dec = False
                first_check = True
            if inc_dec == True:
                if select < int(n):
                    return False
                if (select - int(n)) >= 4:
                    return False
            if inc_dec == False:
                if select > int(n):
                    return False
                if (int(n) - select) >= 4:
                    return False
            select = int(n)
    return True

def get_safe_suite_simple(lines):
    index = 0
    size_of_lines = 0
    result = 0
    for line in lines:
        line_split = line.split(" ")
        if detect_safe_simple(line_split) == True:
            result += 1
    return result


lines_list = read_file("./sample_exo_one.txt")
print (" day02 ( first star ) result : " + str(get_safe_suite_simple(lines_list)))

