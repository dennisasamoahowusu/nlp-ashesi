#!/bin/bash

RESOURCES_FOLDER=/home/david/kaldi/egs/dwom/resources
PROJECT_ROOT=/home/david/kaldi/egs/dwom

train_cmd="utils/run.pl"
decode_cmd="utils/run.pl"

rm -rf data exp mfcc

mkdir data
mkdir data/train
cp $RESOURCES_FOLDER/clean/david_100/data/wav.scp data/train/
cp $RESOURCES_FOLDER/clean/david_100/data/text data/train/
cp $RESOURCES_FOLDER/clean/david_100/data/utt2spk data/train/

utils/fix_data_dir.sh data/train

utils/utt2spk_to_spk2utt.pl data/train/utt2spk > data/train/spk2utt

mfccdir=mfcc
steps/make_mfcc.sh --nj 20 --cmd "$train_cmd" data/train exp/make_mfcc/train $mfccdir/train
steps/compute_cmvn_stats.sh data/train exp/make_mfcc/train $mfccdir/train

mkdir data/local
mkdir data/local/dict
cp $RESOURCES_FOLDER/clean/data/lexicon.txt data/local/dict/
cp $RESOURCES_FOLDER/clean/data/nonsilence_phones.txt data/local/dict/
cp $RESOURCES_FOLDER/clean/data/silence_phones.txt data/local/dict/
cp $RESOURCES_FOLDER/clean/data/extra_questions.txt data/local/dict/
cp $RESOURCES_FOLDER/clean/data/optional_silence.txt data/local/dict/

utils/prepare_lang.sh data/local/dict "<SPOKEN_NOISE>" data/local/lang data/lang

mkdir data/lang_test

mkdir data/local/lm
cp $RESOURCES_FOLDER/clean/data/corpus.lm data/local/lm

# In addition to creating G.fst, it also copies other stuff into data/lang_test
utils/format_lm_sri.sh data/lang data/local/lm/corpus.lm data/lang_test

njobs=1
steps/train_mono.sh --nj $njobs --cmd "$train_cmd" data/train data/lang exp/mono
steps/align_si.sh --nj $njobs --cmd "$train_cmd" data/train data/lang exp/mono exp/mono_ali
steps/train_deltas.sh --cmd "$train_cmd" 2000 11000 data/train data/lang exp/mono_ali exp/tri1
steps/align_si.sh --nj $njobs --cmd "$train_cmd" --use-graphs true data/train data/lang exp/tri1 exp/tri1_ali
steps/train_deltas.sh --cmd "$train_cmd" 2000 11000 data/train data/lang exp/tri1_ali exp/tri2a
#steps/train_lda_mllt.sh --cmd "$train_cmd" 2000 11000 data/train data/lang exp/tri1_ali exp/tri2b
#steps/align_si.sh --nj $njobs --cmd "$train_cmd" --use-graphs true data/train data/lang exp/tri2b exp/tri2b_ali
#steps/make_denlats.sh --nj $njobs --cmd "$train_cmd" data/train data/lang exp/tri2b exp/tri2b_denlats
#steps/train_mmi.sh data/train data/lang exp/tri2b_ali exp/tri2b_denlats exp/tri2b_mmi
#steps/train_mmi.sh --boost 0.05 data/train data/lang exp/tri2b_ali exp/tri2b_denlats exp/tri2b_mmi_b0.05
#steps/train_mpe.sh data/train data/lang exp/tri2b_ali exp/tri2b_denlats exp/tri2b_mpe
#steps/train_sat.sh 2000 11000 data/train data/lang exp/tri2b_ali exp/tri3b

mkdir data/test
