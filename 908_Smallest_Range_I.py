def solution(A, K):

    # ********** Attempt 2 - 2019/09/17  **********

    min_num = min(A)
    max_num = max(A)
    
    result = max_num - min_num - 2 * K
    
    if result > 0:
        return result
    else:
        return 0


    # ********** Attempt 1 - 2019/09/17  **********
       
    # if A:
    #     min = max = A[0]
    #     for i in A:
    #         if i > max:
    #             max = i
    #         elif i < min:
    #             min = i
    #     result = max - min - 2 * K
    #     if result > 0:
    #         return result
    #     else:
    #         return 0
    # else:
    #     return 0

if __name__ == "__main__":
    assert(solution([1], 0) == 0)
    assert(solution([0, 10], 2) == 6)
    assert(solution([1, 3, 6], 3) == 0)