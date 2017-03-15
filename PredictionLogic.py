from sklearn import tree
import pickle

#Rough calculations to equalize GPA, CGPA and percentage.
def conv(u):
    if(u < 4):
        u = u * 21.5
    elif(u <= 10):
        u = u * 8.5
    return u

#Opening pickled lists for local predictions
with open ('admit_prof_arr', 'rb') as fp:
    admit_prof_arr = pickle.load(fp)
with open ('reject_prof_arr', 'rb') as fp:
    reject_prof_arr = pickle.load(fp)

admit_arr = ["Accept"]*len(admit_prof_arr)
print("Total number of admits : " + str(len(admit_arr)))
reject_arr = ["Reject"]*len(reject_prof_arr)
print("Total number of rejects : " + str(len(reject_arr)))

tsx = admit_prof_arr + reject_prof_arr
tsy = admit_arr + reject_arr

clf = tree.DecisionTreeClassifier()
clf = clf.fit(tsx, tsy)

gre = float(input("Enter your GRE score : "))
toefl = float(input("Enter your TOEFL score : "))
gpa = conv(float(input("Enter GPA : ")))
we = float(input("Enter Work Ex : "))

prediction = clf.predict([[gre, toefl, gpa, we]])

print(prediction)