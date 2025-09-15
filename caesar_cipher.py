# 19. Caesar Cipher

cipher_key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s',
              'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
              'm':'z', 'n':'a','o':'b', 'p':'c', 'q':'d', 'r':'e',
              's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
              'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
              'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W',
              'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C',
              'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
              'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

text = input('Text: ')

encoded = []
for char in text:
    if not char.isalpha():
        encoded.append(char)
    else:
        encoded.append(cipher_key.get(char))

encoded = ''.join(encoded)
print(f'Encoded: {encoded}')

decoded = []
for char in encoded:
    if not char.isalpha():
        decoded.append(char)
    else:
        decoded.append(cipher_key.get(char))

decoded = ''.join(decoded)
print(f'Decoded: {decoded}')