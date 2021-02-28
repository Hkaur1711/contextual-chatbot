
# author : A.M.D.Srinivas ( amdsrinivas@gmail.com)

class data_extractor:  # spacy API wrapped under a class.
    '''
    Extractor class that uses Spacy Entity Recognizer to detect the entities in a Document.
    parameters:
        file_name : string ( default_value = input.txt)
            The name of the input file from which the data has to be extracted.
        model_name : string ( default_value = 'en')
            The Spacy model name to be loaded.
    '''
    def __init__(self,input_data, model_name='en'):
        import spacy
        self.nlp_model = spacy.load('en')
        self.entities = []
        self.noun_chunks = []
        self.doc = self.nlp_model(input_data)
    def extract_entities(self):   # Get a dictionary of entities and noun phrases.
        doc_length = len(self.doc)
        data = {}
        data['entities'] = list(self.doc.ents)
        for item in data['entities']:
            data[item] = item.label_
        data['noun_chunks'] = list(self.doc.noun_chunks)
        return data
    def pretty_print(self,data):   # Display the extracted data more intuitively.
        if len(data['entities']) == 0:
            print("No entities extracted.")
        else:
            print("Entities extracted : {0}".format(data['entities']))
            print("Entity Details :")
            for item in data['entities']:
                print("{0}\t{1}".format(item, data[item]))
        if len(data['noun_chunks']) == 0:
            print("No noun phrases detected.")
        else:
            print("Noun phrases detected.")
            for i in range(len(data['noun_chunks'])):
                print("{0}. {1}".format(i+1, data['noun_chunks'][i]))
        print("*"*5+"DONE"+"*"*5)

'''
def main():
    extractor = data_extractor()
    data = extractor.extract_entities()
    extractor.pretty_print(data)

main()'''
