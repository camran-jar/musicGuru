import socket			
import random
import argparse

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

    s = socket.socket()		
    print ("Socket successfully created")

    parser = argparse.ArgumentParser()

    parser.add_argument('port', type=int, help='port to listen on')

    args = parser.parse_args()

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

        c.send('1950,2009'.encode())

        clientResponse = c.recv(1024).decode()
        
        print(songSearch(clientResponse))

        c.send(songSearch(clientResponse).encode())

        # Close the connection with the client
        c.close()

        # Breaking once connection closed
        break

