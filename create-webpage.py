#Jason Olmos
#midterm - Character Webpage Creator
#<10/15/22>

print("")
print("********************************")
print("*  Character Webpage Creator   *")
print("*           Welcome!           *")
print("********************************\n")

#Request user to enter a name for the file to that will be created along with the name and description of the character,
#Also requests user to give and address of a picture of the character
#Each input is assigned to a variable
file_name = input("What is the name of the file?: ")
out_file = file_name + ".html"

body_h1 = input("What is the characters name?: ")
body_h1 = "<h1>" + body_h1 + "</h1>"

body_h2 = input("What is the name of the actor who plays the character?: ")
body_h2 = "<h2>" + "Played by" +  body_h2 + "</h2>"

body_description = input("Can you give us a discription of the character?: ")
body_description = "<p>" + body_description +  "</p>"

body_h2_2 = input("Enter one of their qoutes!: ")
body_h2_2 = "<h2>" + '"' + body_h2_2 + '"' + "</h2>"

body_img = input("Please enter the location or address of where you found your image: ")
body_img = '<img src="' + body_img + '" alt="' + file_name + '">\n'

vid_link = '''<a href="https://www.youtube.com/watch?v=PC4tNqdh6A8&ab_channel=JoBloMovieClips"target="_blank"> Lets watch a clip of Monty Python and the Holy Grail! </a>'''

#Combines all previous variables to a single variable
combined_body = file_name + body_h1 + body_h2 + body_description + body_h2_2 + body_img + vid_link

#This allows the program to lnow the path of where the body and header files are and 
#Reads each txt line from the txt file and assigns it to a head and footer variable.
page_head = open('assets\page-head.txt')
page_footer = open('assets\page-footer.txt')

f = open('assets\page-head.txt', "r")
combined_head = ''.join(f.readlines())
f.close()

f = open('assets\page-footer.txt', "r")
combined_footer = ''.join(f.readlines())
f.close()

#Combines all sections/variables of the webpage into a sigle variable
combined_page = combined_head + combined_body + combined_footer

#Opens the out_file and writes the data from the combined_page varible into the out_file then closes
#The file
f = open(out_file, "w")
f.write(combined_page)
f.close()

#Lets the user know that the character webpage creator file has been created with
#the file name.
print("Created {}".format(out_file))
 
