def count_rides(people, length, weight):
    people.sort()
    count = 0
    first_pos = 0
    second_pos = length -1
    if people[second_pos] > weight:
        print("error, some people cant enter the elevator due to overweight")
    while first_pos < second_pos:
        temp = people[second_pos]
        while people[first_pos] + temp <= weight:
            temp += people[first_pos]
            first_pos += 1
        count += 1
        second_pos += -1
    print(count)

num_people, weight = map(int, input().split())
people = [int(x) for x in input().split(' ')]
count_rides(people, num_people, weight)