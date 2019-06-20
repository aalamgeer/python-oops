import pickle
a = ["Aalm","Geer","Rana"]
f = open("object_pickle.pkl", "rb")
d = pickle.load(f)

f.close()

