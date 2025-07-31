# Part A: Sequential/Linear search

### 1: 
_What is the worst case big-O complexity for the number of comparisons made by the
linear/sequential method (to identify all stolen cars sighted by the camera) given there
are n items in the stolen list and m items in the sighted list?_

For each iteration of the `sighted_plates` list the search also has to iterate through `stolen_plates`. At worse 
`sighted_plates` would not contain any of `stolen_plates` and there be `n` operations for each iteration of `m`, thus a 
total of `n*m` operations. This would look like:
```python

stolen=['SP8651', 'PK4720', 'ZU1800']
sighted=['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']
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

stolen=['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']
sighted=['MT2703', 'SE2025', 'SP8651']
print(linear_stolen_plate_finder(stolen,sighted))
```

Side note: the early termination of the loop is never reached as `len(result_list)` is always greater than
`len(stolen_plates)` as n > m.

### 3:
_Give the equation for the number of comparisons used by the linear/sequential method
(to identify all stolen cars sighted by the camera) given there are n items in the stolen
list, n items in the sighted list AND that all the number plates in the sighted list are also
in the stolen list_

With the lists being of equal length and containing the same items (with potentially different order), each plate would 
take its index in the stolen list (+1) comparisons to be found, thus it would be the sum all the positions (`p`) in the 
`stolen_list` for each item (`i`) the `sighted_list`.
```python

stolen =['MT2703', 'SE2025', 'SP8651', 'PK4720', 'LI3565']
sighted=['SP8651', 'MT2703', 'LI3565', 'SE2025', 'PK4720']

#sighted[0] = stolen[2] so 2 + 1 = 3 comparisons
#sighted[1] = stolen[0] so 0 + 1 = 1 comparisons
#sighted[2] = stolen[4] so 4 + 1 = 5 comparisons
#sighted[3] = stolen[1] so 1 + 1 = 2 comparisons
#sighted[4] = stolen[3] so 3 + 1 = 4 comparisons
# 3 + 1 + 5 + 2 + 4 = 14
```

