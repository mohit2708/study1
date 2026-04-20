### **Ques. Count the number of vowels in a string?**
```python
string = input("Enter a string: ")
# string = string.lower()
vowels = 0
for i in string:
    if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='O' or i=='U' or i=='u'):
        vowels = vowels+1
print("Number of vowels ", vowels)

Output:- 
Enter a string: Mohit saxena
Number of vowels  4
```

#### Type Example 2
```python
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
```

```python
text = "Hello World"
vowels = "aeiouAEIOU"
# Sums 1 for every character in 'text' that is found in 'vowels'
count = sum(1 for char in text if char in vowels)
print(count)  # Output: 3
```

### Counting Individual Vowels
```python
text = "Python Programming is Fun"
# Initialize a dictionary with vowels as keys and 0 as initial count
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Standardized for caseless comparison
text = text.lower()

# Iterate through each character in the string
for char in text:
    # Check if the character is one of the keys in our dictionary
    if char in vowel_counts:
        vowel_counts[char] += 1

print(vowel_counts) # Output: {'a': 1, 'e': 0, 'i': 2, 'o': 2, 'u': 1}
```
- Dynamic Counting
```python
text = "Python Programming is Fun"
vowel_counts = {}  # Start with an empty dictionary
vowels = "aeiou"

text = text.lower()

for char in text:
    if char in vowels:
        if char in vowel_counts:
            vowel_counts[char] += 1
        else:
            vowel_counts[char] = 1 # Adds the new vowel to the dictionary

print(vowel_counts)
# Output: {'o': 2, 'a': 1, 'i': 2, 'u': 1}
```

### Ques. To identify if the Character is vowel or consonant?
```python
def vowel_or_consonant(string):
    vowel = 'aeiouAEIOU'
    for i in string:
        if i in vowel:
            print('Vowel')
        else:
            print('consonant')
vowel_or_consonant('a') # Output:- Vowel

# Method 2
l = input("Enter the character: ")
if l.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")
```