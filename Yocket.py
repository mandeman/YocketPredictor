import urllib.request
from bs4 import BeautifulSoup
import requests
from sklearn import tree
import pickle

temp_arr = []

#Function takes a link. Returns an array with profile details.
def crawl(url, pg):
    source_code = requests.get(url + "?page="+str(pg)).text

    soup = BeautifulSoup(source_code, "html.parser")
    repeat = True

    while(repeat):
        oldlen = len(temp_arr)
        for link in soup.find_all('div', {'class': 'col-sm-3 col-xs-6'}):
            if(link.br != None):
                temp_arr.append(str(link.br.text).lstrip())

        newlen = len(temp_arr)
        if(oldlen == newlen):
            repeat = False
        pg = pg + 1
        source_code = requests.get(url + "?page=" + str(pg)).text
        soup = BeautifulSoup(source_code, "html.parser")

#Returns lists of GRE, TOEFL, % and Work Ex in a list
def lister(arr):
    tuple_arr = []
    shemparr = temp_arr

    for i in range(0, len(shemparr)):
        if (shemparr[i] == "NA " or shemparr[i] == "N.A. "):
            shemparr[i] = '0'
        shemparr[i] = float(shemparr[i].split(" ", 1)[0])

    for i in range(2, len(shemparr), 4):
        if (shemparr[i] < 4):
            shemparr[i] = shemparr[i] * 21.25
        elif (shemparr[i] < 10):
            shemparr[i] = shemparr[i] * 8.5

    # l = len(temp_arr)
    while (len(shemparr) > 0):
        o = list(shemparr[0:4])
        tuple_arr.append(o)
        shemparr = shemparr[4:]

    return tuple_arr


url = input("Enter the admit URL : ")
url = url.rstrip()

crawl(url, 1)
admit_prof_arr = lister(temp_arr)
admit_arr = ["Admit"]*len(admit_prof_arr)
print((admit_prof_arr))

with open('admit_prof_arr', 'wb') as fp:
    pickle.dump(admit_prof_arr, fp)

url = input("Enter the reject URL : ")
url = url.rstrip()
temp_arr = []

crawl(url, 1)
reject_prof_arr = lister(temp_arr)
print(reject_prof_arr)
reject_arr = ["Reject"]*len(reject_prof_arr)

with open('reject_prof_arr', 'wb') as fp:
    pickle.dump(reject_prof_arr, fp)

tsx = admit_prof_arr + reject_prof_arr
tsy = admit_arr + reject_arr

clf = tree.DecisionTreeClassifier()
clf = clf.fit(tsx, tsy)

gre = float(input("Enter your GRE score : "))
toefl = float(input("Enter your TOEFL score : "))
gpa = float(input("Enter GPA : "))
we = float(input("Enter Work Ex : "))

prediction = clf.predict([[gre, toefl, gpa, we]])
print(prediction)