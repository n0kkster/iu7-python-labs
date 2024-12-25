from tkinter import * 
from tkinter import ttk


def convert():
	conn = conn_type.get()
	r0 = 0
	r1 = int(r1_entry.get())
	r2 = int(r2_entry.get())

	if conn == 'cons':
		r0 = r1 + r2
	else:
		r0 = (r1 * r2) / (r1 + r2)
	r0_label['text'] = str(round(r0, 2))


root = Tk()
root.geometry('200x250')
root.title('Resistance')
root.resizable(False, False)

ttk.Label(root, text='R1', font=('Helvetica', 24), 
	anchor='center', borderwidth=1, width=3, relief='solid').place(x=10, y=10)

ttk.Label(root, text='R2', font=('Helvetica', 24), 
	anchor='center', borderwidth=1, width=3, relief='solid').place(x=10, y=70)

r1_entry = ttk.Entry(justify='center', width=6, font=('Helvetica', 22))
r1_entry.place(x=80, y=10)

r2_entry = ttk.Entry(justify='center', width=6, font=('Helvetica', 22))
r2_entry.place(x=80, y=70)

conn_type = StringVar(value='cons') 
ttk.Radiobutton(text='Последовательно', value='cons', variable=conn_type).place(x=10, y=130)
ttk.Radiobutton(text='Параллельно', value='parallel', variable=conn_type).place(x=10, y=150)


r0_label = ttk.Label(root, text='R0', font=('Helvetica', 24), 
	anchor='center', borderwidth=1, width=7, relief='solid')
r0_label.place(x=10, y=180)

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 20))

ttk.Button(root, text='=', width=2, style='my.TButton', command=convert).place(x=150, y=179)

root.mainloop()
