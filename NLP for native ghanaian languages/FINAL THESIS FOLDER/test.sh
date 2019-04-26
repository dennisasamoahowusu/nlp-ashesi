#!/bin/bash

RESOURCES_FOLDER=/home/david/kaldi/egs/dwom/resources
PROJECT_ROOT=/home/david/kaldi/egs/dwom
train_cmd="utils/run.pl"
decode_cmd="utils/run.pl"
mfccdir=mfcc
### Preparing Test Data and Decoding


cp $RESOURCES_FOLDER/clean/test_2/data/wav.scp data/test/wav.scp
# cp $RESOURCES_FOLDER/data/text_test data/test/text
cp $RESOURCES_FOLDER/clean/test_2/data/utt2spk data/test/utt2spk

utils/utt2spk_to_spk2utt.pl data/test/utt2spk > data/test/spk2utt

steps/make_mfcc.sh --nj 1 --cmd "$train_cmd" data/test exp/make_mfcc/test $mfccdir/test
steps/compute_cmvn_stats.sh data/test exp/make_mfcc/test $mfccdir/test


#utils/mkgraph.sh data/lang_test exp/tri1 exp/tri1/graph
#steps/decode.sh --nj 1 --cmd "$decode_cmd" exp/tri1/graph data/test exp/tri1/decode

utils/mkgraph.sh data/lang_test exp/tri2a exp/tri2a/graph
steps/decode.sh --nj 1 --cmd "$decode_cmd" exp/tri2a/graph data/test exp/tri2a/decode

#utils/mkgraph.sh data/lang_test exp/tri2b exp/tri2b/graph
#steps/decode.sh --nj 1 --cmd "$decode_cmd" exp/tri2b/graph data/test exp/tri2b/decode

#utils/mkgraph.sh data/lang_test exp/tri3b exp/tri3b/graph
#steps/decode_fmllr.sh --config conf/decode.config --nj $njobs --cmd "$decode_cmd" \
# exp/tri3b/graph data/test exp/tri3b/decode
