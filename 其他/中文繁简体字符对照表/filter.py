ch = {}
for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/zh.txt"):
    if line.strip():
        if int(line.strip().split()[0]) > 5000:
            break
        ch[line.strip().split()[1]] = 1

for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/other.txt"):
    if line.strip():
        ch[line.strip()] = 1

#for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/ch.txt"):
#    if line.strip():
#        ch[line.strip()] = 1
#
#for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/cht_tw.txt"):
#    if line.strip():
#        ch[line.strip()] = 1
#
#for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/cht_cn.txt"):
#    if line.strip():
#        ch[line.strip()] = 1

filter_vector=open("glove_alinlp_zhwiki_char_vectors.txt.filter","w")
for line in open("glove_alinlp_zhwiki_char_vectors.txt"):
    char = line.strip().split()[0]
    if char in ch:
        filter_vector.write(line)
        #print(line.strip())
    #else:
        #print(line.strip())

