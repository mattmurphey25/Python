import csv
import os

path_1 = "C:\\Users\\mattm\\python-challenge\\PyPoll\\Resources\\raw_data\\election_data_1.csv"

path_2 = "C:\\Users\\mattm\\python-challenge\\PyPoll\\Resources\\raw_data\\election_data_2.csv"

voter_num = 0
candidate_list = []
candidate_votes = []

with open(path_1, newline='') as file_1:
    voter_1 = csv.reader(file_1, delimiter=',')
    next(voter_1)
    for row in voter_1:

        voter_num = voter_num + 1

        current_candidate = row[2]
           
        if current_candidate not in candidate_list:
            candidate_list.append(current_candidate)
            candidate_votes.append(0)
            i = candidate_list.index(current_candidate)
            candidate_votes[i] += 1

        else:
            i = candidate_list.index(current_candidate)
            candidate_votes[i] += 1


with open(path_2, newline='') as file_2:
    voter_2 = csv.reader(file_2, delimiter=',')
    next(voter_2)
    for row in voter_2:
        voter_num = voter_num + 1

        current_candidate = row[2]
           
        if current_candidate not in candidate_list:
            candidate_list.append(current_candidate)
            candidate_votes.append(0)
            i = candidate_list.index(current_candidate)
            candidate_votes[i] += 1

        else:
            i = candidate_list.index(current_candidate)
            candidate_votes[i] += 1


candidate_percent = [x / voter_num for x in candidate_votes]
candidate_percent = [100 * x for x in candidate_percent]
candidate_percent = [round(x) for x in candidate_percent]

print("Election Results")
text1 = "Election Results"
print("---------------------------")
text2 = "---------------------------"
print("Total Votes: " + str(voter_num))
text3 = "Total Votes: " + str(voter_num)
print("---------------------------")
text4 = "---------------------------"


for x in range(0, len(candidate_list)):
    print(candidate_list[x] + ": " + str(candidate_percent[x]) + ".0% (" + str(candidate_votes[x]) + ")")
    
text4a = candidate_list[0] + ": " + str(candidate_percent[0]) + ".0% (" + str(candidate_votes[0]) + ")"
text4b = candidate_list[1] + ": " + str(candidate_percent[1]) + ".0% (" + str(candidate_votes[1]) + ")"
text4c = candidate_list[2] + ": " + str(candidate_percent[2]) + ".0% (" + str(candidate_votes[2]) + ")"
text4d = candidate_list[3] + ": " + str(candidate_percent[3]) + ".0% (" + str(candidate_votes[3]) + ")"
text4e = candidate_list[4] + ": " + str(candidate_percent[4]) + ".0% (" + str(candidate_votes[4]) + ")"
text4f = candidate_list[5] + ": " + str(candidate_percent[5]) + ".0% (" + str(candidate_votes[5]) + ")"
text4g = candidate_list[6] + ": " + str(candidate_percent[6]) + ".0% (" + str(candidate_votes[6]) + ")"
text4h = candidate_list[7] + ": " + str(candidate_percent[7]) + ".0% (" + str(candidate_votes[7]) + ")"

print("---------------------------")
text5= "---------------------------"

max_votes = max(candidate_votes)
max_index = candidate_votes.index(max_votes)
print("Winner: " + candidate_list[max_index])
text6 = "Winner: " + candidate_list[max_index]
print("---------------------------")
text7 = "---------------------------"
text_full = text1 + "\n" + text2 + "\n" + text3 + "\n" + text4a + "\n" + text4b + "\n" + text4c + "\n" + text4c + "\n" + text4d + "\n" + text4e + "\n" + text4f + "\n" + text4g + "\n" + text4h + "\n" + text5 + "\n" + text6 + "\n" + text7

txtpath = "C:\\Users\\mattm\\python-challenge\\PyPoll\\output\\results.txt"
with open(txtpath, "w") as txtfile:
    txtfile.write(text_full)