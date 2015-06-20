def balancedParens(s):
  stack, opens, closes = [], ['(', '[', '{'], [')', ']', '}']
  for c in s:
    if c in opens:
      stack.append(c)
    elif c in closes:
      try:
        if opens.index(stack.pop()) != closes.index(c):
          return False
      except (ValueError, IndexError):
        return False
  return not stack