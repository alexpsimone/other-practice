# anagram finder
# write a function that takes two strings and returns whether or not they are anagrams
# abc cab -> true
# abc abc -> true
# abc abd -> False
# '' '' -> True
# abc1 1abc -> True
# abcd abc -> False

# numbers and letters, no spaces, any length strings

def anagram(x, y):

    # if the strings are equal, return True
    if x == y:
        return True
    # if one of the strings is empty, return False
    if x == '' or y == '':
        return False
    # if len(x) != len(y), return False
    if len(x) != len(y):
        return False

    list_x = sorted(x)
    list_y = sorted(y)

    # loop through each index in x
    for idx in range(len(list_x)):
        if list_x[idx] != list_y[idx]:
            return False
    # see if list_x[idx] = list_y[idx]
    # if not equal, return False
    # return True
    return True


def anagram2(x, y):

    # if the strings are equal, return True
    if x == y:
        return True
    # if one of the strings is empty, return False
    if x == '' or y == '':
        return False
    # if len(x) != len(y), return False
    if len(x) != len(y):
        return False

    # initialize a dict for x
    x_dict = {}
    # initialize a dict for y
    y_dict = {}

    # loop through x
    for char in x:
    # if char in dict, increment value at char
        if char in x_dict:
            x_dict[char] += 1
        else:
            x_dict[char] = 1
    # otherwise, initialize a value dict[char]: 1

    # do the same things for y
    for char in y:
        if char in y_dict:
            y_dict[char] += 1
        else:
            y_dict[char] = 1

    # loop through each key in x dict
    for x_key in x_dict:
        # if key not in y_dict, return False
        if x_key not in y_dict:
            return False
        # elif dict[key] != dict[key] return False
        elif x_dict[x_key] != y_dict[x_key]:
            return False
            
    # else return True
    return True



if __name__ == '__main__':
    pass