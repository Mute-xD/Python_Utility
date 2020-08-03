
def finding(spaces):
    if spaces[0] == [1]:
        return spaces[0]
    elif spaces[0] == 0 or spaces[1] == 0:
        return max(spaces)
    else:
        if spaces[0] < spaces[1]:
            spaces[1] %= spaces[0]
        else:
            spaces[0] %= spaces[1]
        return finding(spaces)


print(finding([1680, 640]))
