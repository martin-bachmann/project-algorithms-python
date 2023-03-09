def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    merge_sort_string(first_list)
    merge_sort_string(second_list)

    sorted_first_string = "".join(first_list)
    sorted_second_string = "".join(second_list)

    is_valid = first_list == second_list and len(first_list) != 0

    return (
        sorted_first_string,
        sorted_second_string,
        is_valid,
    )


def merge_sort_string(string, start=0, end=None):
    if end is None:
        end = len(string)

    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort_string(string, start, mid)
        merge_sort_string(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1
