# def anagram_finder(context):
# 	context.split('')


def anagram_finder(word1, word2):
  newlist1 = list(word1.lower())
  newlist2 = list(word2.lower())
  newlist1.sort()
  newlist2.sort()
  for element in range(0, len(newlist2)):
    if newlist1[element] != newlist2[element]:
      return False
  return True

print(anagram_finder('yoshi', 'syoih'))