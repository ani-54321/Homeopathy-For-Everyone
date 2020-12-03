from tkinter import *
from tkinter.scrolledtext import ScrolledText

t = Tk()
t.geometry('550x500')
t.title('Homeopathy For Everyone')
t.configure(bg="#404040")

name = StringVar()
name2 = StringVar()
symp = StringVar()
dis = StringVar()

# Reading data meaningfully from text file HomeoMedData.txt with some data which I got from web scraping.
medicines = []
indications = []
f = open(r'HomeoMedData.txt','r')
line = f.readlines()
for i in line:
    start = i.find('.')
    med = i.find('-')
    ind = i.find(']')
    medicines.append(i[start+1:med])
    indications.append(i[med+1:ind])

f.close()
dictH = dict(zip(medicines, indications))
medicines_sorted = sorted(medicines)
indications2 = indications
count = 0
stop = 0

# It will provide you information about medicine you have searched for
def func1():
    def info(text):
        searches = []
        tinf.pack()
        text.config(state="normal")
        text.delete(0.0, END)
        n = name.get()
        count = 0
        indication = ""
        for j in range(len(medicines)):
            if medicines[j].lower()==n.lower():
                searches.append(j)

        indication+=medicines[searches[0]]+"\n\n"

        
        for i in searches:
            count += 1
            indication+=str(count)+') '+indications[i]+"\n\n\n"  
        text.pack()
        text.insert(0.0, indication)
        text.config(state="disabled")
        return text, searches

    def some_more(text):
        text.config(state="normal")
        text.delete(0.0, END)
        l = name.get()
        count = 0
        similar_results = []
        med_one = []
        med_one2 = []
        indication = ""
        for j in range(len(medicines)):
            if medicines[j][0].lower()==l[0].lower() and medicines[j].lower()!=l.lower():
                similar_results.append(j)

        for i in similar_results:
            n = medicines[i].replace(" ", '')
            if n not in med_one:
                med_one.append(n)
                med_one2.append(medicines[i])
            else:
                continue
                
        count = 0
        for i in med_one2:
            count+=1
            indication+=str(count)+')'+i+'\n\n'
            for j in similar_results:
                if medicines[j]==i:
                    indication+='*'+indications[j]+'*\n\n\n'
        text.pack()
        text.insert(0.0 ,indication)
        text.config(state="disabled")
        return text

    if f2.winfo_exists() and tinf2.winfo_exists():
        f2.destroy()
        tinf2.destroy()
    if f3.winfo_exists() and tinf3.winfo_exists():
        f3.destroy()
        tinf3.destroy()
    if f4.winfo_exists() and tinf4.winfo_exists():
        f4.destroy()
        tinf4.destroy()
    else:
        pass

    global f1
    f1 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)

    f1.pack()

    global tinf
    
    tinf = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
            
    Label(f1, text="I Will Find Information For Provided Medicine", bg="#00ccff", font="Times 20", padx=150, pady=1).pack()

    e = Entry(f1, width=30, bg="#0099ff", fg="#660033", borderwidth=3, font="Times 15", textvariable=name)
    e.pack(pady=10, padx=20)

    global text
    text = ScrolledText(tinf, height=20, width=100, wrap=WORD, font="Times 16", bg="#606060", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)
    Button(f1, text="Get Informaion About...", command=lambda : info(text), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5).pack()
    Button(f1, text="Some More Medicines...", command=lambda: some_more(text), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5).pack()


        

    


