import random

# Константы карт
SUIT_TUPLE = ("Пики", "Червы", "Трефы", "Бубны")
RANK_TUPLE = ("Туз", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король")

NCARDS = 8

# Проходим по колоде, и эта функция возвращает случайную карты из колоды
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Снимаем одну карты с верхней части колоды и возвращаем
    return thisCard

# Проходим по колоде, и эта функция возвращает перемешанную копию колоды
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # Создаем копию старовой колоды
    random.shuffle(deckListOut)
    return deckListOut

# Основной код
print("Добро пожаловать в игру 'Больше-меньше'")
print("Вам нужно выбрать, будет ли следующая показанная карта больше или меньше текущей карты.")
print("Правильный выбор добавляет 20 очков; ошибетесь и потеряете 15 очков.")
print("У Вас есть 50 очков на старте.")
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {"rank": rank, "suit": suit, "value": thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True: # Несколько игр
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict["rank"]
    currentCardValue = currentCardDict["value"]
    currentCardSuit = currentCardDict["suit"]
    print("Стартовая карта: ", currentCardRank, currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): # Играем в одну игру
                                        # из этого кол-ва карт.
        answer = input("Следующая карта будет больше или меньше чем " +
                        currentCardRank + " " + 
                        currentCardSuit + "? (enter h or l): ")
        answer = answer.casefold() # переводим в нижний регистр
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict["rank"]
        nextCardSuit = nextCardDict["suit"]
        nextCardValue = nextCardDict["value"]
        print("Следующая карта: ", nextCardRank, nextCardSuit)

        if answer == "h":
            if nextCardValue > currentCardValue:
                print("Верно. Поздравляю!")
                score = score + 20
            else:
                print("Неверно. Потрачено 15 очков.")
                score = score - 15

        elif answer == "l":
            if nextCardValue < currentCardValue:
                score = score + 20
                print("Верно. Поздравляю!")

            else:
                score = score - 15
                print("Неверно. Потрачено 15 очков.")
                
        print("Ваш счёт:", score)
        print()
        currentCardRank = nextCardRank
        carrentCardValue = nextCardValue # не нужна текущая масть
        currentCardSuit = nextCardSuit

    goAgain = input("Хотите сыграть еще? ENTER - да, если нет, то нажмите 'q': ")
    if goAgain == "q":
        break

print("Хорошо. Всего доброго.")