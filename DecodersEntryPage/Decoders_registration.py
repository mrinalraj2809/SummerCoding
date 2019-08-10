from tkinter import *
import datetime
import time
root = Tk()
root.geometry("1600x8000")
root.title("DECODERS Registration System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
#=================================================================================
#                  TIME
#=================================================================================
localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('arial',50,'bold'),text="DECODERS ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#=================================================================================
#                  No. of Team Member
#=================================================================================
v = IntVar()
lblInfo=Label(Tops,font=('arial',14,'bold'),text="Choose no. of Team Member in a group:",fg="Black",justify = LEFT,
        padx = 20,bd=10,anchor='w')
lblInfo.grid(row=2,column=0)
#Label(root, 
 #       text="""Choose no. of Team Member in a group:""",
   #     justify = LEFT,
    #    padx = 20).pack()

Radiobutton(root, 
              text="2 Members",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor='w')
Radiobutton(root, 
              text="3 Members",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor = 'w')

def StudentDetails():
    name = StringVar()
    usn = StringVar()
    college = StringVar()
    mail = StringVar()
    phone = StringVar()
    lblName= Label(f1, font=('arial', 16, 'bold'),text="Name ",bd=16,anchor="w")
    lblName.grid(row=0, column=0)
    txtName=Entry(f1, font=('arial',16,'bold'),textvariable=name,bd=10,insertwidth=4,bg="powder blue",justify='right')
    txtName.grid(row=0,column=1)

    
    lblUsn= Label(f1, font=('arial', 16, 'bold'),text="Usn ",bd=16,anchor="w")
    lblUsn.grid(row=1, column=0)
    txtUsn=Entry(f1, font=('arial',16,'bold'),textvariable=usn,bd=10,insertwidth=4,bg="powder blue",justify='right')
    txtUsn.grid(row=1,column=1)

    lblCollege= Label(f1, font=('arial', 16, 'bold'),text="College ",bd=16,anchor="w")
    lblCollege.grid(row=2, column=0)
    txtCollege=Entry(f1, font=('arial',16,'bold'),textvariable=college,bd=10,insertwidth=4,bg="powder blue",justify='right')
    txtCollege.grid(row=2,column=1)


    lblMail= Label(f1, font=('arial', 16, 'bold'),text="Mail address",bd=16,anchor="w")
    lblMail.grid(row=3, column=0)
    txtMail=Entry(f1, font=('arial',16,'bold'),textvariable=mail,bd=10,insertwidth=4,bg="powder blue",justify='right')
    txtMail.grid(row=3,column=1)
    
    lblPhone= Label(f1, font=('arial', 16, 'bold'),text="Phone no.",bd=16,anchor="w")
    lblPhone.grid(row=4, column=0)
    txtPhone=Entry(f1, font=('arial',16,'bold'),textvariable=phone,bd=10,insertwidth=4,bg="powder blue",justify='right')
    txtPhone.grid(row=4,column=1)
#=================================================================================
#                  Saving the input
#=================================================================================
    if (name.get()==""):
        varName=0
    else:
        varName=name.get()
    
    if (usn.get()==""):
        varUsn=0
    else:
        varUsn=usn.get()
    if (college.get()==""):
        varCollege=0
    else:
        varCollege= college.get()

    if (mail.get()==""):
        varMail=0
    else:
        varMail=mail.get()

    if (phone.get()==""):
        varPhone=0
    else:
        varPhone = phone.get()

    
    
    

StudentDetails()



root.mainloop()
