class Lexer:
    NUM, ID, IF, ELSE, WHILE, ASSIG, LBRA, RBRA, \
    MINUS, PLUS, SEMICOLON, EOF = range(12)

    #специальные символы
    SYMBOLS = { '(' : LBRA,
                ')' : RBRA,
                '+' : PLUS,
                '-' : MINUS,
                ';' : SEMICOLON,
                '=' : ASSIG}

    #Ключивые слова
    WORDS = {'if' : IF,
             'else' : ELSE,
             'while' : WHILE}

    ch = ' '

    def error(self):
        print('Lexer error'), msg
        sys.exit

    def getf(self):
        self.ch = sys.stdin.read(1)

    def next_token(self):
        self.value = None
        self.sim = None
