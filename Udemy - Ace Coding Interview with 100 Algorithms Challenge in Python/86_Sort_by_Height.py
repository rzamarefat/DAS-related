def sort_by_height(array):
    non_tree_elements = sorted([a for a in array if a != -1])

    sorted_array = []
    counter = 0
    for a in array:
        if a == -1:
            sorted_array.append(a)
        else:
            sorted_array.append(non_tree_elements[counter])
            counter +=1 
    return sorted_array

if __name__ == "__main__":
    res = sort_by_height([-1, 190, 150, -1, 180, -1])

    print(res)