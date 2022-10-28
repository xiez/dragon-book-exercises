def parse1(string):
    cur, length = 0, len(string)

    def match(terminal):
        nonlocal cur
        if terminal == string[cur]:
            cur += 1
            print(f'match {terminal}, updated cur to {cur}')
        else:
            raise SyntaxError(f"unexpected token {string[cur]}")

    def assert_not_reach_end():
        if cur >= length:
            raise SyntaxError("string reaches end")

    def lookahead():
        try:
            return string[cur]
        except IndexError:
            raise SyntaxError("string reaches end")

    def S():
        while True:
            if cur >= length:
                break

            if lookahead() == '+':
                match('+')
                assert_not_reach_end()
                S()
                assert_not_reach_end()
                S()
                continue
            elif lookahead() == '-':
                match('-')
                S()
                S()
                continue
            elif lookahead() == 'a':
                match('a')
                continue
            else:
                raise SyntaxError(f"unexpected token {string[lookahead]}")

    S()

def parse2(string):

    tokens = [s for s in string.strip()]
    print(f'tokens: {tokens}')

    def lookahead():
        return tokens[0]

    def move_ahead():
        tokens.pop(0)

    def S():
        if lookahead() == '+':
            move_ahead()
            S()
            S()
        elif lookahead() == 'a':
            move_ahead()
        else:
            raise SyntaxError(f"unexpected token")

    S()


# print('Grammer: S -> + S S | - S S | a')
# for s in ['a', 'aa', '+aa', '+a+a']:
#     print(f'parse string: {s} ...')
#     parse1(s)
#     print(' ok')

parse2('a+')
