import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data (first time only)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def summarize_text(text, num_sentences=3):
    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Tokenize words and calculate frequency
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    freq_table = {}
    for word in words:
        if word.isalpha() and word not in stop_words:
            freq_table[word] = freq_table.get(word, 0) + 1

    # Score sentences
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq_table:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq_table[word]

    # Pick top sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = " ".join(summary_sentences)
    return summary

if __name__ == "__main__":
    print("Enter/Paste your text. Press Enter twice to finish:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    text_input = " ".join(lines)

    while True:
        try:
            num_sentences = int(input("Enter number of sentences for summary: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    summary = summarize_text(text_input, num_sentences=num_sentences)
    print("\n--- Summarized Text ---\n")
    print(summary)
