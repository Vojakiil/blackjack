import time
import random

suits = ["♦️", "♥️", "♠️", "♣️"]
cards = list(range(2, 11)) + ["Валет", "Дама", "Король", "Туз"]


# будем использовать для генерации случайной карты, например если взять еще карту
def get_card():
  """
  Эта функция должна вернуть случайную карту в формате [имя, ценность, масть]

  Например:
  get_card() => ['Туз', 11, '♥️']
  """
  card_name = random.choice(cards)
  suit = random.choice(suits)

  if card_name == "Туз":
    count = 11
  elif card_name == "Король":
    count = 10
  elif card_name == "Валет":
    count = 10
  elif card_name == "Дама":
    count = 10
  else:
    count = card_name

  return [card_name, count, suit]


# будет использоваться только в начале ходов, чтобы выбрать игроку и диллеру две карты
def get_pair_cards():
  """
  Эта функция должна вернуть 2 случайных карты

  Например:
  get_pair_cards() => [['Валет', 10, '♥️'], ['5', 5, '♠️']]
  """
  cards = []

  for i in range(2):
    cards.append(get_card())

  return cards


def calc_cards_rate(cards):
  """
  Эта функция считает ценность нескольких карт
  Функция принимает cards (это список карт). Возвращает число (ценность этих карт)

  Например:
  calc_cards_rate([['Валет', 10, '♥️'], ['5', 5, '♠️']]) => 15
  """
  rate = 0

  for card in cards:
    rate += card[1]
  
  return rate


def print_cards(player_name, cards):
  """
  Эта функция выводит карты игрока
  player_name - Имя игрока, например Диллер
  cards - Карты игрока, например [[4, 4, '♦️'], [8, 8, '♦️']]

  В итоге выводит в консоль подобный текст:

  Карты Диллер:
  4 ♦️
  8 ♦️
  (всего 12 очков)
  ----------------
  """
  print("Карты", player_name + ":")

  for card in cards:
    print(card[0], card[2])

  rate = calc_cards_rate(cards)
  print("(всего", rate, "очков)")
  print("----------------")


def take_card(player_name, player_cards):
  """
  Эта функция берет случайную карту пользователю
  player_name - Имя игрока, например Диллер
  player_cards - Карты игрока, например [[4, 4, '♦️'], [8, 8, '♦️']]
  и выводит информациюю об этом в консоль
  """
  card = get_card()
  
  player_cards.append(card)
  rate = calc_cards_rate(player_cards)
  
  print(player_name, "взял карту", card[0], card[2])
  print("(всего", rate, "очков)")

dealer_cards = get_pair_cards()
player_cards = get_pair_cards()

username = input("Введите свое имя: ")

print_cards("Диллер", dealer_cards)
print_cards(username, player_cards)

while True:
  rate = calc_cards_rate(player_cards)
  
  if rate > 21: 
    print("Перебор!")
    break

  action = input("Взять еще карту? >> ")

  if action.lower() == "да":
    take_card(username, player_cards)
  else:
    print("Хватит!")
    break

time.sleep(1)
print("Ход Диллера!")
time.sleep(1)

while True:
  rate = calc_cards_rate(dealer_cards)
  time.sleep(1)
  
  if rate > 21:
    print("Перебор!")
    break

  time.sleep(3)
  
  if rate < 16:
    take_card("Диллер", dealer_cards)
  else:
    print("Хватит!")
    break

player_rate = calc_cards_rate(player_cards)
dealer_rate = calc_cards_rate(dealer_cards)

if player_rate > 21 and dealer_rate <= 21:
  print("Диллер выиграл!")
elif dealer_rate > 21 and player_rate <= 21:
  print(username, "выиграл!")
elif player_rate > 21 and dealer_rate > 21:
  print(username, "и Диллер проиграли!") 
elif player_rate > dealer_rate:
  print(username, "выиграл!")
elif dealer_rate > player_rate:
  print("Диллер выиграл!")
else:
  print("Ничья!")
