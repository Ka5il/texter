from tkinter import *

root = Tk()
root.title('Texter')
root.geometry('800x700')

f_text = Frame (root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text, bg='black', fg='red', padx=10, pady=10, wrap=WORD, insertbackground='red', selectbackground='red', width=80)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()