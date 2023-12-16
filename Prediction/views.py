
from django.shortcuts import render
import pickle


file = open("rf_tuned.pkl",'rb')
object_file = pickle.load(file)

t=[]
for i in range(56):
    t.append(0)
new_var = [t]
predict =object_file.predict(new_var)
print([predict[0]])
