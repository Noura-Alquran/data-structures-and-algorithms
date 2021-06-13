# Trace :
## Sample list = [15,4,6,9,7]
#### pass 1:
* min = 0
* j = 1
* temp = 4
* In the first pass, we check if there is a smaller number in the list than what is currently present in index 0. We find this smaller number in index 1. The min value gets updated >> min =1. **[15,4,6,9,7]>>[4,15,6,9,7]**

#### pass 2:
* min =1
* j = 2
* temp =6
* In the second pass, we check if there is a smaller number in the list than what is currently present in index 1. We find that all the numbers in the rest of list are smaller than 15.At result we swap 6 with 15. The min value gets updated >> min =2. **[4,15,6,9,7]>>[4,6,15,9,7]**

#### pass 3:
* min =2
* j = 3
* temp =7
* In the third pass, we check if there is a smaller number in the list than what is currently present in index 2.We find that all the numbers in the rest of list are smaller than 15.At result we swap 7 with 15.The min value gets updated >> min = 3. **[4,6,15,9,7]>>[4,6,7,9,15]**

#### pass 4:
* min =3
* j = 4
* temp =9
* In the forth pass, we check if there is a smaller number in the list than what is currently present in index 3. We find that its smaller than in 15.so it is swap with itself  **[4,6,7,9,15]>>[4,6,7,9,15]**

#### pass 5:
* min =4
* j = 5
* temp =15
* the last pass ,the last index swap itself **[4,6,7,9,15]>>[4,6,7,9,15]**


