# This is an e_voting system in python written by 
# Eric Nkaka 
candidate_1=input("Enter the First Candidate to contest: ")
candidate_2=input("Enter the second Candidate to contest: ")

cand_1=0
cand_2=0

voters_id=[1,2,3,4,5,6]

no_of_voters=len(voters_id)

while True:
    if voters_id==[]: #to check if the list of voters is empty
        print("=============================")
        print("Voting session is now over!!")
        print("=============================")
        if cand_1>cand_2:
            percent=(cand_1/no_of_voters)*100
            print("{} has won election with {}%".format(candidate_1,percent))
            break #getting rid of infinity loop
        if cand_2>cand_1:
            percent=(cand_2/no_of_voters)*100
            print("{} has won election with {}%".format(candidate_2,percent))
            break 
        else:
            print("Both got equal number of vote! No winner.")
            break
    voter=int(input("Enter Your Id to vote: "))
    if voter in voters_id:
        print("You are now a voter.") 
        voters_id.remove(voter)#This remove a voter so that no one vote twice.
        print("------------------------------------------")
        print("Enter key 1 to vote for {}".format(candidate_1))
        print("Enter key 2 to vote for {}".format(candidate_2))
        print("Please to vote choose between 1 and 2 only.")
        print("------------------------------------------")
        vote=int(input("Enter a given candidate Key you want to vote: "))
        if vote==1:
            cand_1+=1
            print(f"Thank you for your important vote for {candidate_1}")
        elif vote==2:
            cand_2+=1
            print(f"Thank you for your important vote for {candidate_2}")
        else:
            print("Invalid key! Please choose between 1 and 2")
    else:
        print("Your are not a voter or you have already voted")
    





