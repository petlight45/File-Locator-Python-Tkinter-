from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
import time
import shutil
from playsound import playsound

if not(os.path.exists(os.path.join(os.getcwd(), "data"))):
    os.mkdir(os.path.join(os.getcwd(), "data"))

try:
    os.remove(os.path.join(os.getcwd(),"data/temp.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/temp_drive_old.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/temp_drive_new.txt"))
except FileNotFoundError:
    pass
state_file = open("data/sound_state.txt", "w")
state_file.write("ss_on")
state_file.close()
beep_comp_file = open("data/beep_complete.txt", "w")
beep_comp_file.write("2")
beep_comp_file.close()
beep_abort_file = open("data/beep_aborted.txt", "w")
beep_abort_file.write("1")
beep_abort_file.close()

root = Tk()
root.focus_force()
root.title("File Locator")
root.geometry("500x500")
root.configure(bg="#9F0134")

def set_bind(event):
    settings()

root.bind("<Shift-s>",  set_bind)
root.bind("<Shift-S>",  set_bind)

def about_bind(event):
    about()

root.bind("<Shift-a>",  about_bind)
root.bind("<Shift-A>",  about_bind)

def root_destroy(event):
    root.destroy()

root.bind("<Escape>", root_destroy)

root.resizable(0,0)
sound_state_check_var = StringVar()
try:
    root.iconbitmap("data/icon_main.ico")
except TclError:
    pass
menu_root = Menu(root,tearoff=0)
menu_root.add_command(label="Settings[Shift+S]", command=lambda:settings())
menu_root.add_command(label="About[Shift+A]", command=lambda : about())
menu_root.add_command(label="Exit[ESC]", command=lambda :root.destroy())
root.configure(menu=menu_root)
canvas1 = Canvas(root, height=500, width=500)
canvas1.pack()
root.update_idletasks()
root.update()

def about():
    win_about = Toplevel()
    win_about.focus_force()
    win_about.title("About")
    win_about.geometry("300x300")
    win_about.resizable(0,0)

    def about_ret(event):
        win_about.destroy()

    win_about.bind_all("<Escape>", about_ret)
    try:
        win_about.iconbitmap("data/icon_about.ico")
    except TclError:
        pass
    font1 = ("Cambria", 12, "bold")
    font2 = ("Cambria", 10, "italic")
    font3 = ("Cambria", 8, "italic")
    canvas3 = Canvas(win_about, height=300, width=300)
    canvas3.pack()
    try:
        global image1
        canvas3.create_image(150, 150, image=image1)
        back_col = "#9F0134"
        f_back_col = "White"
        f_g = "Black"
    except NameError:
        back_col = "White"
        f_back_col = "Black"
        f_g = "Black"
    canvas3.create_text(150, 150,justify=CENTER, fill=f_back_col, font=font2, text="File Locator v1.0\nThis software was created by Faboyede Peterlight,\nDepartment of Civil Engineering(200L),\nFederal University of Technology,\nAkure Town,\nOndo State.\nNigeria\nEmail adress: Petlight45@yahoo.com\nMobile Number: 09060990102")
    root.update_idletasks()
    root.update()
    canvas3.update()
    canvas3.update_idletasks()


