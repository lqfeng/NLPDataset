import numpy as np
def export_trimmed_glove_vectors(vocab, glove_filename, trimmed_filename, dim):
    """Saves glove vectors in numpy array

    Args:
        vocab: dictionary vocab[word] = index
        glove_filename: a path to a glove file
        trimmed_filename: a path where to store a matrix in npy
        dim: (int) dimension of embeddings

    """
    embeddings = np.zeros([len(vocab), dim])
    with open(glove_filename) as f:
        for line in f:
            line = line.strip().split(' ')
            word = line[0]
            embedding = [float(x) for x in line[1:]]
            if word in vocab:
                word_idx = vocab[word]
                embeddings[word_idx] = np.asarray(embedding)

    np.savez_compressed(trimmed_filename, embeddings=embeddings)

ch = []
VOCAB_MIN_COUNT=100
for line in open("AlphabetDigitPunctuationCharacters.txt"):
    if line.strip():
        ch.append(line.strip())

for line in open("GeneralStandardChineseCharacters.txt"):
    if line.strip():
        ch.append(line.strip().split()[1])

vector_dict={}
for line in open("glove_embedings/glove_zhwiki_char_embedings.txt"):
    char = line.strip().split()[0]
    vector_dict[char]=line

vector_count={}
for line in open("glove_embedings/vocab.txt"):
    char, count = line.split(" ", 1)
    vector_count[char]=count.strip()

vector_fp=open("embeddings.txt","w")
vocab_fp=open("vocab.txt","w")
vocab_cnt_fp=open("vocab_cnt.txt","w")
vector_fp.write("<pad> " + " ".join(["0.0"] * 100) + "\n")
vocab_fp.write("<pad>\n")
vocab_cnt_fp.write("<pad>\t0\n")
vocab_list = []
vocab_list.append("<pad>")
for char in ch:
    if char in vector_dict and (int(vector_count.get(char,"0")) >= VOCAB_MIN_COUNT or char=="<unk>"):
        vector_fp.write(vector_dict[char])
        vocab_fp.write(char + "\n")
        vocab_list.append(char)
        vocab_cnt_str = char + "\t" + vector_count.get(char,"0")+ "\n"
        vocab_cnt_fp.write(vocab_cnt_str);
        vector_count[char] = "skip"

fp=open("exclude_char.txt","w")
for k, v  in vector_count.items():
    if v != "skip":
        fp.write(k + "\t" + v+"\n")

print(len(vocab_list))
export_trimmed_glove_vectors({char:idx for idx, char in enumerate(vocab_list)}, "embeddings.txt", "embeddings.npz", 100)
#vector_dict={}
#for line in open("glove_alinlp_zhwiki_char_vectors.txt"):
#    char = line.strip().split()[0]
#    vector_dict[char]=line
#
#
#vector_fp=open("StandardChineseCharactersEmbeddings.txt","w")
#vocab_fp=open("vocab.txt","w")
#vector_fp.write("<pad> " + " ".join(["0.0"] * 100) + "\n")
#vocab_fp.write("<pad>\n")
#for char in ch:
#    if char in vector_dict:
#        vector_fp.write(vector_dict[char])
#        vocab_fp.write(char + "\n")
#        #print(line.strip())
#    else:
#        print(char)
#
