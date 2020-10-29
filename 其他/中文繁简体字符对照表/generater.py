ch = []
for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/other.txt"):
    if line.strip():
        ch.append(line.strip())
for line in open("/Users/fengliqiang/Downloads/NLPDataSet/中文繁简体字符对照表/zh.txt"):
    if line.strip():
        if int(line.strip().split()[0]) > 5000:
            break
        ch.append(line.strip().split()[1])



vector_dict={}
for line in open("glove_alinlp_zhwiki_char_vectors.txt"):
    char = line.strip().split()[0]
    vector_dict[char]=line


vector_fp=open("glove_zhwiki_char_vectors.txt","w")
vocab_fp=open("vocab.txt","w")
vector_fp.write("<pad> " + " ".join(["0.0"] * 100) + "\n")
vocab_fp.write("<pad>\n")
for char in ch:
    if char in vector_dict:
        vector_fp.write(vector_dict[char])
        vocab_fp.write(char + "\n")
        #print(line.strip())
    else:
        print(char)

