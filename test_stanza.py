import stanza

#load stanza
nlp = stanza.Pipeline('en', r'/mnt/hd0/POStaggingFuzzing/nlp-models/stanzamodel/stanza_model/', processors='tokenize,mwt,pos,lemma,depparse', tokenize_pretokenized=True)
#create output file

doc = nlp('Be sure to ring the little bell on your way out if you enjoyed your meal !')
print(doc.sentences[0].words)

print(*[f'id: {word.id}\tword: {word.text}\tupos: {word.upos}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')