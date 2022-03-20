from lib.getchlib import getch

done = False
while not done:
    print("\n" * 100)
    print("  GET TO FINISH ROOM #1!")
    c = getch()
    done = c == "q"
