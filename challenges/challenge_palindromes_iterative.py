def is_palindrome_iterative(word):
    high_index = len(word) - 1
    qtd_equals = 0
    for low_index in range(len(word)):
        if word[low_index] == word[high_index]:
            qtd_equals += 1
        if low_index >= high_index:
            break
        high_index = high_index - 1
    if qtd_equals == (len(word) // 2) + 1:
        return True
    else:
        return False
