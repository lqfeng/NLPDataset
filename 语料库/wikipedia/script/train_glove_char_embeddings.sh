#!/bin/bash
set -e


#wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
#git clone https://github.com/attardi/wikiextractor.git
WIKI_SRC=../zhwiki-20200923-pages-articles.xml.bz2
pip install wikiextractor
python -m wikiextractor.WikiExtractor $WIKI_SRC --json  --processes 8  -o wikidata --filter_disambig_pages --lists
gsed  -i -e 's/BULLET::::-//g' -e  's/BULLET:::://g' wikidata/*/wiki_??
cat wikidata/??/* |python split.py > clean_wikidata

git clone https://github.com/stanfordnlp/GloVe.git glove
cd glove && make
cd ..

EMBED_PATH=glove_embedings
mkdir $EMBED_PATH
# glove
CORPUS=clean_wikidata
VOCAB_FILE=$EMBED_PATH/vocab.txt
COOCCURRENCE_FILE=$EMBED_PATH/cooccurrence.bin
COOCCURRENCE_SHUF_FILE=$EMBED_PATH/cooccurrence.shuf.bin
BUILDDIR=glove/build
SAVE_FILE=$EMBED_PATH/glove_zhwiki_char_embedings
VERBOSE=2
MEMORY=4.0
VOCAB_MIN_COUNT=5
VECTOR_SIZE=100
MAX_ITER=50
WINDOW_SIZE=15
BINARY=0
NUM_THREADS=8
X_MAX=10

echo "$ $BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE"
$BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE

echo "$ $BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE"
$BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE
echo "$ $BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE"
$BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE
echo "$ $BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE"
$BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE

python create_char_embedding.py

exit
#fasttext
/home/liqiang.flq/embedding/fastText/fasttext skipgram -input $SOURCE -output fasttext_alinlp_zhwiki_char_vectors -lr 0.025 -dim 100  -ws 10 -epoch 1 -minCount 5 -neg 5 -loss ns -bucket 2000000 -minn 3 -maxn 6 -thread 4 -t 1e-4 -lrUpdateRate 100

exit
# word2vec
/home/liqiang.flq/embedding/word2vec/word2vec -train $SOURCE -output w2v_alinlp_zhwiki_char_vectors -size 100 -window 10 -sample 1e-4 -negative 5 -hs 0 -binary 0 -cbow 1 -iter 10
