import stanza

#load stanza
nlp = stanza.Pipeline('en', r'/mnt/hd0/POStaggingFuzzing/nlp-models/stanzamodel/stanza_model/', processors='tokenize,mwt,pos,lemma,depparse', tokenize_pretokenized=True)
#create output file

doc = nlp('Spouse(s) Jean-Louis Richard ( m. 1949 ; div. 1964 ) William Friedkin ( m. 1977 ; div. 1979 )')
# print(doc.sentences[0].words)

print(*[f'id: {word.id}\tword: {word.text}\tupos: {word.upos}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')