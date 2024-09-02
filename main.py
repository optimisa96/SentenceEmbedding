from sentence_embedding import get_sentence_embedding

dataset_sentences = [('Transfer window should close before season begins', 'sport'),
                     ('A tech firm stole our voices - then cloned and sold them', 'business'),
                     ('How the youngest Canary Island escaped mass tourism', 'tourism')]

input_sentence = 'World champion Scotney to face Motu in October'

input_sentence_embedding = get_sentence_embedding(input_sentence)
print("Input sentence embedding parameter count: %s " % len(input_sentence_embedding))

dataset_embeddings = []
for sentence, category in dataset_sentences:
    embedding = get_sentence_embedding(sentence)
    dataset_embeddings.append((embedding, category))
