import random

class WordSearch:
    def __init__(self, size=10, words=None):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.words = words if words else []

    def fill_grid(self):
        for word in self.words:
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])
            if direction == 'horizontal':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - len(word))
                for i in range(len(word)):
                    self.grid[row][col + i] = word[i]
            elif direction == 'vertical':
                row = random.randint(0, self.size - len(word))
                col = random.randint(0, self.size - 1)
                for i in range(len(word)):
                    self.grid[row + i][col] = word[i]
            elif direction == 'diagonal':
                row = random.randint(0, self.size - len(word))
                col = random.randint(0, self.size - len(word))
                for i in range(len(word)):
                    self.grid[row + i][col + i] = word[i]

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))

if __name__ == "__main__":
    words = ['python', 'code', 'game', 'search', 'word']
    word_search = WordSearch(words=words)
    word_search.fill_grid()
    word_search.print_grid()
