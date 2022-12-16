import tensorflow_hub as hub

BERT_URL = 'https://tfhub.dev/google/bert_cased_L-12_H-768_A-12/1'
module = hub.Module(BERT_URL)

# Look at the descriptor. This would tell you the model name
# cat $TFHUB_CACHE_DIR/ecd2596ce849110246602e3d4d81e2d9719cb027.descriptor.txt

# Further look at the assets folder, this has the file `vocab.txt`
# ls $TFHUB_CACHE_DIR/ecd2596ce849110246602e3d4d81e2d9719cb027/assets


import tokenization

def create_tokenizer(vocab_file, do_lower_case=False):
    return tokenization.FullTokenizer(vocab_file=vocab_file, do_lower_case=do_lower_case)
    
tokenizer = create_tokenizer('vocab.txt', do_lower_case=False)


def convert_sentence_to_features(sentence, tokenizer, max_seq_len):
    tokens = ['[CLS]']
    tokens.extend(tokenizer.tokenize(sentence))
    if len(tokens) > max_seq_len-1:
        tokens = tokens[:max_seq_len-1]
    tokens.append('[SEP]')
    
    segment_ids = [0] * len(tokens)
    input_ids = tokenizer.convert_tokens_to_ids(tokens)
    input_mask = [1] * len(input_ids)

    #Zero Mask till seq_length
    zero_mask = [0] * (max_seq_len-len(tokens))
    input_ids.extend(zero_mask)
    input_mask.extend(zero_mask)
    segment_ids.extend(zero_mask)
    
    return input_ids, input_mask, segment_ids

def convert_sentences_to_features(sentences, tokenizer, max_seq_len=20):
    all_input_ids = []
    all_input_mask = []
    all_segment_ids = []
    
    for sentence in sentences:
        input_ids, input_mask, segment_ids = convert_sentence_to_features(sentence, tokenizer, max_seq_len)
        all_input_ids.append(input_ids)
        all_input_mask.append(input_mask)
        all_segment_ids.append(segment_ids)
    
    return all_input_ids, all_input_mask, all_segment_ids