# It will provide you medicines on the symptom which you have searched for
def func2():
    def get_med(text2, name2):
        tinf2.pack()
        indexes2 = []
        indexes = []
        related2 = []
        related = []
        text2.config(state="normal")
        text2.delete(0.0, END)
        disease = name2.get()
        ex_names = "Exact Results : \n\n\n"
        
        for i in range(len(indications)):
            if disease.lower() in indications[i].lower():
                indexes.append(i)
            elif indications[i].find(disease[0:4])>=0:
                related.append(i)

        count = 0
        if len(indexes)>0:
            Label(t, text='')
        for i in indexes:
            if medicines[i] not in indexes2:
                indexes2.append(medicines[i])
                count += 1
                ex_names+=str(count)+')'+medicines[i]+"\n\n"

        else:
            ex_names += "\nRelated Results : \n\n\n"
            count = 0
            for i in related:
                if medicines[i] not in related2:
                    related2.append(medicines[i])
                    count += 1
                    ex_names+=str(count)+')'+medicines[i]+"\n"

        text2.pack()
        text2.insert(0.0 ,ex_names)
        text2.config(state="disabled")
        global indexes_info, related2_info, related_info, indexes2_info
        indexes_info = indexes
        indexes2_info = indexes2
        related_info = related
        related2_info = related2
        
        return indexes_info, related2_info, related_info, indexes2_info

    def get_med_info(text2, indexes_info, related2_info, related_info, indexes2_info):
        tinf2.pack()
        text2.config(state="normal")
        text2.delete(0.0, END)
        ind_info = "More Information About Each Medicine : \n\n\n"
        count = 0
        for i in indexes2_info:
            count+=1
            ind_info+=str(count)+')'+i+"\n\n"
            for j in indexes_info:
                if medicines[j]==i:
                    ind_info+='*'+indications[j]+'*\n\n\n'

        ind_info+="More Information About Each Related Results : \n\n\n"

        count = 0
        for i in related2_info:
            count+=1
            ind_info+=str(count)+')'+i+"\n"
            for j in related_info:
                if medicines[j]==i:
                    ind_info+='*'+indications[j]+'*\n\n\n'

        text2.pack()
        text2.insert(0.0 ,ind_info)
        text2.config(state="disabled")
        

    if f1.winfo_exists() and tinf.winfo_exists():
        f1.destroy()
        tinf.destroy()
    if f3.winfo_exists() and tinf3.winfo_exists():
        f3.destroy()
        tinf3.destroy()
    if f4.winfo_exists() and tinf4.winfo_exists():
        f4.destroy()
        tinf4.destroy()
    else:
        pass

    global f2
    f2 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)

    global tinf2
    
    tinf2 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
    
    f2.pack()
    Label(f2, text="I Will Find Medicine For Provided Symptom", bg="#00ccff", font="Times 20", padx=150, pady=1).pack()

    e2 = Entry(f2, width=30, bg="#0099ff", fg="#660033", borderwidth=3, font="Times 15", textvariable=name2)
    e2.pack(pady=10, padx=20)

    global text2
    text2 = ScrolledText(tinf2, height=20, width=100, wrap=WORD, font="Times 16", bg="#606060", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)

    Button(f2, text="Get Medicines", command=lambda:get_med(text2, name2), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5).pack()

    Button(f2, text="More Info on Each Medicine", command=lambda: get_med_info(text2, indexes_info, related2_info, related_info, indexes2_info), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5).pack()

    

    
# This is test section using which you can test your knowledge by yourself
def func3():
    def check(text3):
        tinf3.pack()
        text3.config(state="normal")
        text3.delete(0.0, END)
        s = symp.get()
        meds = med.get()
        global index
        index = []
        more = []
        info = ""
        for j in range(len(medicines)):
            if medicines[j].lower()==meds.lower():
                index.append(j)

        for i in range(len(indications)):
            if s.lower() in indications[i].lower():
                more.append(i)
        for i in index:
            for j in more:
                if i==j:
                    info+=medicines[i]+' :'+'\n\n '+indications[i]+'\n\n\n'
        if len(info)>1:
            info+='Yes!!! You Are Correct!!!\n\n'
        else:
            info+="Nope!!! You Are Wrong...\n\n"

        
        text3.pack()
        text3.insert(0.0, info)
        text3.config(state="disabled")
        global index_info
        index_info = more
        but = Button(f3, text="Some Other Medicines on Given Symptom", command=lambda : info_extra(text3, index_info, but), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5)
        but.pack()
        
    def info_extra(text3, index_info, but):
        text3.config(state="normal")
        text3.delete(0.0, END)
        but.destroy()
        information = 'Some Related Results on Basis of Provided Information : \n\n'
        for i in index_info:
            information+=medicines[i]+' :\n\n'+indications[i]+"\n\n\n"

        text3.pack()
        text3.insert(0.0, information)
        text3.config(state="disabled")


    if f1.winfo_exists() and tinf.winfo_exists():
        f1.destroy()
        tinf.destroy()
    if f2.winfo_exists() and tinf2.winfo_exists():
        f2.destroy()
        tinf2.destroy()
    if f4.winfo_exists() and tinf4.winfo_exists():
        f4.destroy()
        tinf4.destroy()
    else:
        pass

    global f3
    f3 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)

    global tinf3
    
    tinf3 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
    
    f3.pack()
    Label(f3, text="Enter Medicine Name : ", bg="#00ccff", font="Times 20", padx=150, pady=1).pack()

    e3 = Entry(f3, width=30, bg="#0099ff", fg="#660033", borderwidth=3, font="Times 15", textvariable=med)
    e3.pack(pady=10, padx=20)

    Label(f3, text="Enter Medicine\'s Use To Get More Information About It : ", bg="#00ccff", font="Times 20", padx=150, pady=1).pack()

    e4 = Entry(f3, width=30, bg="#0099ff", fg="#660033", borderwidth=3, font="Times 15", textvariable=symp)
    e4.pack(pady=10, padx=20)

    global text3
    text3 = ScrolledText(tinf3, height=20, width=100, wrap=WORD, font="Times 16", bg="#606060", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)

    Button(f3, text="Check Me", command=lambda : check(text3), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5).pack()


