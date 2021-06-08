dictionary = {"pee": "+",
              "gah": "-",
              "milk": "*",
              "heh": "/",
              "mama": "(",
              "dada": ")",
              "baaaaaaaaa": 9,
              "baaaaaaaa": 8,
              "baaaaaaa": 7,
              "baaaaaa": 6,
              "baaaaa": 5,
              "baaaa": 4,
              "baaa": 3,
              "baa": 2,
              "ba": 1,
              "b": 0
              }


def decipher(baby_expression):
    src_code = ""
    split = baby_expression.split(" ")
    temp = []
    for element in split:

        if "b" in element:
            size = len(element)
            idx_list = [idx for idx, val in enumerate(element) if val == "b"]
            res = [element[i: j] for i, j in
                   zip([0] + idx_list, idx_list +
                       ([size] if idx_list[-1] != size else []))]
            temp.append(res)
        else:

            temp.append([element])
    for list in temp:
        for element in list:
            for value in dictionary:
                if value in element:
                    src_code = src_code + str(dictionary.get(value))
                    break

    return src_code
