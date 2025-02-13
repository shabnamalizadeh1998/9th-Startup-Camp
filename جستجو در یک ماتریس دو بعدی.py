def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


def get_input():
    matrix = []
    print("Please enter the matrix (enter each row on a new line and enter a blank line to finish):")
    while True:
        row = input()
        if row == "":
            break
        matrix.append(list(map(int, row.split())))
    
    target = int(input("Please enter the target value: "))
    return matrix, target

matrix, target = get_input()
result = searchMatrix(matrix, target)
print("OUTPUT:", result)
