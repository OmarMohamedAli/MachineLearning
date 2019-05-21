
# for String 

def Linear_Search(X):
    for ch in X :
        if ch=='H':
            print('character index : ', X.index(ch))
            break 

X='MACHINELEARNING'
Linear_Search(X)

print('--------------------------------')

# for List

def Linear_Search(X):
    for ch in X :
        if ch=='A':
            print('character index : ', X.index(ch))
            break 

X=['M','A','C','H','I','N','E']
Linear_Search(X)

print('--------------------------------')

# for Tuple

def Linear_Search(X):
    for ch in X :
        if ch=='C':
            print('character index : ', X.index(ch))
            break 

X=('M','A','C','H','I','N','E')
Linear_Search(X)






