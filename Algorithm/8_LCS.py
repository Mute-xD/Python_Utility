"""
最长公共子序列
比较两字符串相似度
"""

import numpy as np


def LCS(a_word, b_word):
    a_list = list(a_word)
    b_list = list(b_word)

    match_list = np.zeros((len(a_list), len(b_list)))

    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if a_list[i] == b_list[j]:
                if i == 0 or j == 0:
                    match_list[i][j] = 1
                else:
                    match_list[i][j] += (match_list[i-1][j-1] + 1)
            else:
                match_list[i][j] = max(match_list[i-1][j], match_list[i][j-1])
    return match_list


print(LCS('fish', 'dish'))
print(max(LCS('fish', 'dish').flat))  # 扁平化 取最值
