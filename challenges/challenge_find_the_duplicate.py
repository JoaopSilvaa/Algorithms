def find_duplicate(nums):
    if len(nums) == 0:
        return False
    elif type(nums) != list:
        return False
    else:
        nums.sort()
        return verify_duplicate(nums)


def verify_duplicate(nums):
    duplicate = False
    for index in range(len(nums)):
        if index + 1 == len(nums):
            break
        elif not verify_number(nums[index]):
            duplicate = False
            break
        elif nums[index] == nums[index + 1]:
            duplicate = nums[index]
            break
    return duplicate


def verify_number(number):
    if type(number) != int:
        return False

    elif number < 0:
        return False

    else:
        return True
