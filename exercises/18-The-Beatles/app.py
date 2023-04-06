# Your code here!!
# song= ['let it be', 'let it be', 'let it be', 'let it be', 'whisper words of wisdom', 'let it be', 'let it be', 'let it be', 'let it be', 'let it be', 'there will be an answer', 'let it be']

def sing():
    for n in range(0, 11):
        if n < 4:
            print('Let it be, ')
        if n == 5:
            print('whisper words of wisdom,'+ str(n))
        if n == 9:
            print('there will be an answer'+ str(n))
        else: print('let it be'+ str(n))

sing()