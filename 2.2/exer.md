## 2.2.1

S -> S S + <!-- 1 -->
S -> S S * <!-- 2 -->
S -> a     <!-- 3 -->

a) for a string: `aa+a*`,

```
a is S by production 3,
aa+ is S by production1, since a is S
aa+a* is SS* by production 2, since aa+ is S and a is S
```

c) L = repeat { one or many a(s) optionally followed by + or * }

## 2.2.2


a) L = N 0s followed by N 1s, where N >= 1

b)

c) L = valid parentheses

d) L = Full permutation of N As and N Bs, where N >= 1

e)

## 2.2.3

e is ambiguous

## 2.2.4

**Terminals are expressed in quotes.**

a)

S -> S S op

S -> digit

op -> "+"|"-"|"*"|"/"

e.g.

12+

123+-

b)

S -> S,"id" | "id"

e.g.

a

a,b,c,d

c)

S -> "id",S | "id"

e.g.

a

(a,(b,(c,(d))))


d)

S -> S operator operand

operator -> "+"|"-"|"*"|"/"

operand -> "id" | "digit"

e.g.

a + 1

2 - b + a

e)

+a - 1

-2 - b + a 
