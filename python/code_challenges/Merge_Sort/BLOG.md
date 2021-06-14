# Trace
## Sample list = [8,4,23,42,16,15]
#### Pass 1:
* list =[8,4,23,42,16,15]
* Split the list into two halves
* left = [8,4,23]
* right = [42,16,15]

#### Pass 2:
* left-list=[8,4,23]
* Split the first half (left) list into two halves
* left-left=[8,4]
* right-left=[23]

#### Pass 3 :
* left-left-list = [8,4]
* Split this list into left =[8] and right =[4] and sort and merge them >> [4,8]

#### Pass 4 :
* Merge the left-left-list after we sorted it and right-left list in a way that they stay sorted 
* left-list=[4,8,23]

#### Pass 5 :
* right-list =[42,16,15]
* Split the second half list into two halves
* left-right=[42,16]
* right-right=[15]

#### Pass 6 :
* left-right-list=[42,16]
* Split this list into left =[42] and right =[16] and sort and merge them >> [16,42]

#### Pass 7 :
* Merge the left-right-list after we sorted it and right-right list in a way that they stay sorted 
* right-list=[15,16,42]

#### Pass 8:
* Sort and merge the final two halves
* the list after it sorted= [4,8,15,16,23,42]

