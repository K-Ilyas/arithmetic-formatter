import re


def arithmetic_arranger(arithmetics, show=False):
    table = list()
    if len(arithmetics) > 5:
        return "Error: Too many problems."

    for arithmetic in arithmetics:

        fragments = arithmetic.split()
        # print(fragments)
        if re.search('^[^\+\-]+$', fragments[1]):
            return "Error: Operator must be '+' or '-'."
        elif re.search('\D+', fragments[0]) or re.search('\D+', fragments[2]):
            return "Error: Numbers must only contain digits."
        elif len(fragments[0]) > 4 or len(fragments[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        dictionary = dict()
        dictionary['sup'] = fragments[0]
        dictionary['sub'] = fragments[2]
        dictionary['opertaor'] = fragments[1]
        dictionary['max'] = max(len(fragments[0]), len(fragments[2]))

        table.append(dictionary)

    # show calcutaions sup:
    sup = ''
    sub = ''
    sep = ''
    result = ''
    for opt in range(len(table)):
        opertaion = table[opt]
        space = ("" if opt == len(table) - 1 else " "*4)
        convention = "{:"+str(opertaion["max"])+"d}"
        sup = sup + " "*2 + \
            convention.format(int(opertaion['sup'])) + space
        sub = sub + opertaion["opertaor"] + " " + \
            convention.format(int(opertaion['sub'])) + space
        sep = sep + "-"*(int(opertaion["max"])+2) + space
        finalresult = eval(
            opertaion['sup']+opertaion['opertaor']+opertaion['sub'])
        result = result + " "*(opertaion["max"]+2-len(str(finalresult))) + \
            convention.format(
                finalresult) + space

    final = sup + "\n" + sub + "\n" + sep
    if show:
        final = final + "\n" + result

    return final


print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))
