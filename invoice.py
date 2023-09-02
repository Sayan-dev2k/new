# from docxtpl import DocxTemplate
# doc=DocxTemplate("Invoice-Template.docx")
# # print(doc)
# invoice_list=[['copy',3,30,90],['ribbon',1,5,5]]
# doc.render({'Name':'sayan','Phone':'9934649548','Address':'1,gic colony,chowmatha,24 pgs(N)(WB),PIN-7000001 ',
#             'invoice_list':invoice_list,'subtotal':95,'discount':10,'tax':'5%','total':88})
# doc.save("new.docx")

# Import module
from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wedday",
    "Thruday",
    "Frday",
    "Satrday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()