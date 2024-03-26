def main():
  for i in range(1,11):
    file = str(i)+".in"
    fin = open(file, "r")
    n = int(fin.readline().strip())
    #print(n)

    elsie_has = []

    for j in range(n):
      card = int(fin.readline().strip())
      elsie_has.append(card)



    problem_solve(n, elsie_has)

def problem_solve(n, elsie_cards):
  ''' Put your code here to solve the problem! '''
  points = 0
  elsie_cards.sort()
  #print(f'E: {elsie_cards}, {len(elsie_cards)}')
  bessie_cards = []
  for i in range(1, n * 2):
    if i not in elsie_cards:
      bessie_cards.append(i)

  #print(f'E: {elsie_cards}, {len(elsie_cards)}')
  #print(f'B: {bessie_cards}, {len(bessie_cards)}')

  #if bessie wins, incriment both
  #if bessie loses, incriment  bessie until they win
  #probably use a while loop but can use for

  #for i in [1, 2n]:
    #if E[j] == i

  E_pos = 0
  B_pos = 0

  if elsie_cards[-1] < bessie_cards[-1]:
    points += 1

  while E_pos <= len(elsie_cards) - 1 and B_pos <= len(bessie_cards) - 1:
    #print(f'E: {E_pos} = {elsie_cards[E_pos]} vs B: {B_pos} = {bessie_cards[B_pos]}')
    if bessie_cards[B_pos] < elsie_cards[E_pos]:
      B_pos += 1
    elif bessie_cards[B_pos] > elsie_cards[E_pos]:
      points += 1
      B_pos += 1
      E_pos += 1
  print(points)

main()