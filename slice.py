# using find() and string slicing to extract the number at the end and convert it to a float value

text = "X-DSPAM-Confidence:    0.8475"

"""
l = text.find("0")
print(l)
"""

print(float(text[23:]))
