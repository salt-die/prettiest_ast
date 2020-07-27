# prettiest_ast

A simple pretty printer for python abstract syntax trees:

```py
>>> from prettiest_ast import ppast
>>> ppast('for i in range(5): print(i)')

For
├──Name
│  ├──i
│  ╰──Store
├──Call
│  ├──Name
│  │  ├──range
│  │  ╰──Load
│  ╰──Constant
│     ╰──5
╰──Expr
   ╰──Call
      ├──Name
      │  ├──print
      │  ╰──Load
      ╰──Name
         ├──i
         ╰──Load
```