from sentence_transformers import SentenceTransformer
from typing import Union, List

model = SentenceTransformer("all-mpnet-base-v2", tokenizer_kwargs= {'clean_up_tokenization_spaces': True})
def get_sentence_embedding(sentences: Union[str, List[str]]):
    return model.encode(sentences)
