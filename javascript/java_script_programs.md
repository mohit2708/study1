### Reverse a given string?
* Using Function
```javascript
var str = "Full Stack Tutorials";
var output = str
  .split("")
  .reverse()
  .join("");
document.write(output);

Output:- slairotuT kcatS lluF
```
* Using For loop
```javascript
function reverseString(str) {
    var newString = "";
    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    document.write(newString);
}
reverseString('hello');

Output:- olleh
```

### Find the sum of all elements/numbers of a given array?
* Using for loop
```javascript
var arr = [1, 2, 5, 10, 20];
var sum = 0;
for (let i in arr) {
  sum += arr[i];
}
document.write(sum);
```

### Find the duplicate number from the array?
```javascript
let array = [6, 9, 15, 6, 13, 9, 11, 15, 20];
let obj = {}
const length = array.length;
for(let i=0; i<length; i++){
    let val = array[i]
    if(!obj[val]){
        obj[val] = 1
    }else{
        obj[val] += 1
    }
}
console.log(obj)

Output:- { '6': 2, '9': 2, '11': 1, '13': 1, '15': 2, '20': 1 }
```