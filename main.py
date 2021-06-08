# Dennis Matveev
# Comp 340
import lexer
import parserr
import evaluator
import decipher

print("\nHello baby language.\nEnter baby exp and see what you get.")
while True:
    baby_exp = input(">>> ")
    if baby_exp == "poopoo":
        break
    srcCode = decipher.decipher(baby_exp)
    print("Interpreted as: ", srcCode)
    tokSeq = lexer.tokenize(srcCode)
    new_tok_seq = lexer.check_negatives(tokSeq)
    rootNode = parserr.parse(new_tok_seq)
    result = evaluator.evaluate(rootNode)
    print("The result is: ", result)
print("Now it is time to go poo poo.")


