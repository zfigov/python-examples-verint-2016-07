"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""

lower_keys = [chr(lc) for lc in range(255) if (chr(lc)).islower()]

