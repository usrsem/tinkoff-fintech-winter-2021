n = int(input())
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]

current_height: int = 0
jumps_count: int = 0

while current_height < n:
    length_to_top = n - current_height
    current_max_jump = a[length_to_top - 1]

    min_fall = b[length_to_top - current_max_jump - 1]
    best_jump = current_max_jump

    for jump in range(current_max_jump-1, -1, -1):
        new_fall = b[length_to_top - jump - 1]

        if best_jump - min_fall < jump - new_fall:
            min_fall = new_fall
            best_jump = jump

    current_height += best_jump - min_fall
    jumps_count += 1

    if current_height == n:
        print(jumps_count)
        break

    if best_jump == min_fall:
        print(-1)
        break

