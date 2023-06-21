import os
import urllib.request
import colorama
import random


def create():
    # Set up colorama for colored output
    colorama.init()

    # Define the gradient colors
    colors = [
        colorama.Fore.RED,
        colorama.Fore.YELLOW,
        colorama.Fore.GREEN,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
    ]
    # Define the particle characters
    particles = ['''                          ⣀⠀⠀⣀⣀⣀⣠⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⢀⡆⣼⣁⢠⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⢰⣾⣧⣹⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⡘⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀  ⠈⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀
    ⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠘⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   
    ⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠇⢀⣤⣤⣤⣄⠀⠀⣤⡶⠶⠶⢄⠸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣴⣏⣭⣭⣽⣽⡏⢹⠿⣶⣶⣶⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀
    ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⡌⠛⠛⠉⣽⠇⠈⢧⣈⠁⣀⡜⠉⡗⣦⠀⠀----------------------------------⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀
    ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⡇⠈⠒⠒⢊⣯⣦⣴⣬⠉⠙⠀⠀⢸⠃⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀Author : @Brownspy1⠀⠀ ⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⡀⠀⢀⣴⣛⣉⣉⣑⣢⡀⠀⢀⣼⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀  The spy battel⠀⠀ ⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣶⡀⠙⠧⣄⣤⠼⠉⠁⣠⣾⡏⠀⠀⠀⠀-----------------------------------⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣄⢀⣤⣄⠀⣀⣴⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀   
    ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⣿⣿⣿⣿⣿⡿⠛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀ 
    ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠁⢈⣿⡽⠛⠉⠀⠀⣣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
    ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣷⡀⠀⠉⠁⠀⠀⠀⠀⣀⣼⣧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀
    ⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣟⢷⣦⠀⣴⡿⣛⣽⡟⣹⣿⣿⣶⣤⣀⡀⠀⠀⠀⠀  ⠀⠀⠀⠀
    ⠀⠀⠀  ⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣼⣿⣾⣿⣿⣾⣿⣿⣿⣿⣿⣿⣏⡗⣦⣄⡀⠀ ⠀⠀
    ⠀⠀⠀⠀⠀⠱⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣹⣏⣩⣿⣿⣿⣿⣿⣿⣿⣿⣦⢹⣶⡔⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢿⣿⣿⠛⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣶⢾⣿⣿⣿⣿⠈⢿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠁⢸⣿⣿⣿⣯⣠⡆⢻⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠿⠿⣿⣿⣿⣿⣇⣀⣾⡏⠿⠿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀''']

    # Set the number of rows and columns for the image
    rows = 1
    cols = 1

    # Generate the gradient image
    for i in range(rows):
        # Choose a random color for each row
        color = random.choice(colors)

        # Print the particles in the row with the chosen color
        for j in range(cols):
            particle = random.choice(particles)
            print(f"{color}{particle}", end="")
        print()

    # Reset colorama to default settings
    colorama.deinit()

    code_name = input("Your Code Name: ")
    meta_title = input("Your Meta Title: ")
    # team_name = input("Your team name: ")

    file_content = f"""
<html>
<head>
    <title>{meta_title}</title>
    <meta property="og:image" content="https://media.giphy.com/media/3oriNM8HF8oijarwre/giphy.gif">
    <meta name="description" content="FAKE LOVE:)">
    <link href="https://fonts.googleapis.com/css?family=Kelly+Slab" rel="stylesheet">
    <link rel="stylesheet" href="https://itcoursem.000webhostapp.com/style.css">
</head>
<body>
    <canvas id="matrix-effect"></canvas>
    <center>
        <div class="tengahken">
            <img src="https://k.top4top.io/p_2728blb0i1.gif" height="35%">
            <br>
            <b><font size="5px">i am a muslim hacker that's enough to describe me</b></font>
            <br>
            <font size="4px">I love you but you don't love me back :)</font><br>
            <br>
            <br>
        </div>
        <b><font class="usar1" size="2px">Hack by: </font></b>
        <font class="usar" size="2px">{code_name}</font>
    </center>
    <script src="https://itcoursem.000webhostapp.com/app.js"></script>
    
</body>
</html>"""

    with open("Deface.html", "w") as file:
        file.write(file_content)

    os.system("clear")
    os.system("cp Deface.html /sdcard")
    print("\033[1;35m This Deface page saved to your phone storage\n")
    print("Thanks for using this tool\n")


def download():
    print("\n"
          "                    ▄───▄\n"
          "                    █▀█▀█\n"
          "                    █▄█▄█\n"
          "                    ─███──▄▄\n"
          "                    ─████▐█─█\n"
          "                    ─████───█\n"
          "                    ─▀▀▀▀▀▀▀\n"
          "    ")

    print("\n")
    print("\033[1;32m ------‐---------------------------------------------")
    print("\n")
    print("\033[1;36m               Author : Brownspy1     ")
    print("\n")
    print("\033[1;36m                 The spy battel      ")
    print("\n")
    print("\033[1;32m -----‐-----------‐----------------------------------")
    print("\n")

    url = input("Enter the deface URL: ")

    try:
        response = urllib.request.urlopen(url)
        deface_content = response.read().decode()

        with open("Deface.html", "w") as file:
            file.write(deface_content)

        os.system("clear")
        os.system("cp Deface.html /sdcard")
        print("\033[1;35m       This Deface page saved to your phone storage\n")
        print("Thanks for using this tool\n")

    except Exception as e:
        print("Error: Failed to download the deface page.")
        print(f"Reason: {str(e)}\n")


while True:

    print("""
┏━━┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏┓━
┃┏┓┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏┛┃━
┃┗┛┗┓┏━┓┏━━┓┏┓┏┓┏┓┏━┓━┏━━┓┏━━┓┏┓━┏┓┗┓┃━
┃┏━┓┃┃┏┛┃┏┓┃┃┗┛┗┛┃┃┏┓┓┃━━┫┃┏┓┃┃┃━┃┃━┃┃━
┃┗━┛┃┃┃━┃┗┛┃┗┓┏┓┏┛┃┃┃┃┣━━┃┃┗┛┃┃┗━┛┃┏┛┗┓
┗━━━┛┗┛━┗━━┛━┛┗┛┗━┛┗┛┗┛┗━━┛┗━━┛┗━━━┛┗━━┛
    """)

    print("\n")
    print("\033[1;32m ------‐---------------------------------------------")
    print("\033[1;36m               Author : Brownspy1    ")
    print("\033[1;36m                 The spy battel      ")
    print("\033[1;32m -----‐-----------‐----------------------------------")
    print("\n")

    print("Please select an option:")
    print("1. Create a deface page")
    print("2. Download a deface page")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        create()
    elif choice == "2":
        download()
    elif choice == "3":
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
