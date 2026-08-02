# numpy vs lists 
    lists - slow numpy - fast 
## numpy uses fixed type (why its fast)
     5 - 00000101 -> numpy -> converts to int 32 (4byte) but we can specify to int 16 or int 8

    5 - 00000101 ->lists-> lot more info to store uses a built in int type it consist of object value , object type , refernce count , size therefore when in binary its very long 

    therefore since numpy uses less bytes of memory its faster 
    when iterating through numpy array we dont need to type check
    hence faster

## numpy also uses contiguous memory making it faster
    information are not next to each other inmemory in lists making harder to find each items so takes time
    while a numpy array of size 8 will have a continuous memory therefore easy to find teh items 

    SIMD vector processing in processors makes numpy even faster 
    numpy has effective cache utilization
### what is SIMD (learn it when you have time)

## How are lists different from numpy
    numpy can do what lists can + more will cover later 
## Application of numpy
    - mathematics (matlab replacement)
    - plotting 
    - backend (pandas , connect 4, Digital photography)
    - machine learning (tensors and all)

