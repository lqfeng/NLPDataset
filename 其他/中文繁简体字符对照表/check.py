ch = {}
for line in open("zh.txt"):
    fields  = line.strip().split()
    num = int(fields[0])
    if num > 5000:
        break
    char = fields[1]
    ch[char] = 1

for line in open("chars.txt"):
    if line.strip() not in ch:
        print(line.strip())
