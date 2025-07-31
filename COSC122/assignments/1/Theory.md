# Part A: Sequential/Linear search

### 1: 
_What is the worst case big-O complexity for the number of comparisons made by the
linear/sequential method (to identify all stolen cars sighted by the camera) given there
are n items in the stolen list and m items in the sighted list?_

For each iteration of the `sighted_plates` list the search also has to iterate through `stolen_plates`. At worse 
`sighted_plates` would not contain any of `stolen_plates` and there be `n` operations for each iteration of `m`, thus a 
total of `n*m` operations. This would look like:
```python
stolen  = ['AL530', 'PG609', 'ZU1800']                          # n = 3
sighted = ['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']    # m = 5
print(linear_stolen_plate_finder(stolen,sighted))
```
With 3 `stolen` and 4 `sighted` for a total 12 operations.

Some improvements could be to copy the stolen list and remove an element each time to shorten the amount of iterations 
of `stolen_plates` needed.

### 2:
_What is the best case big-O complexity for the number of comparisons made by the
linear/sequential method (to identify all stolen cars sighted by the camera) given there
are n items in the stolen list and m items in the sighted list, AND n > m?_

The best case would be when `sighted_plates` is in the same (consecutive) order as `stolen_plates` so that there would 
be no redundant checks (other than values already checked). When it is in this order the algorithm would only have to 
check `stolen_plates` up to the index +1 of the current item in `sighted_plates`, with the total number of comparsions 
being: m*(m + 1) / 2 or time complexity O(m^2). Example code of this situation is as follows:  
```python
stolen  = ['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']    # n = 5
sighted = ['MT2703', 'SE2025', 'SP8651']                        # m = 3
print(linear_stolen_plate_finder(stolen,sighted))
```

Side note: the early termination of the loop is never reached as `len(result_list)` is always greater than
`len(stolen_plates)` as n > m.

### 3:
_Give the equation for the number of comparisons used by the linear/sequential method
(to identify all stolen cars sighted by the camera) given there are n items in the stolen
list, n items in the sighted list AND that all the number plates in the sighted list are also
in the stolen list._

With the lists being of equal length and containing the same items (with potentially different order), each plate would 
take its index in the stolen list (+1) comparisons to be found, thus it would be the sum all the positions (`p`) in the 
`stolen_list` for each item (`i`) the `sighted_list`.
```python
stolen  = ['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']    # n = 5
sighted = [ 'SP8651', 'MT2703', 'LI3565', 'SE2025', 'PK4720']   # m = 5

#sighted[0] = stolen[2] so 2 + 1 = 3 comparisons
#sighted[1] = stolen[0] so 0 + 1 = 1 comparisons
#sighted[2] = stolen[4] so 4 + 1 = 5 comparisons
#sighted[3] = stolen[1] so 1 + 1 = 2 comparisons
#sighted[4] = stolen[3] so 3 + 1 = 4 comparisons
```
With a total of 3 + 1 + 5 + 2 + 4 = 14 comparisons.

# Part B: Binary Search

### 1:
_What is the worst case big-O complexity for the number of comparisons made by the
binary search method (to identify all stolen cars sighted by the camera) given there are
n items in the stolen list and m items in the sighted list?_

The worst case is when the stolen plate is not in the `sighted_plates` list, causing the list to be halfed the maximum 
amount of times for a list of size `n`. Because of this the list needs to be recursively halved until there is only one 
item a total of `m` times,  which causes the time complexity of the comparisons to be O(m * log(n)). An example of this 
happening would be in this situation:

```python
stolen  = ['AL530', 'PG609', 'ZU1800', "HI1234"]                # n = 4
sighted = ['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']    # m = 5    
print(linear_stolen_plate_finder(stolen,sighted))
```
With 5 * log2(4) = 10 total operations.

### 2: 
_What is the best case big-O complexity for the number of comparisons made by the
binary search method given there are n items in the stolen list and m items in the sighted
list?_

For my method, the best case is the same as the worse case as the item is not checked to be in the list until after the 
search has been reduced to the last item and therefore still has a complexity of O(m * log(n)). The only difference 
between the two situations would   

Note: This is different for other binary searches that may perform multiple checks per iteration as items in the middle 
of the list will have time complexity O(1) as they are found immediately. The overall time complexity would be O(m).