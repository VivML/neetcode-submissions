class Solution(object):

  def isValid(self, s):
    """:type s: str

    :rtype: bool
    """
    # Early exit: odd length strings can't be balanced
    if len(s) % 2 != 0:
      return False

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Pop top character if stack isn't empty, else assign a dummy character
        top_element = stack.pop() if stack else "#"

        # Check if the closing bracket matches the last opening bracket
        if mapping[char] != top_element:
          return False
      else:
        # Push opening bracket onto the stack
        stack.append(char)

    # Valid if no unmatched opening brackets remain
    return not stack       