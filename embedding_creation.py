from transformers import AutoModel, AutoTokenizer
import torch.nn.functional as F
import torch


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def mean_pooling(model_output):
    return torch.mean(model_output["last_hidden_state"], dim=1)

def get_sentence_embedding(text):
    encoded_input = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**encoded_input)
    sentence_embeddings = mean_pooling(model_output)
    return F.normalize(sentence_embeddings)

