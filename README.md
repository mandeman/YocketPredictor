## Dead Project. Does not work anymore.

# YocketPredictor
Crawls Yocket for student data. Predicts accepts or rejects based on GRE, TOEFL, CGPA and WorkEx. Not to be taken seriously because a lot of factors go into consideration of your score.
Steps:
1. Run Yocket.py first.
2. Copy the link for the admits page of a given university from Yocket. For example, https://yocket.in/applications-admits-rejects/44-texas-a-and-m-university-college-station/2. The reject link is just replacing the 2 in the end with a 3.
3. Run the program. The data for the university will be pickled and saved on your machine for local predictions.
4. Run PredictionLogic.py for predictions based on pickled data saved on your PC.

Notes: 
1. Only one college's accept/reject data can be pickled at a time. I was too lazy to include ways to allow multiple pickles.
2. Don't get disappointed.
