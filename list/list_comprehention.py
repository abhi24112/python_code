'''Example
x=1
y=1
z=2
n=3
All permutations of [i, j, k] are:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2), [1, 0, 0], [1, 0, 1), [1, 0, 2], [1, 1, 0), [1, 1, 1), [1, 1, 2]].
Print an array of the elements that do not sum ton=3.
[[0, 0, 0), [0, 0, 1], [0, 0, 2), [0, 1, 0], [0, 1, 1], [1, 0, 0), [1, 0, 1], [1, 1, 0), [1, 1, 2]]
Input Format
Four integers æ, y,zand n, each onaseparate line.
Constraints
Print the list in lexicographic increasing order.'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k)!=n])