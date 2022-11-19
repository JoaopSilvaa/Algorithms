def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) != 0:
        second_string_letters = list(second_string.lower())
        sorted_second_string = merge_sort(second_string_letters, 0, len(second_string_letters))
        return (first_string, sorted_second_string, first_string == sorted_second_string)

    elif len(second_string) == 0 and len(first_string) != 0:
        first_string_letters = list(first_string.lower())
        sorted_first_string = merge_sort(first_string_letters, 0, len(first_string_letters))
        return (sorted_first_string, second_string, sorted_first_string == second_string)

    elif len(second_string) == 0 and len(first_string) == 0:
        return (first_string, second_string, False)

    else:
        first_string_letters = list(first_string.lower())
        sorted_first_string = merge_sort(first_string_letters, 0, len(first_string_letters))

        second_string_letters = list(second_string.lower())
        sorted_second_string = merge_sort(second_string_letters, 0, len(second_string_letters))
        return (sorted_first_string, sorted_second_string, sorted_first_string == sorted_second_string)

def merge_sort(letters, start=0, end=None):
    if end is None:
        end = len(letters)
    if (end - start) > 1: 
        mid = (start + end) // 2 
        merge_sort(letters, start, mid) 
        merge_sort(letters, mid, end)
        merge(letters, start, mid, end) 
    
    new_string = "".join(letters)
    return new_string

def merge(numbers, start, mid, end):
    left = numbers[start:mid] 
    right = numbers[mid:end] 

    left_index, right_index = 0, 0 

    for general_index in range(start, end): 
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
