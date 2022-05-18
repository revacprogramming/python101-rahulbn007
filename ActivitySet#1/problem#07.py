
text = "X-DSPAM-Confidence:    0.8475"
h=text.find('0.8475')
x=float(text[h:])
print(x)