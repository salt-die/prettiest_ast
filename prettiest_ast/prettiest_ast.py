from ast import AST, parse, iter_fields, iter_child_nodes, Load, Store, Delete
import re

NAME_RE = re.compile('[.]([A-Za-z]+)[ ]')
STYLES = {
    'light': ('├─', '│ ', '╰─','  '),
}
CONTEXTS = Load, Store, Delete

def snake(head, tail, text):
    first, *rest = text
    yield head + first
    yield from (tail + line for line in rest)

def stringify(node, skip_contexts, *prefixes):
    fields = ', '.join(f'{fieldname}={value!r}' for fieldname, value in iter_fields(node) if fieldname in ('id', 'value') and not isinstance(value, AST))
    yield f'{type(node).__name__}' + (f'({fields})' if fields else '')

    HEAD, TAIL, LAST_HEAD, LAST_TAIL = prefixes

    children = list(child for child in iter_child_nodes(node) if not skip_contexts or not isinstance(child, CONTEXTS))
    if not children:
        return

    if len(children) > 1:
        *rest, last = children
        for child in rest:
            yield from snake(HEAD, TAIL, stringify(child, skip_contexts, *prefixes))
    else:
        last, = children

    yield from snake(LAST_HEAD, LAST_TAIL, stringify(last, skip_contexts, *prefixes))

def format_ast(code, indent=4, style='light', skip_contexts=True):
    """Returns a string of the parsed code as a nicely formatted tree.
    """
    prefixes = (line + continuation * (indent - 1) for line, continuation in STYLES[style])
    return '\n'.join(stringify(parse(code), skip_contexts, *prefixes))

def pp_ast(code, indent=4, style='light', skip_contexts=True):
    """Prints `format_ast(code, indent)`
    """
    print(format_ast(code, indent, style))
