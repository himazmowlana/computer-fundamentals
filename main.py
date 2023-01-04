import csv
import matplotlib.pyplot as plt


file = open('charts.csv')
csv_reader = csv.reader(file)

headers = []
headers = next(csv_reader)

rows = []
for r in csv_reader:
    rows.append(r)


def bye():
    print("Goodbye!")

def top_ranked_song_for_a_particular_day():
    particular_day = input("Enter the date you wish to see results for in yyyy-mm-dd format:\n")
    songs_of_the_day = []
    for i in range(0,len(rows)-1):
        if particular_day in rows[i]:
            songs_of_the_day.append(rows[i])
    print("----------------------------------------------------------------------------------")
    print(f"\nTop ranked songs for the date {particular_day}\n")
    for i in range(0, 10):
        print(f"   {songs_of_the_day[i][1]}. {songs_of_the_day[i][2]} by {songs_of_the_day[i][3]}")
    print("----------------------------------------------------------------------------------\n")
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()


def songs_of_an_artist():
    artist = input("Enter the name of the artist:\n")
    artists_songs = []
    for i in range(0,len(rows)):
        if artist in rows[i][3]:
            artists_songs.append(rows[i][2])
    artists_songs_final = []
    for i in artists_songs:
        if i not in artists_songs_final:
            artists_songs_final.append(i)
    print("----------------------------------------------------------------------------------")
    print(f"Some songs of {artist} are:\n")
    for i in range(0,20):
        print(f"{i+1}. {artists_songs_final[i]}")
    print("----------------------------------------------------------------------------------")
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()

def find_artist_of_a_song():
    song=input("Enter the name of the song:\n")
    print("----------------------------------------------------------------------------------")
    for i in range(0,len(rows)):
        if song in  rows[i][2]:
            print(f"The song: {song} \nThe artist(s): {rows[i][3]}")
            break
    print("----------------------------------------------------------------------------------")
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()

def history_of_the_song():
    name_of_song = input("Enter the name of the song:\n")
    print("----------------------------------------------------------------------------------")
    print(f"Details for the song {name_of_song}")
    for i in range(0,len(rows)):
        if name_of_song in rows[i][2]:
            print(f"Date: {rows[i][0]}, Artist(s): {rows[i][3]}, Rank: {rows[i][1]}, Peak Rank: {rows[i][5]}, Weeks on board: {rows[i][6]}")
        else:
            pass
    print("----------------------------------------------------------------------------------")
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()
        

def visualise_the_top_songs():
    ranks = []
    song_name = []
    for i in range(0,len(rows)):
        ranks.append(rows[i][1])
        song_name.append(rows[i][2])
    plt.plot(ranks, song_name)
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()

def main():
    print("----------------------------------------------------------------------------------")
    print("\nHello there! Please choose an option from the following:\n")
    print("1 - Retreive the details for the top ranked song for a particular day\n")
    print("2 - Retrieve the songs of an artist by the name\n")
    print("3 - Retrieve the name of the artist of a song\n")
    print("4 - Retrieve the history of a song by the name of the song\n")
    print("5 - Visualise the songs according to the ranks\n")
    print("M - Main menu\n")
    print("Q - Quit")
    print("----------------------------------------------------------------------------------")
    
    while True:
        choice = input("Please enter your choice: \n")
        if choice == "Q" or choice == "q":
            bye()
            break
        elif choice == "M" or choice == "m":
            main()
        elif choice == "1":
            top_ranked_song_for_a_particular_day()
        elif choice == "2":
            songs_of_an_artist()
        elif choice == "3":
            find_artist_of_a_song()
        elif choice == "4":
            history_of_the_song()
        elif choice == "5":
            visualise_the_top_songs()
            
        else:
            print("Please enter a valid choice!")
            main()
        break

main()