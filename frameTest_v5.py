from tkinter import *
from datetime import date
import os
import asteroid_funck





todays_date = date.today()
root = Tk()
root.geometry("750x500")


# func's
def button_click_ID_numbers():
    id_input_two = int(id_input.get())

    asteroid_funck.roidFinderr(id_input_two)
    checks = os.path.isfile("asteroid_threat.txt")
    if checks == True:
        # asteroid_info_text.delete(END)
        asteroid_info_lines = open("asteroid_threat.txt", "r")
        asteroid_file_lines = asteroid_info_lines.readlines()
        count = 0
        threat_and_pass_dates.delete(0,END)
        for line in asteroid_file_lines:
            count += 1
            threat_and_pass_dates.insert(END,"{}".format(line.strip()))

        asteroid_info_lines.close()

    else:
        root.after(1000,button_click_dates())


def button_click_dates():
    asteroid_info_text.delete(0,END)
    asteroid_id_text.delete(0,END)
    start_date = user_input_Start_date.get()
    end_date = user_input_End_date.get()
    # print(start_date + "\n" + end_date)
    # print(todays_date)
    asteroid_funck.getroids(start_date,end_date)
    checks = os.path.isfile("asteroidName_speed_diamiter.txt")
    if checks == True:
        # asteroid_info_text.delete(END)
        asteroid_info_lines = open("asteroidName_speed_diamiter.txt", "r")
        asteroid_file_lines = asteroid_info_lines.readlines()
        count = 0
        for line in asteroid_file_lines:
            count += 1
            asteroid_info_text.insert(END,"{}".format(line.strip())+"")

        asteroid_info_lines.close()

    else:
        root.after(1000,button_click_dates())
    #################################################################
    checks = os.path.isfile("neo_id_made_from_astroid.txt")
    if checks==True:
        id_file_asteroid = open("neo_id_made_from_astroid.txt", "r")
        neo_file_line = id_file_asteroid.readlines()
        count = 0
        # itirates through the files line by line above three lines are with this
        for line in neo_file_line:
            count += 1
            asteroid_id_text.insert(END,"{}ID#: {}".format(count, line.strip())+ '')
    else:
        root.after(1000,button_click_dates)
    id_file_asteroid.close()
        


# StringVar() is used to catch the user input an store it. 
user_input_Start_date = StringVar()
user_input_Start_date.set("YYYY-MM-DD")
# user_input_End_date = StringVar()
# user_input_End_date.set("YYYY-MM-DD")
user_input_End_date = user_input_Start_date
id_input = StringVar()
id_input.set("ID NUMBER HERE")



# Lables

top_lable_info = Label(root, text="Enter One date not this year ")
top_lable_info.grid(pady=2,padx=1, row=0, column=0, columnspan=1)
id_input_lable = Label(root, text="Enter one of the ID numbers to see \n if it will hit earth and it approach dates")
id_input_lable.grid(row=4, column=0, columnspan=1, padx=3, pady=3,sticky=SW)
info_lable = Label(root,text="Here the name is displayed \n along with speed and diamerter").grid(row=3,column=3,columnspan=3)
id_lable = Label(root, text="Asteroid ID numbers").grid(row=3,column=6, columnspan=2,padx=3,pady=3,sticky=S)
threat_and_pass_lable = Label(root, text="Here are the pass dates and\nif will hit us!!")
threat_and_pass_lable.grid(row=7,columnspan=3,column=3)

# button

enter_button = Button(root,text="ENTER",command=button_click_dates)
enter_button.grid(row=2, column=1, padx=1, pady=3, sticky=W)
enter_but = Button(root,text="ENTER",command=button_click_ID_numbers).grid(row=5, column=1,sticky=W)



# text box
asteroid_id_text = Listbox(root, height=10, width=19)
asteroid_id_text.grid(row=4, column=6,pady=3, padx=3,columnspan=3, rowspan=3)
asteroid_info_text = Listbox(root, height=10, width=25)
asteroid_info_text.grid(row=4,column=3,columnspan=3,rowspan=3,pady=3,padx=3)
threat_and_pass_dates = Listbox(root, height=8,width=25)
threat_and_pass_dates.grid(row=8 , column=3, columnspan=3, rowspan=3,pady=3,padx=3)

# entry box
entry_box_Start_date = Entry(root, textvariable=user_input_Start_date,fg='grey')
# entry_box_End_date = Entry(root, textvariable=user_input_End_date,fg='grey')
entry_box_ID_Number = Entry(root, textvariable=id_input, fg="grey")

entry_box_Start_date.grid(row=2, column=0, sticky=W, columnspan=1)
# entry_box_End_date.grid(row=3, column=0, sticky=W, columnspan=1)
entry_box_ID_Number.grid(row=5,column=0, columnspan=1, sticky=W)

# image
# img = ImageTK.PhotoImagae(Image.open("nasa.png"))


root.mainloop()