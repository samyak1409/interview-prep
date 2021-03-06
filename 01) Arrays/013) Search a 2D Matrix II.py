"""
https://leetcode.com/problems/search-a-2d-matrix-ii
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """"""

    # 0) Brute-force (Linear Search): TC = O(m*n); SC = O(1)

    """
    for row in matrix:
        if target in row:
            return True
    return False  # if target is not found above
    """

    # 1) Optimal (Like a BST): TC = O(m+n); SC = O(1)
    # https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution
    # https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66139/C%2B%2B-search-from-top-right
    # Why are we starting from top-right corner only?
    # Because we need to start from a corner from where one side is ascending and the other descending, why?
    # Because otherwise we will not know in which direction to go if "target" is greater/lesser than both the elements of both direction.
    # You guessed right! We can also start from bottom-left corner.

    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1  # top-right corner
    while i < m and j >= 0:  # while both the indices are in bound
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1  # move down
        else:  # (if matrix[i][j] > target)
            j -= 1  # move left
    return False

    # Note: This same algo can also be applied to https://leetcode.com/problems/search-a-2d-matrix. (Though it can be better solved by Finding the Target Row + Linear Search)
