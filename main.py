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

    def getc(self):
        self.ch = sys.stdin.read(1)

    def next_token(self):
        self.value = None
        self.sym = None
        while self.sym == None:
            if len(self.ch) == 0:
                self.sym == Lexer.EOF
            elif self.ch.isspace():
                self.getc()
            elif self.ch.isdigit():
                intval = 0
                while self.ch.isdigit():
                    intval = intval * 10 + int(self.ch)
                    self.getc()
                self.value = intval
                self.sym = Lexer.NUM

            elif self.sym.isalpha():
                ident = ' '
                while self.ch.isalpha():
                    ident = ident + self.ch.lower()
                    self.getc
                if ident in Lexer.WORDS:
                    self.sym = Lexer.WORDS[ident]
                elif len(ident) == 1:
                    self.sym == Lexer.ID
                    self.value = ord(ident) - ord("a")
                else:
                    self.error("Unknow identifier")
            else:
                self.error("Unxpected symbol: " + self.ch)
