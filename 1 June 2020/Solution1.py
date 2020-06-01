from array import *
votes = array('i',[])
numberOfVotes = int(input("Enter number of votes: "))
for i in range(numberOfVotes):
    vote = int(input("Enter Candidate Number: "))
    votes.append(vote)
def searchWinner(votes):
    size = len(votes)
    maxCount = 0
    winner = 0
    for i in range(size):
        votes[votes[i]%size] += size
    for i in range(0,size):
        if(votes[i]/size>maxCount):
            maxCount=votes[i]/size
            winner=i
    return winner
result = searchWinner(votes)
print("Winner is Cadidate: ",result)