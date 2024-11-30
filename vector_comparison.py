from sentence_transformers import util
from enum import Enum

class ComparisonType(Enum):
    COS_SIM = 0
    EUCLIDEAN_SIM = 1
    DOT_PRODUCT_SIM = 2
    

def compare_vectors(first_vector, second_vector, comparison_type: ComparisonType):
    if (comparison_type == ComparisonType.COS_SIM):
        return util.pytorch_cos_sim(first_vector, second_vector)
    if (comparison_type == ComparisonType.EUCLIDEAN_SIM):
        return util.euclidean_sim(first_vector, second_vector)
    if (comparison_type == ComparisonType.DOT_PRODUCT_SIM):
        return util.dot_score(first_vector, second_vector)

