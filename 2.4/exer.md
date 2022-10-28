## 2.4.1

```
void match(terminal t) {
    if ( lookahead == t) lookahead = nextTerminal;
    else report("syntax error");
}
```

a) S -> + S S | - S S | a

```
void S() {
    switch (lookahead) {
    case +:
        match(+); S (); S(); break;
    case -:
        match(-); S (); S(); break;
    case a:
        match(a); break;
    default:
        report("syntax error");
    }
}
```

b) S -> S ( S ) S | ε

```
void S() {
    switch (lookahead) {
    case '(':
        match('('); S(); match(')'); S(); break;
    default:
        report("syntax error");
    }
}
```

c)  S -> 0 S 1 | 0 1

```
void S() {
    switch (lookahead) {
    case 0:
        match(0);
        if (lookahead == 1) {
            match(1);
        } else {
            S(); match(1);
        }
        break;
    default:
        report("syntax error");
        
    }
}
```