def settings():
    try:
        os.remove(os.path.join(os.getcwd(), "data/temp_drive_new.txt"))
    except FileNotFoundError:
        pass
    win_sett = Toplevel()
    win_sett.focus_force()
    win_sett.title("Settings")
    win_sett.geometry("500x500")
    win_sett.resizable(0,0)

    def but_app_ret(event):
        apply_settings()

    win_sett.bind("<Return>", but_app_ret)

    def but_back_ret(event):
        back_settings()

    win_sett.bind("<Escape>", but_back_ret)

    def but_add_ret(event):
        add_drive()

    win_sett.bind("A", but_add_ret)
    win_sett.bind("a", but_add_ret)

    def but_clear_ret(event):
        clear_drive()

    win_sett.bind("C", but_clear_ret)
    win_sett.bind("c", but_clear_ret)


    try:
        win_sett.iconbitmap("data/icon_settings.ico")
    except TclError:
        pass
    font1 = ("Cambria", 12, "bold")
    font2 = ("Cambria", 10, "italic")
    font3 = ("Cambria", 8, "italic")
    canvas2 = Canvas(win_sett, height=500, width=500)
    canvas2.pack()
    try:
        global image1
        canvas2.create_image(250, 250, image=image1)
        back_col = "#9F0134"
        f_back_col = "White"
        f_g = "Black"
    except NameError:
        back_col = "White"
        f_back_col = "Black"
        f_g = "Black"
    listbox_drives = Listbox(canvas2, fg=f_back_col, bg=back_col, font=font3, height=3)
    try:
        drive_file = open("data/temp_drive_old.txt", "r")
        line = 0
        for text in drive_file.readlines():
            if line == 0:
                listbox_drives.insert(0, text)
                line += 1
            else:
                listbox_drives.insert(END, text)
        drive_file.close()
    except FileNotFoundError:
        listbox_drives.delete(0, END)
        listbox_drives.insert(0, "No Drive(s) Added")
    canvas2.create_text(250, 20, text="Settings",font=font1, fill=f_back_col)
    canvas2.create_window(350, 460, window=Button(canvas2, fg=f_back_col, bg=back_col, text="Back[ESC]", command = lambda :back_settings()))
    canvas2.create_window(450, 460, window=Button(canvas2, fg=f_back_col, bg=back_col, text="Apply[Enter]", command = lambda :apply_settings()))
    canvas2.create_text(250, 60, text="Drives to search!!",font=font2, fill=f_back_col)
    canvas2.create_window(200, 90, window=Button(canvas2, fg=f_back_col, bg=back_col, text="Add Drive(s)[A]", command = lambda :add_drive(), font=font3))
    canvas2.create_window(300, 90, window=Button(canvas2, fg=f_back_col, bg=back_col, text="Clear Drives[C]", command = lambda :clear_drive(), font=font3))
    canvas2.create_window(250, 130, window=listbox_drives)
    canvas2.create_text(250, 200, text="Audio Notification!!", font=font2, fill=f_back_col)
    try:
        sound_state_file = open("data/sound_state.txt", "r")
        sound_state = sound_state_file.read()
        sound_state_file.close()
    except FileNotFoundError:
        sound_state_file = open("data/sound_state.txt", "w")
        sound_state_file.write("ss_on")
        sound_state = "ss_on"
        sound_state_file.close()
    global sound_state_check_var
    sound_state_check_var.set(sound_state)
    sound_state_check = Checkbutton(canvas2, text="Enable audio notifications[SPACEBAR]",  font=font3)
    canvas2.create_window(250,240, window=sound_state_check)
    sound_state_check.configure(variable=sound_state_check_var, onvalue="ss_on", offvalue="ss_off")
    sound_state_check.configure(selectcolor=back_col, bg=back_col, fg=f_back_col, activebackground=back_col, activeforeground=f_back_col)
    sound_state_check.update_idletasks()
    sound_state_check.update()

    def change_state(event):
        if sound_state_check_var.get() == "ss_off":
            sound_state_check_var.set("ss_on")
        else:
            sound_state_check_var.set("ss_off")

    win_sett.bind("<space>", change_state)
    win_sett.bind("<space>", change_state)

    try:
        beep_comp_file = open("data/beep_complete.txt", "r")
        beep_comp_times = beep_comp_file.read()
        beep_comp_file.close()
    except FileNotFoundError:
        beep_comp_file = open("data/beep_complete.txt", "w")
        beep_comp_file.write("2")
        beep_comp_times = "2"
        beep_comp_file.close()
    canvas2.create_text(230, 260, fill=f_back_col, text="No of beep for 'Search Completed':", font=font3)
    entry_beep_comp = Entry(canvas2, font=font3, fg=f_back_col, bg=back_col)
    entry_beep_comp.insert(0, beep_comp_times)
    canvas2.create_window(330,260, window=entry_beep_comp, width=17, height=13)
    try:
        beep_abort_file = open("data/beep_aborted.txt", "r")
        beep_abort_times = beep_abort_file.read()
        beep_abort_file.close()
    except FileNotFoundError:
        beep_abort_file = open("data/beep_aborted.txt", "w")
        beep_abort_file.write("1")
        beep_abort_times = "1"
        beep_abort_file.close()
    canvas2.create_text(230, 280, fill=f_back_col, text="No of beep for 'Search Aborted':", font=font3)
    entry_beep_abort = Entry(canvas2, font=font3, fg=f_back_col, bg=back_col)
    entry_beep_abort.insert(0, beep_abort_times)
    canvas2.create_window(330,280, window=entry_beep_abort, width=17, height=13)
    root.update_idletasks()
    root.update()
    canvas2.update()
    canvas2.update_idletasks()

    def add_drive():
        add_drive_win = Toplevel(root)
        add_drive_win.focus_force()
        add_drive_win.resizable(0,0)
        add_drive_win.geometry("150x150")
        add_drive_win.title("Add Drive")

        def but_app_dr_ret(event):
            add_drive_2()

        add_drive_win.bind("<Return>", but_app_dr_ret)

        def but_back_dr_ret(event):
            add_drive_win.destroy()

        add_drive_win.bind("<Escape>", but_back_dr_ret)
        try:
            add_drive_win.iconbitmap("data/icon_settings.ico")
        except TclError:
            pass
        canvas_add_win = Canvas(add_drive_win, height=150, width=150, bg=back_col)
        canvas_add_win.pack()
        entr_drive_var = StringVar()
        entry_drives_add = Entry(canvas_add_win, bg="White", fg="Black", font=font2, textvariable=entr_drive_var, justify=CENTER)
        entry_drives_add.focus_force()
        canvas_add_win.create_text(75,20, text="Drive:", font=font2, fill=f_back_col)
        canvas_add_win.create_window(75,40,window=entry_drives_add, width=40)


        def add_drive_2():
            if os.path.exists(os.path.join(os.getcwd(), "data/temp_drive_new.txt")):
                drive_file = open("data/temp_drive_new.txt", "r")
                for text in drive_file.readlines():
                    if entr_drive_var.get().upper() + ":" in text:
                        messagebox.showerror("Error", "Path Already Added")
                        add_drive_win.focus_force()
                        entry_drives_add.focus_force()
                        return
            elif os.path.exists(os.path.join(os.getcwd(), "data/temp_drive_old.txt")):
                old_drive_file = open("data/temp_drive_old.txt", "r")
                for text in old_drive_file.readlines():
                    if entr_drive_var.get().upper() + ":" in text:
                        messagebox.showerror("Error", "Path Already Added")
                        add_drive_win.focus_force()
                        entry_drives_add.focus_force()
                        return
            if os.path.exists(entr_drive_var.get() + ":/"):
                entr_drive_var.set(entr_drive_var.get().upper())
            elif os.path.exists(entr_drive_var.get().upper() + ":/"):
                entr_drive_var.set(entr_drive_var.get().upper())
            else:
                messagebox.showerror("Error", "Invalid Path!!")
                return
            try:
                drive_file = open("data/temp_drive_new.txt", "r")
                drive_file.close()
                drive_file = open("data/temp_drive_new.txt", "a")
                drive_file.write("\nDrive " + entr_drive_var.get() + ":")
                listbox_drives.insert(END, "Drive " + entr_drive_var.get() + ":")
                root.update_idletasks()
                root.update()
                canvas2.update()
                canvas2.update_idletasks()
                drive_file.close()
            except FileNotFoundError:
                if os.path.exists(os.path.join(os.getcwd(), "data/temp_drive_old.txt")):
                    drive_file = open("data/temp_drive_new.txt", "w")
                    old_drive_file = open("data/temp_drive_old.txt", "r")
                    drive_file.write(old_drive_file.read())
                    drive_file.close()
                    old_drive_file.close()
                    drive_file = open("data/temp_drive_new.txt", "a")
                    drive_file.write("\nDrive " + entr_drive_var.get() + ":")
                    drive_file.close()
                    listbox_drives.insert(END, "Drive " + entr_drive_var.get() + ":")
                    root.update_idletasks()
                    root.update()
                    canvas2.update()
                    canvas2.update_idletasks()
                else:
                    drive_file = open("data/temp_drive_new.txt", "w")
                    drive_file.write("Drive " + entr_drive_var.get() + ":")
                    listbox_drives.delete(0, END)
                    listbox_drives.insert(0, "Drive " + entr_drive_var.get() + ":")
                    root.update_idletasks()
                    root.update()
                    canvas2.update()
                    canvas2.update_idletasks()
                    drive_file.close()
            entr_drive_var.set("")

        canvas_add_win.create_window(100, 130,
                                     window=Button(canvas_add_win, fg=f_back_col, bg=back_col, font=font3, text="Add[Enter]",
                                                   command=lambda: add_drive_2()))
        menubutton_add = Menubutton(canvas_add_win, text=chr(0x00A1), fg=f_back_col, bg=back_col, font=font1,
                                    direction='above')
        canvas_add_win.create_window(40, 125, window=menubutton_add)
        menu_but_add = Menu(menubutton_add, tearoff=0, bg=back_col, fg=f_back_col)
        menubutton_add.configure(menu=menu_but_add)
        menu_but_add.add_command(label="Enter the desired drive letter in the entry given above")
        add_drive_win.update_idletasks()
        add_drive_win.update()
        add_drive_win.mainloop()

    def clear_drive():
        try:
            os.remove(os.path.join(os.getcwd(), "data/temp_drive_old.txt"))
        except FileNotFoundError:
            pass
        try:
            os.remove(os.path.join(os.getcwd(), "data/temp_drive_new.txt"))
        except FileNotFoundError:
            pass
        listbox_drives.delete(0, END)
        listbox_drives.insert(0, "No Drive(s) Added")
        root.update_idletasks()
        root.update()
        canvas2.update()
        canvas2.update_idletasks()



    def back_settings():
        canvas2.destroy()
        win_sett.destroy()
        try:
            os.remove(os.path.join(os.getcwd(), "data/temp_drive_new.txt"))
        except FileNotFoundError:
            pass

    def apply_settings():
        try:
            if int(entry_beep_abort.get()) > 10 or int(entry_beep_comp.get()) > 10:
                messagebox.showerror("Error", "No of beep times exceded!")
                return
            if int(entry_beep_abort.get()) < 1 or int(entry_beep_comp.get()) < 1:
                messagebox.showerror("Error", "Invalid no of beep times!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid no of beep times!")
            return
        if os.path.exists(os.path.join(os.getcwd(), "data/temp_drive_new.txt")):
            drive_file = open("data/temp_drive_new.txt", "r")
            old_drive_file = open("data/temp_drive_old.txt", "w")
            old_drive_file.write(drive_file.read())
            drive_file.close()
            old_drive_file.close()
        try:
            os.remove(os.path.join(os.getcwd(), "data/temp_drive_new.txt"))
        except FileNotFoundError:
            pass
        sound_state_file = open("data/sound_state.txt", "w")
        sound_state_file.write(sound_state_check_var.get())
        sound_state_file.close()
        beep_comp_file = open("data/beep_complete.txt", "w")
        beep_comp_file.write(entry_beep_comp.get())
        beep_comp_file.close()
        beep_abort_file = open("data/beep_aborted.txt", "w")
        beep_abort_file.write(entry_beep_abort.get())
        beep_abort_file.close()


