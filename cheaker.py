import re
import math
from collections import Counter

def text_to_vector(text):
    words = re.findall(r'\w+', text)
    return Counter(words)

def cosine_similarity(vector1, vector2):
    intersection = set(vector1) & set(vector2)
    numerator = sum([vector1[x] * vector2[x] for x in intersection])

    sum1 = sum([vector1[x] ** 2 for x in vector1])
    sum2 = sum([vector2[x] ** 2 for x in vector2])

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def plagiarism_checker(text1, text2, threshold=0.8):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    similarity = cosine_similarity(vector1, vector2)

    if similarity >= threshold:
        return f"Plagiarism detected! Similarity: {similarity:.2f}"
    else:
        return "No plagiarism detected."

if __name__ == "__main__":
    # Example usage
    original_text = "This is an example text for the plagiarism checker."
    copied_text = "This is a copied text for the plagiarism checker."

    result = plagiarism_checker(original_text, copied_text)
    print(result)
