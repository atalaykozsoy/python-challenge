
import csv
import os
import itertools

candidates = []
total_votes = 0


csvpath = os.path.join('PyPoll.csv')
with open(csvpath, newline='') as votes:
  csvreader = csv.DictReader(votes)

  for row in itertools.islice(csvreader, 1, None):
    
    
    if row["Candidate"] not in candidates:
      total_votes += 1
      candidates.append(row["Candidate"])
    else: 
      total_votes += 1
      


i = 0

length = len(candidates)
vote_count = [0] * length 


with open(csvpath, newline='') as votes:
  csvreader = csv.reader(votes)
  for row in itertools.islice(csvreader, 1, None): 
    
    
    for i in range(length):
      if row[2] == candidates[i]:
        vote_count[i] += 1


j = 0       
percent_votes = []
      

for j in range(length):
  pv = round(vote_count[j] / total_votes * 100.00, 2)
  percent_votes.append(pv)


max_votes = max(vote_count)

max_index = vote_count.index(max_votes)

election_winner = candidates[max_index]



print("Election Results")
print("---------------------------------------------------")
print("Total votes: " + str(total_votes))
print("---------------------------------------------------")
for (x, y, z) in zip(candidates, percent_votes, vote_count):
    print( x ,":", y,"%", z )
print("---------------------------------------------------")
print("Winner: " + str(election_winner))
  

txtpath = ("results.txt")

with open(txtpath, "w") as txtfile:
    txtfile.write("   Election Results   \n")
    txtfile.write("----------------------\n")
    txtfile.write(("Total votes: " + str(total_votes) + "\n")
    txtfile.write("----------------------\n")
    txtfile.write
    txtfile.write("----------------------\n") 
    txtfile.write("Winner: " + str(election_winner)) + "\n")  


# csvpath = os.path.join("Results", filename)
# with open(csvpath, "w") as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerows(zip(candidates, percent_votes, vote_count))