import datetime
import os
from tkinter import Label, Tk
from PIL import ImageTk
import pickle as pkl
#os.getcwd()
class lms:
    """this class is used to keep record of the books in the library.
    it has total 4 modules:1 display books 2:issue books 3: return books 4: add books"""
    def __init__(self, list_of_books, library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
        self.books_dict={}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name":"","issue_date":"","status":"available"}})
            Id=Id+1
        with open('mylms.pkl','ab') as file:
            pkl.dump(self.books_dict, file)
        

    def listGui(self):
        win = Tk()
        win.title("Library")
        win.minsize(width=400,height=400)
        win.geometry("605x405")
        bg = ImageTk.PhotoImage(file='assets/libBg.jpg')
        lab = Label(win, image=bg)
        lab.pack(side='top')
        lab.place(x=0, y=0)

        win.mainloop()


    def display_books(self):
        print("__________________list of books ______________________")
        print("books ID", "\t" ,"Title")
        print("____________________________________________")#using get we can get the key's value
        for key , value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("status"),"]")


    def Issue_books(self):
        books_id=input("enter the books ID:")
        current_date=datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status']=="available":
                  print(f"this books is already issued to {self.books_dict[books_id]['lender_name']} \
                        on {self.books_dict[books_id]['issue_date']}")
                  return self.Issue_books()
            elif self.books_dict[books_id]['status']=='available':
                your_name=input("enter your name:")
                self.books_dict[books_id]['lender_name']=your_name
                self.books_dict[books_id]['issue_date']=current_date
                self.books_dict[books_id]['status']="already issued"
                print("books will be issued successfully")
        else:
            print("book not found")
    def add_books(self):
        new_books=input("enter book title")
        if new_books=="":
            return self.add_books()
        elif len(new_books)> 25:
            print("books title length is too long!!! title length should be 20 chars only")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_books,"lender name":"","issue_date":"","status":"available"}})
                print(f" this books '{new_books}' has been added successfully!!!")
                
    def delete_books(self):
        delete_book=input("enter the book ID that  you want to delete")
        if delete_book in self.books_dict.keys():
            if self.books_dict[delete_book]["status"]=="available":
                self.books_dict.pop('delete_book')
                print("the book ID ",delete_book,"is succesfully deleted")
        else:
            print("book ID not found")
            
    def return_books(self):
        books_id=input("enter the book ID")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"]=="available":
                print("this book is already available in library.please check your book ID")
                return self.return_books()
            elif not self.books_dict[books_id]["status"]=="available":
                self.books_dict[books_id]["lender_name"]=""
                self.books_dict[books_id]["issue date"]=""
                self.books_dict[books_id]["status"]="already issued"
                print("succesfully updated!!! \n")
        else:
            print("book ID is not found")
try:
    mylms=lms(r"trail codes\list_of_books.txt","python library")
    press_key_list={"d":"display books","i":"issue books","a":"add books","db":"delete books","r":"return books","q":"quit"}
    key_press=False
    while not(key_press=="q"):
        print(f"\n------------------welcome to {mylms.library_name} library management syystem ---------\n")
        for key,value in press_key_list.items():
            print("press",key,"to",value)
        key_press=input("press key: ").lower()
        if key_press=="i":
                print("\n current selection : Issue books \n")
                mylms.Issue_books()
        elif key_press=="a":
                print("\n current selection : add books \n")
                mylms.add_books()
        elif key_press=="d":
                print("\n current slection: display books \n")
                mylms.display_books()
        elif key_press=="db":
                print("\n current location: delete books \n")
                mylms.delete_books()
        elif key_press=="r":
                print("\n current selection: return books\n")
                mylms.return_books()
        elif key_press=="a":
                break
        else:
                continue
except Exception as e:
    print("something went wrong please check your input:")
