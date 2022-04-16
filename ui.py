from msilib.schema import tables
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, ITALIC


class App:
    def __init__ (self,root):
        self.root= root
        self.root.geometry ('1200x690+1+5')
        self.root.title('Prodduct Managment System',)
        self.root.configure(background="#F8F8FF")
        self.root.resizable(False,False)
        
        header = Label(self.root,text='Add Category', pady=5, bg='#0762eb', font=('arial',16, ITALIC), fg='White')
        header.pack(fill='x')

        # Search Frame
        Search_frame = Frame(self.root,bg='black', padx=15)
        Search_frame.place(x=600,y=39,width=1100,height=50)

        Search_btn=Button(Search_frame,text ='Search', bg='#0762eb', fg='#f8f8f8', font=('ariat',10, ITALIC))
        Search_btn.place(x=330, y=15, width=100, height=25)

        Entry_Search=Entry(Search_frame,bd='0', bg='#f1f1f1' ,justify="left", width=20)
        Entry_Search.place(x=200, y=15, height=25)

        Combo_Search=ttk.Combobox(Search_frame)
        Combo_Search['values']=('product','category','desc','category name')
        Combo_Search.place(x=50,y=15, height=25)


        #table

#         tables_frame= Frame(self.root,bg='green', padx=15)
#         tables_frame.place(x=400,y=120,width=1000,height=250)

#     class Table:
	
# 	    def __init__(self,root):
		
# 		# code for creating table
# 		    for i in range(total_rows):
# 			    for j in range(total_columns):
				
# 				    self.e = Entry(root, width=20, fg='blue',
# 							font=('Arial',16,'bold'))
				
# 				    self.e.grid(row=i, column=j)
# 				    self.e.insert(END, lst[i][j])

# # take the data
# lst = [(1,'Raj','Mumbai',19),
# 	(2,'Aaryan','Pune',18),
# 	(3,'Vaishnavi','Mumbai',20),
# 	(4,'Rachna','Mumbai',21),
# 	(5,'Shubham','Delhi',21)]

# # find total number of rows and
# # columns in list
# total_rows = len(lst)
# total_columns = len(lst[0])

        # Entry Frame
        mange_frame = Frame(self.root,bg='white', pady=40)
        mange_frame.place(x=0, y=40, width=250, height=350)

        entries_list = ['Category ID', 'Category Name', 'Ctaegory Description']
        for ent in entries_list:
            label = Label(mange_frame, text = ent, bg='white', font=('ariat',10, BOLD)).pack()
            entry = Entry(mange_frame, justify="center", bd='0', bg='#f1f1f1', width=35).pack(pady=10)

        #dashboard Frame
        Button_framr = Frame(self.root,bg='white', )
        Button_framr.place(x=0,y=365,width=250,height=325)
        
        title1=Label(Button_framr,text='DashBoard', pady=10, font=('arial',14, ITALIC), fg='white', bg='#0762eb')
        title1.pack(fill='x')


        add_btn=Button(Button_framr,text='Add Category ', bd=0, bg='#0762eb', fg='#f8f8f8', font=('ariat',12, ITALIC))
        add_btn.place(x=45, y=70, width=170, height=30)

        delete_btn=Button(Button_framr,text='Delete Category', bd=0, bg='#0762eb', fg='#f8f8f8', font=('ariat',12, ITALIC))
        delete_btn.place(x=45, y=120, width=170, height=30)

        update_btn=Button(Button_framr,text='Update Category', bd=0, bg='#0762eb', fg='#f8f8f8', font=('ariat',12, ITALIC))
        update_btn.place(x=45, y=170, width=170, height=30)

        exit_btn=Button(Button_framr,text='Exit', bd=0, bg='red', fg='#f8f8f8', font=('ariat',12, ITALIC), command=exit)
        exit_btn.place(x=45, y=230, width=170, height=30)     

    
#scroll

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
    t = tables(root)


