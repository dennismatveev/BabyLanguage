class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


def tokenize(srs_code):
    tok_seq = []
    # blah blah blah
    while srs_code != "":
        char = srs_code[0]
        if char == "+":
            new_token = token("PLUS", char)
            tok_seq.append(new_token)
            srs_code = srs_code[1:]

        elif char == "-":
            new_token = token("MINUS", char)
            tok_seq.append(new_token)
            srs_code = srs_code[1:]

        elif char == "*":
            new_token = token("MULTIPLICATION", char)
            tok_seq.append(new_token)
            srs_code = srs_code[1:]
        elif char == "/":
            new_token = token("DIVISION", char)
            tok_seq.append(new_token)
            srs_code = srs_code[1:]
        elif char == "(":
            new_token = token("LPAREN", char)
            tok_seq.append(new_token)
            srs_code = srs_code[1:]
        elif char == ")":
            new_token = token("RPAREN", char)
            tok_seq.append(new_token)
            srs_code = srs_code[1:]

        elif char == " ":
            srs_code = srs_code[1:]

        elif char.isdigit():
            numb_str = ""
            while char.isdigit():
                numb_str += char
                srs_code = srs_code[1:]
                if srs_code == "":
                    char = ""
                else:
                    char = srs_code[0]
            new_token = token("NUMBER", numb_str)
            tok_seq.append(new_token)

    return tok_seq


def check_negatives(tok_seq):
    new = []
    special_case = \
        [token("LPAREN", '('), token("NUMBER", 0), token("MINUS", '-'), token("NUMBER", 1), token("RPAREN", ')'), token("MULTIPLICATION", '*')]
    for index, tok in enumerate(tok_seq):
        if tok.type == "MINUS" and (index == 0 or tok_seq[index-1].type != "NUMBER"):
            new.extend(special_case)
        else:
            new.extend([tok])
    return new
