def description(list, bound):
    if list[0] > bound:
        return 0
    if len(list) < 2:
        return 1
    if list[1] != 0:
        if abs(list[0] - list[1]) < 2:
            return description(list[2:], bound)
        return 0 
    if list[1] == 0:
        new_list = list[1:]
        new_list[0] = list[0] - 1
        count = description(new_list, bound)
        new_list[0] += 1
        count += description(new_list, bound)
        new_list[0] += 1
        count += description(new_list, bound)
        return count

first, bound = map(int, input().split())
nums = [int(x) for x in input().split()]
print(description(nums, bound))