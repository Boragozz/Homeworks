# Palindrom review
def palindrome(text: str) -> bool:
  revText = ''.join(char.lower() for char in text if char.isalnum()
  return revText = revText[::-1]
review = input("Введите слово для проверки: ")
print(polindrom(review))
