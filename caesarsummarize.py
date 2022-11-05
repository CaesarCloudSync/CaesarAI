import os
import re
import sys
import nltk
import heapq
#nltk.download('stopwords')
#nltk.download("punkt")

class CaesarAISummarize:
    @staticmethod
    def summarize():
        # runsummarize <filename> <subject> <num_of_sentences>
        if len(sys.argv) > 4 or len(sys.argv) == 1 or len(sys.argv) == 3: 
            print("Max 4 arguments.")
        elif len(sys.argv) == 2:
            if sys.argv[1] == "help":
                print("runsummarize <filename> <subject> <num_of_sentences>")
        elif len(sys.argv) == 4:
            if "CaesarNotes" not in os.listdir():
                os.mkdir("CaesarNotes")
            filename = sys.argv[1]
            subject = sys.argv[2].capitalize()
            num_of_sentences = int(sys.argv[3])
            with open(f"CaesarNotes/{subject}/{filename}.txt","r") as f:
                article_text = f.read()
            article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
            article_text = re.sub(r'\s+', ' ', article_text)
            formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
            formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
            sentence_list = nltk.sent_tokenize(article_text)
            #print(sentence_list)
            stopwords = nltk.corpus.stopwords.words('english')

            word_frequencies = {}
            for word in nltk.word_tokenize(formatted_article_text):
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1
            maximum_frequncy = max(word_frequencies.values())

            for word in word_frequencies.keys():
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

            sentence_scores = {}
            for sent in sentence_list:
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]
            
            summary_sentences = heapq.nlargest(num_of_sentences, sentence_scores, key=sentence_scores.get)

            summary = ' '.join(summary_sentences)
            if "CaesarSummary" not in os.listdir():
                os.mkdir("CaesarSummary")
            if subject not in os.listdir("CaesarSummary"):
                os.mkdir(f"CaesarSummary/{subject}")
            with open(f"CaesarSummary/{subject}/{filename}.txt","w+") as f:
                f.write(summary)
            #print(summary)
            summary_sent = ""
            summary_list = summary.split(".")
            #print(summary_list)
            for sent in summary_list:
                if sent != "":
                    #print(sent)
                    summary_sent += f"{sent}.\n".lstrip()
            
            print(summary_sent)
            return summary
       
if __name__ == "__main__":
    CaesarAISummarize.summarize()
