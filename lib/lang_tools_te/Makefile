TAGGER=./bin/tnt -H -v0 models/telugu  # Use option -u1 for speed at a slight cost of precision. For more options use ./bin/tnt -h
LEMMATIZER=./bin/lemmatiser.py models/telugu.lemma
TAG2VERT=./bin/tag2vert.py
TOKENIZER=./bin/unitok.py -l telugu -n

tag:
	cat telugu.input.txt | $(TOKENIZER) | sed -e 's/^\.$$/.\n<\/s>\n<s>/g' | sed -e 's/^\?$$/?\n<\/s>\n<s>/g' > telugu.tmp.words
	$(TAGGER) telugu.tmp.words | sed -e 's/\t\+/\t/g' | $(LEMMATIZER) | $(TAG2VERT) > telugu.output.txt
	rm telugu.tmp.words
	echo "Output stored in telugu.output.txt"

tag2:
	cat telugu.input.txt | $(TOKENIZER)  > telugu.tmp.words
	$(TAGGER) telugu.tmp.words | sed -e 's/\t\+/\t/g' | $(LEMMATIZER) | $(TAG2VERT) > telugu.output.txt
