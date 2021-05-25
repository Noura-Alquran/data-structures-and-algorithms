
def multi_bracket_validation(input):
    opening_brackets=['(','[','{']
    closing_brackets=[')',']','}']
    check_list = []
    for i in input:
        if i in opening_brackets:
            check_list.append(i)
        elif i in closing_brackets:
            pos = closing_brackets.index(i)
            if ((len(check_list) > 0) and
                (opening_brackets[pos] == check_list[len(check_list)-1])):
                check_list.pop()
            else:
                return  False
    if len(check_list) == 0:
        return True
    else:
        return False


