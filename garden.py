# import the spacy module
import spacy

# call spacy.load() to load en_core_web_sm pipeline and define as nlp

nlp = spacy.load('en_core_web_sm')

# initalise list that stores the garden path sentences

gardenpathSentences = ["The complex houses married and single soldiers and their families.",
                       "Because he always jogs a mile seems a short distance to him.",
                       "The florist sent the bouquet of flowers was very flattered.",
                       "The cotton clothing is made of grows in Mississippi.", "The old man the boat.",
                       "The barge floated down the river sank.", "The man who hunts ducks out on weekends",
                       "The horse raced past the barn fell", "When Fred eats food gets thrown."]


# loop through each sentence in the list of sentences

for sentence in gardenpathSentences:

    # call nlp on each sentnces

    text = nlp(sentence)

    # loop through each entity found in text entities and print out details about each

    print([(x, x.label_, x.label) for x in text.ents])


# I did not expect the Fred to be treated as an entity as it is a general name, but it is labelled as a person
# so perhaps it is reffering to a specific person named fred rather than the name itself, same for weekends, which
# which I did not expect to be treated as an entity
