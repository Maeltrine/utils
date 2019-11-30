# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class TextMetrics:
    """
    Compute metrics for a given text
    Total number of words
    Maximum number of words per line
    Frequency and line occurences for a given word
    """

    def __init__(self, text):
        self.text = text
        self.words = {}
        self.words_per_frequency = {}
        self.metrics = {'totalWords': 0,
                        'maxWordsPerLine': 0 }

    @staticmethod
    def _clean_word(word: str):
        """
        Given a word, lower it and makes sure its characters are among the alphabet

        :param word (string): word to clean
        :return cleaned word (string):
        """
        return ''.join([letter if letter.isalpha() else '' for letter in word]).lower()

    def get_n_most_recent_words(self, n: int):
        """
        Get the n most recent words ordered by frequency and by alphabetical order
        in case of equal frequency

        :param n (int): number of most recent words to get
        :return most recent words (list[str])
        """
        most_recent_words = []
        word_count = 0

        # Build the table of words per frequency if it does not exist yet
        # for a given frequency store all the words associated to it
        if self.words_per_frequency == {}:
            for word in self.words.keys():
                word_frequency = self.words[word]['frequency']
                if word_frequency not in self.words_per_frequency.keys():
                    self.words_per_frequency[word_frequency] = [word]
                else:
                    self.words_per_frequency[word_frequency] += [word]

        # Build the list of most recent words by decreasing frequency
        # and alphabetically ordered words
        frequencies = list(self.words_per_frequency.keys())
        frequencies.sort(reverse=True)

        for frequency in frequencies:
            for word in sorted(self.words_per_frequency[frequency]):
                if word_count < n:
                    most_recent_words+=[word]
                    word_count+=1
                else:
                    break
        return most_recent_words

    def parse(self):
        """
        Parse a text input by lines and words
        evaluate metrics for this given text

        :param text (stdin):
        """
        lineNumber = 0
        for line in self.text:
            line_words = line.split()
            lineWordsCount = 0

            # Update the metrics for a given word if it is considered valid after cleaning
            for item in line_words:
                word = self._clean_word(item)
                if word != '':
                    if self.words.get(word) is not None:
                        self.words[word]['frequency'] += 1
                        if lineNumber not in self.words[word]['word_occurences']:
                            self.words[word]['word_occurences'] += [lineNumber]
                    else:
                        self.words[word] = {}
                        self.words[word]['frequency'] = 1
                        self.words[word]['word_occurences'] = [lineNumber]
                    lineWordsCount += 1
            lineNumber += 1

            # Update text general metrics
            self.metrics['totalWords'] += lineWordsCount
            if self.metrics['maxWordsPerLine'] < lineWordsCount:
                self.metrics['maxWordsPerLine'] = lineWordsCount

    def print_metrics(self, n_most_recent_words):
        """
        Print general metrics obtained from the parsed text with
        metrics for the number of most recent words n_most_recent_words

        :param n_most_recent_words (int): most recents words to print metrics for
        """
        print(f"Total words = {self.metrics['totalWords']}, Max words per line = {self.metrics['maxWordsPerLine']}")
        for word in self.get_n_most_recent_words(n_most_recent_words):
            print(f"{word} {self.words[word]['frequency']} {self.words[word]['word_occurences']}")


if __name__ == "__main__":
    text_metrics = TextMetrics(sys.stdin)
    text_metrics.parse()
    text_metrics.print_metrics(10)

