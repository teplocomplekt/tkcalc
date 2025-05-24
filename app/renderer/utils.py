PT2MM = 1 / 72 * 25.4
MM2PT = 72 / 25.4


class PaperSize:
    A4_PORTRAIT = (210, 297)
    A4_LANDSCAPE = (297, 210)

    @staticmethod
    def get_paper_in_pt(size: tuple):
        return map((lambda x: x * MM2PT), size)


class LineWidth:
    BOLD = 1
    MEDIUM = 0.6
    THIN = 0.18


class Color:
    BLACK = (0.0, 0.0, 0.0)
    WHITE = (1.0, 1.0, 1.0)
    CUSTOM = (0.9, 0.9, 0.8)


def matrix_multiplication(A, B):
    # Determine the matrices' dimensions.

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    # Установить матрицу результатов в нули.
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]
    # Iterate through rows of A
    for s in range(rows_A):
        # Iterate through columns of B
        for j in range(cols_B):
            # Iterate through rows of B
            for k in range(cols_A):
                result[s][j] += A[s][k] * B[k][j]
    return result


# from typing import List
#
#
# def vec_product(vec1: List[float], vec2: List[float]) -> float:
#     return sum([int(x * y) for x, y in zip(vec1, vec2)])
#
#
# def matrix_transpose(mat: List[List]) -> List[List]:
#     return [*map(list, zip(*mat))]
#
#
# def matrix_product(mat1: List[List[float]], mat2: List[List[float]]):
#     l, n = len(mat1), len(mat2[0])
#     ans = [[0 for i in range(n)] for j in range(l)]
#     for i in range(l):
#         for j in range(n):
#             vec1 = mat1[i]
#             vec2 = matrix_transpose(mat2)[j]
#             ans[i][j] = vec_product(vec1, vec2)
#     return ans