class Background:
    def __init__(self,canvas, image):
        self.canvas = canvas
        self.image = image
        self.canvas.create_image(250, 250, image=self.image)
        root.update_idletasks()
        root.update()
        self.canvas.update()
        self.canvas.update_idletasks()


class Main:
    def __init__(self, canvas, state):
        self.canvas = canvas
        self.state = state
        if self.state != "Already":
            id_text = self.canvas.create_text(250, -20, text="")
            if id_text != 1:
                self.back_col = "#9F0134"
                self.f_back_col = "White"
                self.fg = "Black"
                self.entry_bg = "White"
            else:
                self.back_col = "White"
                self.f_back_col = "Black"
                self.fg = "Black"
                self.entry_bg = "White"
            self.font1 = ("Cambria", 12, "bold")
            self.font2 = ("Cambria", 10, "italic")
            self.font3 = ("Cambria", 10, "bold")
            self.canvas.create_text(250, 20, text="File Locator", fill=self.f_back_col, font=self.font1)
            self.entry_var = StringVar()
            self.canvas.create_text(250, 50, text = "Enter the name of the directory or the file you want to find below!!", fill=self.f_back_col, font=self.font2)
            self.entry_search = Entry(self.canvas, fg=self.fg, bg=self.entry_bg, font=self.font3, textvariable=self.entry_var)
            self.canvas.create_window(250, 80, window=self.entry_search, width=400)
            self.entry_search.focus_force()
            coord_y = 120
            self.button_find = Button(self.canvas, fg=self.f_back_col, bg=self.back_col, font=self.font3, text="Find![Enter]", command=lambda: self.find())
            self.canvas.create_window(250, coord_y, window=self.button_find)



            self.entry_search.bind("<Return>", self.find_ret)
            root.update_idletasks()
            root.update()
            self.canvas.update()
            self.canvas.update_idletasks()

    def find_ret(self, event):
        self.find()

    def add(self):
        pass

    def find(self):
        if os.path.exists(os.path.join(os.getcwd(), "data/temp_drive_old.txt")):
            pass
        else:
            messagebox.showerror("Error", "Select drive(s) to search")
            return
        if self.entry_var.get() == "":
            messagebox.showerror("Error", "Enter a search term")
            return
        else:
            pass
        temp_search = open("data/temp.txt", "w")
        temp_search.write("Search Term:\n" + self.entry_var.get() + "\n")
        temp_search.close()
        over_all_match_file = 0
        over_all_match_folder = 0
        over_all_index_file = 0
        over_all_index_folder = 0
        self.entry_search.configure(state=DISABLED)
        self.button_find.configure(state=DISABLED)
        self.entry_search.unbind("<Return>")
        progress_var = StringVar()
        progress_var.set("")
        files_and_folders_found_var = StringVar()
        files_and_folders_found_var.set("")
        searching_var = StringVar()
        searching_var.set("")
        searching_wind = self.canvas.create_window(250, 300,
                                                   window=Label(self.canvas, fg=self.f_back_col, bg=self.back_col,
                                                                font=self.font2,
                                                                textvariable=searching_var))
        progress_win = self.canvas.create_window(250, 340,
                                                 window=Label(self.canvas, fg=self.f_back_col, bg=self.back_col,
                                                              font=self.font2,
                                                              textvariable=progress_var))
        files_folder_win = self.canvas.create_window(250, 380,
                                                     window=Label(self.canvas, fg=self.f_back_col, bg=self.back_col,
                                                                  font=self.font2,
                                                                  textvariable=files_and_folders_found_var))
        root.update()
        root.update_idletasks()
        self.canvas.update_idletasks()
        self.canvas.update()
        list_drives = []
        old_drive_file = open("data/temp_drive_old.txt", "r")
        for drive in old_drive_file.readlines():
            list_drives.insert(-1, drive)
        old_drive_file.close()
        drives_list = []
        for drives in list_drives:
            drives_list.append(drives.replace("\n", ""))
        loop_continue = BooleanVar()
        skip_button_empty = BooleanVar()
        skip_button_empty.set(True)
        total_drive = len(drives_list)
        current_drive = 1
        for drive in drives_list:
            if len(drives_list) > 1 and skip_button_empty.get():
                button_skip_win = self.canvas.create_window(250, 160, window=Button(self.canvas, fg=self.f_back_col,
                                                                                    bg=self.back_col, font=self.font3,
                                                                                    text="Skip Drive![N]",
                                                                                    command=lambda: skip()))
                skip_button_empty.set(False)

                def skip_ret(event):
                    root.unbind("N")
                    root.unbind("n")
                    skip()

                root.bind("N", skip_ret)
                root.bind("n", skip_ret)


            if current_drive == total_drive:
                try:
                    self.canvas.delete(button_skip_win)
                except UnboundLocalError:
                    pass

            current_drive += 1

            loop_continue.set(False)

            def skip():
                loop_continue.set(True)

            drive_path = drive.replace("Drive ", "")
            drive_path = drive_path.replace(":", ":/")
            temp_search = open("data/temp.txt", "a")
            temp_search.write("\n\n------" + drive + "------")
            temp_search.close()
            searching_dot = ".."
            indexing_dot = "."

            def stop_dur_lfm():
                def help_tools():
                    help_win = Toplevel()
                    help_win.geometry("400x400")
                    help_win.resizable(0,0)
                    help_win.title("Help")
                    try:
                        help_win.iconbitmap("data/icon_main.ico")
                    except TclError:
                        pass
                    canvas_help = Canvas(help_win, bg=self.back_col, height=400, width=400)
                    canvas_help.pack()
                    canvas_help.create_text(200, 200, font=self.font2,  fill=self.f_back_col, justify=CENTER,  text="Try opening file or folder location in explorer by clicking the\n'Open File/Folder Location in Explorer' command and paste\n the file/folder link copied from the searches result\n in the given entry\n\n Try opening file by clicking the\n'Open File' command and paste the file link copied\n from the searches result\n in the given entry\n\nPress CTRL+C to copy a selected link from the searches result\n\nPress CTRL+V to paste a copied link into the entry given")
                    help_win.update()
                    help_win.update_idletasks()
                    help_win.mainloop()

                def open_ff_ex():
                    def open_ffe():
                        path = entry_link.get()
                        for num in range(0, len(path)):
                            if path[-1] == " ":
                                path = path[0:-1]
                        if os.path.exists(os.path.normpath(path)):
                            if os.path.isfile(os.path.normpath(path)):
                                direct, fil = os.path.split(os.path.normpath(path))
                                os.startfile(direct)
                                return
                            else:
                                os.startfile(os.path.normpath(path))
                                return
                        else:
                            messagebox.showerror("Error", "Invalid Link Given")
                            return

                    open_ff_win = Toplevel()
                    open_ff_win.geometry("600x200")
                    open_ff_win.resizable(0,0)
                    open_ff_win.focus_force()
                    open_ff_win.title("Open File/Folder Location in Explorer")
                    try:
                        open_ff_win.iconbitmap("data/icon_main.ico")
                    except TclError:
                        pass
                    canvas_open_ff = Canvas(open_ff_win, bg=self.back_col, height=200, width=600)
                    canvas_open_ff.pack()
                    canvas_open_ff.create_text(300, 20, text="Enter the file/folder link below", font=self.font2, fill=self.f_back_col)
                    entry_link = Entry(canvas_open_ff, bg="White", fg="Black", font=self.font3)
                    entry_link.focus_force()
                    entry_link_win = canvas_open_ff.create_window(300, 40, window=entry_link, width=560)
                    button_open = Button(canvas_open_ff, text="Open", fg=self.f_back_col, bg=self.back_col, font=self.font3, command=lambda : open_ffe())
                    canvas_open_ff.create_window(300, 80, window=button_open)
                    def open_1_ret(event):
                        open_ffe()

                    entry_link.bind("<Return>", open_1_ret)

                    def destroy_1_ret(event):
                        open_ff_win.destroy()

                    entry_link.bind("<Escape>", destroy_1_ret)

                    open_ff_win.update()
                    open_ff_win.update_idletasks()
                    open_ff_win.mainloop()


                def open_f():
                    def open_fe():
                        path = entry_link.get()
                        for num in range(0, len(path)):
                            if path[-1] == " ":
                                path = path[0:-1]
                        if os.path.exists(os.path.normpath(path)):
                            if os.path.isfile(os.path.normpath(path)):
                                direct, fil = os.path.split(os.path.normpath(path))
                                os.startfile(os.path.normpath(path))
                                return
                            else:
                                messagebox.showerror("Error", "The Link Given is not a File's")
                                return
                        else:
                            messagebox.showerror("Error", "Invalid Link Given")
                            return

                    open_f_win = Toplevel()
                    open_f_win.geometry("600x200")
                    open_f_win.resizable(0,0)
                    open_f_win.focus_force()
                    open_f_win.title("Open File")
                    try:
                        open_f_win.iconbitmap("data/icon_main.ico")
                    except TclError:
                        pass
                    canvas_open_f = Canvas(open_f_win, bg=self.back_col, height=200, width=600)
                    canvas_open_f.pack()
                    canvas_open_f.create_text(300, 20, text="Enter the file link below", font=self.font2, fill=self.f_back_col)
                    entry_link = Entry(canvas_open_f, bg="White", fg="Black", font=self.font3)
                    entry_link.focus_force()
                    def open_2_ret(event):
                        open_fe()

                    entry_link.bind("<Return>", open_2_ret)

                    def destroy_2_ret(event):
                        open_f_win.destroy()

                    entry_link.bind("<Escape>", destroy_2_ret)

                    entry_link_win = canvas_open_f.create_window(300, 40, window=entry_link, width=560)
                    button_open = Button(canvas_open_f, text="Open", fg=self.f_back_col, bg=self.back_col, font=self.font3, command=lambda : open_fe())
                    canvas_open_f.create_window(300, 80, window=button_open)
                    open_f_win.update()
                    open_f_win.update_idletasks()
                    open_f_win.mainloop()


                root_2 = Toplevel(root)
                root_2.focus_force()
                try:
                    self.canvas.delete(button_skip_win)
                except NameError or UnboundLocalError:
                    pass
                self.canvas.delete(searching_wind)
                self.canvas.delete(progress_win)
                self.canvas.delete(files_folder_win)

                def root_bind(event):
                    root_2.destroy()

                root_2.bind("<Escape>", root_bind)

                def root_y_move_down(event):
                    listbox_search.yview_moveto(1)

                root_2.bind("<Next>", root_y_move_down)

                def root_x_move_left(event):
                    listbox_search.xview_moveto(0)

                root_2.bind("<Left>", root_x_move_left)

                def root_x_move_right(event):
                    listbox_search.xview_moveto(1)

                root_2.bind("<Right>", root_x_move_right)

                def root_y_move_up(event):
                    listbox_search.yview_moveto(0)

                root_2.bind("<Prior>", root_y_move_up)

                def root_y_scroll_up(event):
                    listbox_search.yview_scroll(-10, UNITS)

                root_2.bind("<Up>", root_y_scroll_up)

                def root_y_scroll_down(event):
                    listbox_search.yview_scroll(10, UNITS)

                root_2.bind("<Down>", root_y_scroll_down)


                root_2.geometry("600x600")
                root_2.resizable(0, 0)
                try:
                    root_2.iconbitmap("data/icon_main.ico")
                except TclError:
                    pass
                root_2.title("Search Results")
                menu_search_results = Menu(root_2, font=self.font2, tearoff=0)
                root_2.configure(menu=menu_search_results)
                menu_tools = Menu(menu_search_results, font=self.font2, tearoff=0)
                menu_search_results.add_cascade(label="Tools", menu=menu_tools)
                menu_tools.add_command(label="Open File/Folder Location in Explorer", command= lambda : open_ff_ex())
                menu_tools.add_command(label="Open File", command = lambda : open_f())
                menu_tools.add_command(label="Help", command=lambda : help_tools())
                self.entry_search.configure(state=NORMAL)
                self.entry_search.focus_force()
                self.entry_search.bind("<Return>", self.find_ret)
                self.button_find.configure(text="Find![Enter}", command=lambda: self.find(), state=NORMAL)
                scrollbar_y = Scrollbar(root_2, orient=VERTICAL)
                scrollbar_y.pack(side=RIGHT, fill=Y)
                scrollbar_x = Scrollbar(root_2, orient=HORIZONTAL)
                scrollbar_x.pack(side=BOTTOM, fill=X)
                listbox_search = Listbox(root_2, height=38, font=self.font2)
                if os.path.exists(os.path.join(os.getcwd(), "data/background.jpg")):
                    listbox_search.configure(bg="#9F0134", fg="White")
                listbox_search.pack(fill=BOTH)
                listbox_search.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
                scrollbar_x.configure(command=listbox_search.xview)
                scrollbar_y.configure(command=listbox_search.yview)
                root_2.update()
                root_2.update_idletasks()
                temp_search = open("data/temp.txt", "r")
                for text in temp_search.readlines():
                    listbox_search.insert(END, text)
                    root_2.update()
                    root_2.update_idletasks()
                temp_search.close()
                root_2.update()
                root_2.update_idletasks()
                os.remove(os.path.join(os.getcwd(), "data/temp.txt"))
                root_2.mainloop()
                temp_search.close()

            unused1, total_size, unused2 = shutil.disk_usage(drive_path)
            current_size = 0
            folders_found = 0
            files_found = 0
            files_index = 0
            folders_index = 0
            progress = 0
            search_term = self.entry_var.get()

            def stop_dur_search():
                if os.path.exists(os.path.join(os.getcwd(), "data/beep.wav")):
                    if os.path.exists(os.path.join(os.getcwd(), "data/sound_state.txt")):
                        state_file = open("data/sound_state.txt", "r")
                        state = state_file.read()
                        state_file.close()
                    else:
                        state = "ss_on"
                    if os.path.exists(os.path.join(os.getcwd(), "data/beep_aborted.txt")):
                        beep_file = open("data/beep_aborted.txt", "r")
                        beep = beep_file.read()
                        beep_file.close()
                    else:
                        beep = "1"
                    if state == "ss_on":
                        for num in range(0,int(beep)):
                            playsound("data/beep.wav")
                    else:
                        pass
                else:
                    pass
                temp_search = open("data/temp.txt", "a")
                temp_search.write("\nAborted!")
                temp_search.close()
                stop_dur_lfm()

            self.button_find.configure(text="Stop![S]", command=lambda: stop_dur_search(), state=NORMAL)

            def stop_bind(event):
                self.button_find.unbind_all("s")
                self.button_find.unbind_all("S")
                stop_dur_search()

            self.button_find.bind_all("S", stop_bind)
            self.button_find.bind_all("s", stop_bind)
            temp_search = open("data/temp.txt", "a")
            temp_search.write("\nMatches;")
            temp_search.close()
            for directory, folders, files in os.walk(drive_path):
                if loop_continue.get() == True:
                    break
                if searching_dot == "........":
                    searching_dot = "."
                searching_var.set("Searching " + drive + searching_dot)
                searching_dot += "."

                root.update()
                root.update_idletasks()
                self.canvas.update_idletasks()
                self.canvas.update()
                files_and_folders_found_var.set(
                    str(files_found) + " File(s) and " + str(folders_found) + " Folder(s) Founded")

                root.update()
                root.update_idletasks()
                self.canvas.update_idletasks()
                self.canvas.update()
                for folder in folders:
                    folders_index += 1
                    if loop_continue.get() == True:
                        break
                    if search_term.lower() in str(folder).lower():
                        temp_search = open("data/temp.txt", "a")
                        path = os.path.join(directory, folder)
                        for num in range(0, len(path)):
                            if path[-1] == " ":
                                path = path[0:-1]
                        temp_search.write("\n" + str(os.path.normpath(path)))
                        temp_search.close()
                        folders_found += 1
                        files_and_folders_found_var.set(
                            str(files_found) + " File(s) and " + str(folders_found) + " Folder(s) Founded")

                        root.update()
                        root.update_idletasks()
                        self.canvas.update_idletasks()
                        self.canvas.update()
                for file in files:
                    files_index += 1
                    if loop_continue.get() == True:
                        break
                    if progress > 99:
                        progress = 99
                    progress_var.set("Looking for Matches in Files and Folder: " + str(progress) + "%")
                    progress = int((current_size / total_size) * 100)

                    root.update()
                    root.update_idletasks()
                    self.canvas.update_idletasks()
                    self.canvas.update()
                    current_size += os.stat(os.path.join(directory, file)).st_size
                    if search_term.lower() in str(file).lower():
                        temp_search = open("data/temp.txt", "a")
                        path = os.path.join(directory, file)
                        for num in range(0, len(path)):
                            if path[-1] == " ":
                                path = path[0:-1]
                        temp_search.write("\n" + str(os.path.normpath(path)))
                        temp_search.close()
                        files_found += 1
                        files_and_folders_found_var.set(
                            str(files_found) + " File(s) and " + str(folders_found) + " Folder(s) Founded")

                        root.update()
                        root.update_idletasks()
                        self.canvas.update_idletasks()
                        self.canvas.update()
            if folders_found == 0 and files_found == 0:
                if loop_continue.get() == True:
                    temp_search = open("data/temp.txt", "a")
                    temp_search.write("\nSkipped!")
                    temp_search.close()
                else:
                    temp_search = open("data/temp.txt", "a")
                    temp_search.write("\nNo File(s) or Folder(s) to Search")
                    temp_search.close()
            else:
                temp_search = open("data/temp.txt", "a")
                temp_search.write(
                    "\nTotal Matches: " + str(files_found) + " File(s) and " + str(folders_found) + " Folder(s) ")
                temp_search.close()
                temp_search = open("data/temp.txt", "a")
                temp_search.write(
                    "\nTotal Indices: " + str(files_index) + " File(s) and " + str(folders_index) + " Folder(s) ")
                temp_search.close()
                if loop_continue.get() == True:
                    temp_search = open("data/temp.txt", "a")
                    temp_search.write("\nSkipped!")
                    temp_search.close()
            searching_var.set("Search Complete")
            progress_var.set("Search Completed; " + drive + ":" + str(100) + "%")
            root.update()
            root.update_idletasks()
            self.canvas.update_idletasks()
            self.canvas.update()
            over_all_index_folder += folders_index
            over_all_index_file += files_index
            over_all_match_file += files_found
            over_all_match_folder += folders_found
            time.sleep(1.0)

        try:
            self.canvas.delete(button_skip_win)
        except NameError or UnboundLocalError:
            pass
        progress_var.set("Total Search Completed!")
        root.update()
        root.update_idletasks()
        self.canvas.update_idletasks()
        self.canvas.update()
        temp_search = open("data/temp.txt", "a")
        temp_search.write("\n\n\nTotal Search Operation Completed!\nAnalysis;\n" "Total File(s) Indices = " + str(
            over_all_index_file) + "\n" "Total Folders(s) Indices = " + str(
            over_all_index_folder) + "\n" "Total File(s) Matches = " + str(
            over_all_match_file) + "\n" "Total Folder(s) Matches = " + str(over_all_match_folder) + "\n-----DONE------")
        temp_search.close()
        if os.path.exists(os.path.join(os.getcwd(), "data/beep.wav")):
            if os.path.exists(os.path.join(os.getcwd(), "data/sound_state.txt")):
                state_file = open("data/sound_state.txt", "r")
                state = state_file.read()
                state_file.close()
            else:
                state = "ss_on"
            if os.path.exists(os.path.join(os.getcwd(), "data/beep_complete.txt")):
                beep_file = open("data/beep_complete.txt", "r")
                beep = beep_file.read()
                beep_file.close()
            else:
                beep = "1"
            print(state)
            print(beep)
            if state == "ss_on":
                for num in range(0, int(beep)):
                    playsound("data/beep.wav")
            else:
                pass
        else:
            pass
        time.sleep(1.0)
        button_view_res = Button(self.canvas, fg=self.f_back_col, bg=self.back_col, font=self.font3, text="View Result[Enter]",
                                 command=lambda: view_result())
        button_view_res_win = self.canvas.create_window(250, 450, window=button_view_res)
        root.focus_force()

        def view_result_ret(event):
            self.button_find.unbind_all("<Return>")
            view_result()

        self.button_find.bind_all("<Return>", view_result_ret)
        root.update()
        root.update_idletasks()
        self.canvas.update_idletasks()
        self.canvas.update()

        def view_result():
            try:
                self.canvas.delete(button_skip_win)
            except NameError or UnboundLocalError:
                pass
            self.canvas.delete(button_view_res_win)
            root.update()
            root.update_idletasks()
            self.canvas.update_idletasks()
            self.canvas.update()
            stop_dur_lfm()

        def find_another():
            try:
                self.canvas.delete(button_skip_win)
            except NameError or UnboundLocalError:
                pass
            os.remove(os.path.join(os.getcwd(), "data/temp.txt"))
            self.canvas.delete(button_view_res_win)
            self.canvas.delete(searching_wind)
            self.canvas.delete(progress_win)
            self.canvas.delete(files_folder_win)
            self.button_find.configure(text="Find![Enter]", state=NORMAL, command=lambda: self.find())
            self.entry_search.configure(state=NORMAL)
            self.entry_search.focus_force()
            self.entry_search.bind("<Return>", self.find_ret)
            root.update()
            root.update_idletasks()
            self.canvas.update_idletasks()
            self.canvas.update()


        self.button_find.configure(text="Find Another[F]!", state=NORMAL, command=lambda: find_another())
        root.focus_force()

        def find_another_ret(event):
            self.button_find.unbind_all("F")
            self.button_find.unbind_all("f")
            find_another()

        self.button_find.bind_all("F", find_another_ret)
        self.button_find.bind_all("f", find_another_ret)
        root.update()
        root.update_idletasks()
        self.canvas.update_idletasks()
        self.canvas.update()

try:
    image1 = ImageTk.PhotoImage(Image.open("data/background.jpg"))
    Background(canvas1, image1)
except:
    pass
Main(canvas1, "Empty")



#9F0134
root.mainloop()
try:
    os.remove(os.path.join(os.getcwd(),"data/temp.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/temp_drive_old.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/temp_drive_new.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/sound_state.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/beep_aborted.txt"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(os.getcwd(),"data/beep_complete.txt"))
except FileNotFoundError:
    pass

