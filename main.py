from random import shuffle

secret_words = []

while True:
  secret_word, hint = [input('\nSecret word?:'), input('Hint?:')]
  if secret_word == '' or hint == '': break
  elif secret_word.isalpha(): secret_words.append({'secret_word': secret_word, 'hint': hint, 'score': 6})
  else: print("\nThe secret word must only contain alphabetical characters. Please try again.\n")

shuffle(secret_words)
for current_secret_word in secret_words:
  word = ['_'] * len(current_secret_word["secret_word"])
  misses = []

  while current_secret_word["score"] > 0 and '_' in word:
    guess = input("\nWord: {}\nHint: {}\nGuess?: ".format(' '.join(word), current_secret_word["hint"]))[0].upper()
    if 65 <= ord(guess) <= 90:
      if guess not in word and guess not in misses:
        if guess in current_secret_word["secret_word"].upper():
          for i in [index for index, letter in enumerate(current_secret_word["secret_word"].upper()) if letter == guess]:
            word[i] = guess
        else:
          current_secret_word["score"] -= 1
          misses.append(guess)
        print('\nWord:', ' '.join(word),
              '\nHint:', current_secret_word["hint"],
              '\nMisses:', ' '.join(misses),
              '\nScore:', current_secret_word["score"])
      else: print('Already made that guess. Try a different letter.')
    else: print('Guess must be a letter (A to Z).')
  print("\nScore:", current_secret_word["score"], "\nSecret word:", current_secret_word["secret_word"])

wins = [secret_word for index, secret_word in enumerate(secret_words) if secret_word["score"] > 0]
losts = [secret_word for secret_word in secret_words if secret_word not in wins]

print("\nTotal secret words:", len(secret_words),
      "\nTotal wins:", len(wins),
      "\nTotal losts:", len(losts),
      "\nTotal score:", sum(secret_word["score"] for secret_word in wins),
      "\nWins:\n", "\n ".join([win["secret_word"] for win in wins]),
      "\nLosts:\n", "\n".join([lost["secret_word"] for lost in losts]))