# This is the section where you just need to enter your symptoms one by one and it will provide you the medicines in each step
def func4():
    def stoper(ter, indexes, related, lab, disease, d):
        global but1
        tinf4.pack()
        text4.config(state="normal")
        text4.delete(1.0, END)
        lab.destroy()
        info = ""
        disease = disease.title()
        d+=" * "+disease
        count = 0
        e5.delete(0, END)
        if len(indexes)>0:
            info+=d+"\n\n"
            info+="Exact Results :\n"
            indexes2 = []
        for i in indexes:
            if indexes.count(i)==ter and medicines[i] not in indexes2:
                indexes2.append(medicines[i])
                count += 1
                info+="\n"+str(count)+')'+ medicines[i]+"\n"

        if len(related)>0:
            info+="\nRelated Results :\n"
            count = 0
        related2 = []
        for i in related:
            if related.count(i)==ter and medicines[i] not in related2:
                related2.append(medicines[i])
                count += 1
                info+=str(count)+')'+medicines[i]+"\n"

        text4.pack()
        text4.insert(0.0, info)
        text4.config(state="disabled")
        but1 = Button(f4, text="Go Further>>", command=lambda : for_doct(ter, but1, d), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5)
        but1.pack()
        return ter

    
    def for_doct(ter, but1, d):
        disease = dis.get()
        for i in range(len(indications)):
            if disease.lower() in indications[i].lower():
                if i in indexes or ter==0:
                    indexes.append(i)
            elif indications[i].find(disease[0:4])>=0:
                if i in related or ter==0:
                    related.append(i)
                    
        ter+=1
        but1.destroy()
        stoper(ter, indexes, related, lab, disease, d)


    if f1.winfo_exists() and tinf.winfo_exists():
        f1.destroy()
        tinf.destroy()
    if f3.winfo_exists() and tinf3.winfo_exists():
        f3.destroy()
        tinf3.destroy()
    if f2.winfo_exists() and tinf2.winfo_exists():
        f2.destroy()
        tinf2.destroy()
    else:
        pass

    global f4
    f4 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
    f4.pack()

    global indexes, indexes2, related, related2
    indexes = []
    related = []
    indexes2 = []
    related2 = []

    global tinf4
    global lab, e5
    tinf4 = Frame(t, height=50, width=90, bg="#585858", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
    lab = Label(f4, text='Write Name Of Disease Symptom or Anything Related With That Medicine & I Will Show You Medicines :', bg="#00ccff", font="Times 20", padx=150, pady=1)
    lab.pack()
    
    e5 = Entry(f4, width=30, bg="#0099ff", fg="#660033", borderwidth=3, font="Times 15", textvariable=dis)
    e5.pack()
    global text4
    text4 = ScrolledText(tinf4, height=20, width=100, wrap=WORD, font="Times 16", bg="#606060", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)
    global d
    d = ""
    
    global ter
    ter = 0
    lab = Label(f4, text='Write Name Of Disease Symptom or Anything Related With That Medicine & I Will Show You Medicines :', bg="#00ccff", font="Times 20", padx=150, pady=1)
    global but1
    but1 = Button(f4, text="Go Further>>", command=lambda : for_doct(ter, but1, d), font="Times 12", height=1, bg="#00ffff", padx=10, pady=10, borderwidth=5)
    but1.pack()

# This is menu bar
menu = Menu(t)
med = StringVar()
menu.add_command(label="Information of Medicine", command=func1)
menu.add_command(label="Get Medicines on Symptoms", command=func2)
menu.add_command(label="Test Yourself", command=func3)
menu.add_command(label="Doctor & Patient", command=func4)

#This are the frames and scrolltextboxes which are used in above functions
global f1
f1 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global f2
f2 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global f3
f3 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global f4
f4 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global text
text = ScrolledText(t, height=20, width=100, wrap=WORD, font="Times 16", bg="grey", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)
global text2
text2 = ScrolledText(t, height=20, width=100, wrap=WORD, font="Times 16", bg="grey", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)
global text3
text3 = ScrolledText(t, height=20, width=100, wrap=WORD, font="Times 16", bg="grey", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)
global text4
text4 = ScrolledText(t, height=20, width=100, wrap=WORD, font="Times 16", bg="grey", fg="white", padx=50, pady=20, relief=GROOVE, borderwidth=3)
global tinf
tinf = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global tinf2
tinf2 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global tinf3
tinf3 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)
global tinf4
tinf4 = Frame(t, height=50, width=90, bg="grey", borderwidth=3, relief=SUNKEN, padx=20, pady=20)

t.config(menu=menu)
