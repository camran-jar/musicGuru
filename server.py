import socket			
import random
import argparse

#https://www.geeksforgeeks.org/socket-programming-python/

# Function to search for song in file, search for year provided
# If year not in file, print random year and song
def songSearch(year, test=False):
    count = 0 
    
    with open('top_songs.txt', "r") as file:
        
        for line in file:
            count += 1
            if line.startswith(str(year)): #in line:
                break
        
        file.seek(0)
        
        randomNum = random.randint(1, 9)
   
        for i, line in enumerate(file, start=1):
            if i == count + randomNum + 2:
                if not test:
                    return f"In {year} the number {randomNum+1} song was {line[3:]}"
                else:
                    return [randomNum + 1, line.strip()]
                
if __name__ == '__main__':

    #testing           
    #print(songSearch(1950))

    # create a socket object
    s = socket.socket()		
    print ("Socket successfully created")

    
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument('port', type=int, help='port to listen on')

    # parse the arguments
    args = parser.parse_args()

    # assign args to variables
    port = args.port

    
    s.bind(('', port))		
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(5)	
    print ("socket is listening")		

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

    # Establish connection with client.
        c, addr = s.accept()	
        print ('Got connection from', addr )

        #send range of years
        c.send('1950,2009'.encode())

        # Get client input
        clientResponse = c.recv(1024).decode()
        
        # Ensure client response is in range, if not print random year and song
        print(songSearch(clientResponse))

        # Send song to client
        c.send(songSearch(clientResponse).encode())

        # Close the connection with the client
        c.close()

        # Breaking once connection closed
        break

