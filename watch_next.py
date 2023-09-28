import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_md")

movie_descriptions = {}
with open('movies.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(':', 1)
        if len(parts) == 2:
            movie_name, movie_description = parts[0].strip(), parts[1].strip()
            movie_descriptions[movie_name] = movie_description
            
def find_similar_movie(input_description):
    similarity_scores = defaultdict(float)
    
    input_doc = nlp(input_description)
    
    for movie_name, movie_description in movie_descriptions.items():
        movie_doc = nlp(movie_description)
        similarity_scores[movie_name] = input_doc.similarity(movie_doc)
        
    most_similar_movie = max(similarity_scores, key = similarity_scores.get)
    
    return most_similar_movie

input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
most_similar_movie = find_similar_movie(input_description)

print(f"The most similar movie is: {most_similar_movie}")

     