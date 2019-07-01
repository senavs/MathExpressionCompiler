# MathExpressionCompiler

<p align="center">
  <img src="http://robertjacobson.herokuapp.com/blogimages/MathGrammar/simple_parse_tree.png" width=250>
</p>

## How does it work?
&nbsp; Before I tell you how **compilers** **read** and **solve** mathematical expressions, there are things that you must know.
- Yours math expressions are called **infix expressions**.
  - *mx+b*
- Compilers can only read **postfix expressions**.
  - _mx*b+_  

&nbsp; So, compilers do not read mathematical expressions like we do.
They first change an **infix** to a **postfix** expression and then, evaluate it.
Some compilers do this two steps at the same time. To return the expression answer, 
[Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) and 
[Stack](https://github.com/senavs/AbstractDataTypes/tree/master/stack) are used during the process.  
&nbsp; The English Algorithm can be seen [here](http://personal.denison.edu/~havill/algorithmics/algs/postfix.pdf).

## How to use MathExpressionsCompiler functions
**Import**
``` python
from MathExpressionCompiler import to_postfix, evaluate
```
###### NOTE: My [Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) and [Stack](https://github.com/senavs/AbstractDataTypes/tree/master/stack) [AbstractDataTypes](https://github.com/senavs/AbstractDataTypes) are needed at the same [MathExpressionCompiler](https://github.com/senavs/MathExpressionCompiler) path

**Infix to Postfix expression**
``` python
infix_01 = 'a - b'
print(f'>> {to_postfix(infix_01)}')
# >> a b -

infix_02 = 'a - b * c'
print(f'>> {to_postfix(infix_02)}')
# a b c * -

infix_03 = '( a - b ) * c'
print(f'>> {to_postfix(infix_03)}')
# >> a b - c *

infix_04 = 'a + b * c ** d - e'
print(f'>> {to_postfix(infix_04)}')
# >> a b c d ** * + e -

infix_05 = 'a * ( b + c ) * ( d - g ) * h'
print(f'>> {to_postfix(infix_05)}')
# >> a b c + * d g - * h *

infix_06 = 'a * b - c * d ** e / f + g * h'
print(f'>> {to_postfix(infix_06)}')
# >> a b * c d e ** * f / - g h * +
```

**Evaluate the postfix expression**
``` python
print(f'>> {evaluate("8 7 2 * -")}')
# >> -6
```

**Evaluate the postfix expression with variables**
``` python
variables = {'a': 8, 'b': 7, 'c': 2}
print(f'>> {evaluate("a b c * -", variables)}')
# >> -6
```

