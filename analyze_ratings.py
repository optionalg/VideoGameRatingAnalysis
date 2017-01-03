import csv
import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

def is_score_valid(score):
    try:
        float(score)
        return True
    except ValueError:
        return False

users_scores = []
critic_scores = []
with open('Video_Games_Sales_as_at_22_Dec_2016.csv', 'r') as csvfile:
    row_reader = csv.DictReader(csvfile)
    for row in row_reader:
        user_score = row["User_Score"]
        critic_score = row["Critic_Score"]

        if is_score_valid(user_score) and is_score_valid(critic_score):  #make sure both scores are numbers
            users_scores.append(float(user_score))
            critic_scores.append(float(critic_score))
            
linear_rel = np.polyfit(users_scores, critic_scores, 1)  #deg = 1: linear regression
slope = linear_rel[0]
critic_intercept = linear_rel[1]

print("slope:", slope)    #slope and y-intercept
print("critic_intercept:", critic_intercept)

plt.title("User Scores vs Critic Scores for Video Games")
plt.xlabel("User Score")
plt.ylabel("Critic Score")
plt.plot(users_scores, critic_scores, 'o')  #actual data points
plt.plot(users_scores, np.polyval(linear_rel, users_scores), 'r')  #linear regression/line of best fit

plt.show()