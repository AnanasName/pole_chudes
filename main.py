import random


class PoleChudes:
    lives = 5
    default_lives = 0
    words_array = ["книга", "месяц", "ручка", "шарик",
             "олень", "носок", "поле", "таблоид", "угадайка",
             "программирование"]
    guessed_letters = []
    current_word = ""
    is_win = False

    def __init__(self, lives_count):
        self.lives = lives_count
        self.default_lives = lives_count

    def print_word_state(self):
        for letter in self.current_word:
            if self.guessed_letters.__contains__(letter):
                print(letter.capitalize(), end=' ')
            else:
                print("\u25A0", end=' ')
        print(f'| {self.lives}x\u2764')

    def print_whole_word(self):
        for letter in self.current_word:
            print(letter.capitalize(), end=' ')
        print()

    def print_info(self):
        self.print_word_state()
        value = input('Назовите буквы или слово целиком: ').lower()
        if value == "":
            print("Вы должны ввести букву")
            return
        if value == self.current_word:
            self.is_win = True
            return
        if self.current_word.__contains__(value):
            if self.guessed_letters.__contains__(value):
                print("Вы уже вводили данную букву")
            else:
                self.guessed_letters.append(value)
            if self.guessed_letters.__len__() == set(self.current_word).__len__():
                self.is_win = True
        else:
            self.lives -= 1

    def main_logic(self):
        self.current_word = random.choice(self.words_array)
        while self.lives > 0:
            if self.is_win:
                self.print_whole_word()
                print("Вы выиграли! Приз в студию!")
                choice = input("Вы хотите сыгарть ещё? (да/нет): ")
                if choice.lower() == "да":
                    self.words_array.remove(self.current_word)
                    if self.words_array.__len__() == 0:
                        print("Вы выиграли все туры")
                        return
                    self.lives = self.default_lives
                    self.guessed_letters = []
                    self.is_win = False
                    self.current_word = random.choice(self.words_array)
                    continue
                else:
                    return
            self.print_info()
        print("Вы проиграли")


def input_logic():
    global pc
    wanna_play = True
    if wanna_play:
        difficulty = int(input("Выберите уровень сложности: (1 - простой, 2 - средний, 3 - сложный): "))
        if difficulty == 1:
            pc = PoleChudes(7)
        elif difficulty == 2:
            pc = PoleChudes(5)
        elif difficulty == 3:
            pc = PoleChudes(3)
    pc.main_logic()


input_logic()
