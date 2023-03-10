def find_duplicate(nums):
    try:
        sort_nums(nums)
    except ValueError:
        return False

    prev_num = -1
    for num in nums:
        if num == prev_num:
            return num
        prev_num = num
    return False


def sort_nums(nums):
    if (not nums) or (len(nums) < 2):
        raise ValueError("inválido")

    for num in nums:
        if type(num) == str or num < 0:
            raise ValueError("inválido")

    merge_sort(nums)


def merge_sort(nums, start=0, end=None):
    if end is None:
        end = len(nums)

    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid, end)
        merge(nums, start, mid, end)


def merge(nums, start, mid, end):
    left = nums[start:mid]
    right = nums[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            nums[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            nums[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            nums[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            nums[general_index] = right[right_index]
            right_index = right_index + 1
