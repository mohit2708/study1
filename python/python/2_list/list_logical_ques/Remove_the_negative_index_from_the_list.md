### **Ques. Remove the negative index from the list?**
```python
lstnum = [-5, 27, 1000, -4, 0, -80,56,-67]
# //Removing negative values
posNum = []
for item in lstnum:
    if item >= 0:
        posNum.append(item)
print(posNum)

res_lst = [item for item in lstnum if item >= 0] 
print('list after removing negative values =',res_lst)

Output:-
[27, 1000, 0, 56]
```

### **Ques. Remove negative values from a list with the filter function?**
```python
def remove_negatives(x):
    return True if x >= 0 else False
    
a = [-10, 27, 1000, -1, 0, -30]
b  = [x for x in filter(remove_negatives, a)] 
print(b)

# Using for Comprehension
res = [ele for ele in test_list if ele > 0]
print("List after filtering : " + str(res))
```