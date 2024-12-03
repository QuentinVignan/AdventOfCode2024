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

def is_safe(report):
    is_increasing = True
    is_decreasing = True
    for i in range(len(report) - 1):
        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3:
            return False, False
        if report[i+1] < report[i]:
            is_increasing = False
        if report[i+1] > report[i]:
            is_decreasing = False
    return is_increasing, is_decreasing

def is_safe_with_one_removal(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        is_increasing, is_decreasing = is_safe(new_report)
        if is_increasing or is_decreasing:
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        report = list(map(int, report.split()))
        is_increasing, is_decreasing = is_safe(report)
        if is_increasing or is_decreasing:
            safe_count += 1
        else:
            if is_safe_with_one_removal(report):
                safe_count += 1
    return safe_count


lines_list = read_file("./sample_exo_one.txt")
print (" day02 ( first star ) result : " + str(get_safe_suite_simple(lines_list)))
lines_list = read_file("./sample_exo_two.txt")
print (" day02 ( second star ) result : " + str(count_safe_reports(lines_list)))

