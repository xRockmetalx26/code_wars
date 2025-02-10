def mirror(input_list: list[float]):
    output_list = sorted(input_list)
    return output_list + output_list[-2::-1]

test = [-5, 10, 8, 10, 2, -3, 10]

print(mirror(test))
