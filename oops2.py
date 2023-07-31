import pickle

#Write
my_list = [24, 65, 98, 45]
with open("oops.txt", "wb") as f:
    pickle.dump(my_list, f)

#Read
f = open("oops.txt", "rb")
ans = pickle.load(f)
print(ans)
print(type(ans))
f.close()


