def infinite_chai():
    count =1 
    while True:
        yield f"refille #{count}"
        count +=1

# !! While loop is used to create infinite loop and dangerous if it was normal return but with yield it is controlled. 


refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))
    