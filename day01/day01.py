
def read_file(path):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line)
    return lines

def get_left_list(lines):
    left_list = []
    for line in lines:
        split_line  = line.split(" ")
        left_list.append(int(split_line[0]))
    return left_list

def get_right_list(lines):
    right_list = []
    for line in lines:
        split_line = line.split(" ")
        right_list.append(int(split_line[len(split_line) - 1].replace('\n' , '')))
    return right_list

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def get_distance_simple(left_list , right_list):
    result = 0
    index = 0
    for r in right_list:
        if left_list[index] < r:
            result = result + (r - left_list[index])
        elif left_list[index] > r:
            result = result + (left_list[index] - r)
        else:
            result = result + 0
        index += 1
    return result

def get_distance_hard(left_list ,right_list , size_of):
    loop_left_list = left_list
    select_number_left = 0
    right_same_number = 0
    result = 0
    for l in left_list:
        left_same_number = 0
        right_same_number = 0
        select_number_left = l
        for r in right_list:
            if select_number_left == r:
                right_same_number += 1
#        print("select : " + str(select_number_left) + " right_same : " + str(right_same_number) + " result : " + str(select_number_left * right_same_number))
        result = result + (select_number_left * right_same_number)
        
    return result

lines_list = read_file("./sample_exo_one.txt")
left_list_unsort = get_left_list(lines_list)
right_list_unsort = get_right_list(lines_list)
left_list_sort = bubble_sort(left_list_unsort)
right_list_sort = bubble_sort(right_list_unsort)

print("day01 ( fisrt start ) result : " + str(get_distance_simple(left_list_sort , right_list_sort)))

lines_list = read_file("./sample_exo_two.txt")
left_list_unsort = get_left_list(lines_list)
right_list_unsort = get_right_list(lines_list)

print("day01 ( second start ) result : " + str(get_distance_hard(left_list_unsort , right_list_unsort , len(left_list_sort))))

