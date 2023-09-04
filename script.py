import random

def songSearch(year):
    count = 0 

    with open('top_songs.txt', "r") as file:

        for line in file:
            count+=1
            if str(year) in line:
                print(count)
                break
        

        randomNum = random.randint(1,10)

        for i, line in enumerate(file, start=1):
            if i == count+randomNum:
                return(f"In {year} the number {randomNum+1} song was {line[5:]}")
            
print(songSearch(1950))