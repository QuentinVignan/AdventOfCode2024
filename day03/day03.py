import re 

def read_file(path):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            line = line.replace('\n' , '')
            lines.append(line)
    return lines

def search_simple(lines):
    pattern = r"mul\((\d+),(\d+)\)"
    result = 0
    for l in lines:
        result_parttern_list = re.findall(pattern , l)
        for x in result_parttern_list:
            result = result + (int(x[0]) * int(x[1]))
    return result

def search_hard(lines):
    pattern = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"
    result = 0
    do = False
    dont = False
    for l in lines:
        result_parttern_list = re.findall(pattern , l)
        for x in result_parttern_list:
            if do == True and x[2] != '' and x[3] != '':
                result = result + (int(x[2]) * int(x[3]))                
            if x[1] == "do()" or x[0] == "do()" and x[2] == '' and x[3] == '':
                do = True
                dont = False
            elif x[1] == "don't()" or x[0] == "don't()" and x[2] == '' and x[3] == '':
                do = False
                dont = True
            if do == False and dont == False and x[2] != '' and x[3] != '':
                result = result + (int(x[2]) * int(x[3]))
    return result

lines_list = read_file("./sample_exo_one.txt")
print (" day03 ( first star ) result : " + str(search_simple(lines_list)))
lines_list = read_file("./sample_exo_two.txt")
print (" day03 ( second star ) result : " + str(search_hard(lines_list)))


