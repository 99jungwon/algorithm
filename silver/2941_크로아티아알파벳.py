word = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for ch in croatia:
    word = word.replace(ch, "*")

print(len(word))
