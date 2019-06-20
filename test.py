import pickle
a = ["Aalm","Geer","Rana"]
f = open("object_pickle.pkl", "wb")
d = pickle.dump(a, f) # picking of object

f.close()

