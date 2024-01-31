code_word = input()

move = code_word[0:2]
decrypt = code_word.replace(move, '') + move
print(decrypt)
