### **Two given words are anagrams**
* An anagram means both words contain the same characters with the same frequency, but possibly in a different order.
* Example
```python
hello
oellh
```
```python
def anagram(str1, str2):

    # First checks if both words have the same length.
    if len(str1) != len(str2):
        return False

    # Then for each character, checks whether it appears the same number of times in both words.
    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            return False

    return True


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if anagram(word1, word2):
    print("Anagrams")
else:
    print("Not Anagrams")
```