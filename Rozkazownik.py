# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 19:48:45 2022

@author: Maslo200g
"""

import tkinter as tk
import Locale as lc
import datetime
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

class Rozkazownik(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        master.geometry('500x900')
        master.resizable(False, False)
        master.title('Rozkazownik')
        master.lang = tk.StringVar()
        tk.Frame.__init__(self, master)
        topframe = tk.Frame(self)
        tt = ttk.Label(topframe, text="Rozkazownik",
                       font=('Helvetica', 18, "bold"))
        tt.grid(row=0, column=0)
        langlist = ttk.Combobox(topframe, width=3,
                     textvariable=master.lang,
                     values=lc.langlist,
                     state='readonly')
        langlist.grid(row=0, column=1, padx=15)
        topframe.pack(side="top", fill="x", pady=5, padx=120)
        Sllabel = tk.Frame(self)
        ttk.Label(Sllabel, width=25, text='Stacja / Staions',anchor="c").grid(row=0, column=0)
        ttk.Label(Sllabel, width=20, text='Posterunki / Posts',anchor="c").grid(row=0, column=1)
        Sllabel.pack()
        Stationlist = tk.Frame(self)
        master.sta = [tk.StringVar(),
                      tk.StringVar(),
                      tk.StringVar(),
                      tk.StringVar()]
        master.pos = [[tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar()],
                      [tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar()],
                      [tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar()],
                      [tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar(),
                       tk.StringVar()]]
        ttk.Entry(Stationlist, textvariable=master.sta[0],
                  width=25).grid(row=0, column=0)
        ttk.Entry(Stationlist, textvariable=master.pos[0][0],
                  width=5).grid(row=0, column=1)
        ttk.Entry(Stationlist, textvariable=master.pos[0][1],
                  width=5).grid(row=0, column=2)
        ttk.Entry(Stationlist, textvariable=master.pos[0][2],
                  width=5).grid(row=0, column=3)
        ttk.Entry(Stationlist, textvariable=master.pos[0][3],
                  width=5).grid(row=0, column=4)
        ttk.Entry(Stationlist, textvariable=master.sta[1],
                  width=25).grid(row=1, column=0)
        ttk.Entry(Stationlist, textvariable=master.pos[1][0],
                  width=5).grid(row=1, column=1)
        ttk.Entry(Stationlist, textvariable=master.pos[1][1],
                  width=5).grid(row=1, column=2)
        ttk.Entry(Stationlist, textvariable=master.pos[1][2],
                  width=5).grid(row=1, column=3)
        ttk.Entry(Stationlist, textvariable=master.pos[1][3],
                  width=5).grid(row=1, column=4)
        ttk.Entry(Stationlist, textvariable=master.sta[2],
                  width=25).grid(row=2, column=0)
        ttk.Entry(Stationlist, textvariable=master.pos[2][0],
                  width=5).grid(row=2, column=1)
        ttk.Entry(Stationlist, textvariable=master.pos[2][1],
                  width=5).grid(row=2, column=2)
        ttk.Entry(Stationlist, textvariable=master.pos[2][2],
                  width=5).grid(row=2, column=3)
        ttk.Entry(Stationlist, textvariable=master.pos[2][3],
                  width=5).grid(row=2, column=4)
        ttk.Entry(Stationlist, textvariable=master.sta[3],
                  width=25).grid(row=3, column=0)
        ttk.Entry(Stationlist, textvariable=master.pos[3][0],
                  width=5).grid(row=3, column=1)
        ttk.Entry(Stationlist, textvariable=master.pos[3][1],
                  width=5).grid(row=3, column=2)
        ttk.Entry(Stationlist, textvariable=master.pos[3][2],
                  width=5).grid(row=3, column=3)
        ttk.Entry(Stationlist, textvariable=master.pos[3][3],
                  width=5).grid(row=3, column=4)
        Stationlist.pack()
        ttk.Label(self, width=60, anchor='c',
                  text='Rozkaz wystawiony przez: / Written order given by:').pack()
        master.drpolec = tk.StringVar()
        droood_cb = ttk.Combobox(self, width=33, textvariable=master.drpolec)
        droood_cb['values'] = ['Dyżurny Ruchu / Dispatcher',
                               'z polecenia DR / On order of dispatcher']
        droood_cb['state'] = 'readonly'
        droood_cb.pack()
        ttk.Label(self, width=33,
                  text='Nazwisko / Surname',
                  anchor="c").pack()
        master.username = tk.StringVar()
        ttk.Entry(self, textvariable=master.username, width=33).pack()
        tk.Button(self, text="Start",
                  command=lambda: master.switch_frame(Main)).pack(pady=10)


class Main(tk.Frame):
    def __init__(self, master):
        lang = master.lang.get()
        if lang == '':
            lang = 'EN'
        stations = []
        posts = []
        for i in master.sta:
            if i.get() != '':
                stations.append(i.get())
        for j in master.pos:
            for k in j:
                if k.get() != '':
                    posts.append(k.get())
        tk.Frame.__init__(self, master)
        tabs = ttk.Notebook(master)
        tabs.pack(fill='both', expand=True)
        Sroot = tk.Frame(tabs)
        Nroot = tk.Frame(tabs)
        Oroot = tk.Frame(tabs)
        tabs.add(Sroot, text='\tS\t ')
        tabs.add(Nroot, text='\tN\t ')
        tabs.add(Oroot, text='\tO\t ')

        # S ===================================================================
        # Header --------------------------------------------------------------
        # First line
        l1 = tk.Frame(Sroot)

        # label
        rp = ttk.Label(l1, text=lc.text[lang]['rp'] +
                       ': "S" ' + lc.text[lang]['nr'])
        rp.pack(side='left', padx=5, pady=5)

        # number entrybox
        srpno = tk.StringVar()
        Order_no = tk.Entry(l1, width=5, textvariable=srpno)
        Order_no.pack(side='left', padx=5, pady=5)
        l1.pack()

        # Second line
        l2 = tk.Frame(Sroot)

        # number label
        trno = ttk.Label(l2, text=lc.text[lang]['dla'])
        trno.pack(side='left', padx=5, pady=5)

        # train type
        spmtype = tk.StringVar()
        spmtype_cb = ttk.Combobox(l2, width=9, textvariable=spmtype)
        spmtype_cb['values'] = lc.text[lang]['pocman']
        spmtype_cb['state'] = 'readonly'
        spmtype_cb.pack(side='left', padx=5, pady=5)

        # number entrybox
        strno = tk.StringVar()
        Train_no = tk.Entry(l2, width=7, textvariable=strno)
        Train_no.pack(side='left', padx=5, pady=5)

        l2.pack()

        # Separator before sections
        topsep = ttk.Separator(Sroot, orient='horizontal')
        topsep.pack(fill='x')

        # Sections ------------------------------------------------------------
        # Section 1-1
        sd1 = tk.Frame(Sroot)
        sd1.pack()

        sd1no = ttk.Label(sd1, text=' 1.', font='bold', anchor="nw")
        sd1no.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

        sd11 = tk.Frame(sd1)
        sd11.grid(row=0, column=1)

        sd11n = tk.BooleanVar()
        sd11n.set(False)
        sd11need = tk.Checkbutton(sd11, variable=sd11n)
        sd11need.grid(row=0, column=0)

        sd11l1 = tk.Frame(sd11)
        sd11l1.grid(row=0, column=1, sticky="w")

        sd11l1txt = ttk.Label(sd11l1, text=lc.text[lang]['zezpootrz'],
                              anchor="w")
        sd11l1txt.pack(side='left', pady=5)

        sd11_command = tk.StringVar()
        sd11l1_cb = ttk.Combobox(sd11l1, width=lc.text[lang]['otrzymsz'],
                                 textvariable=sd11_command)
        sd11l1_cb['values'] = lc.text[lang]['otrzym']
        sd11l1_cb['state'] = 'readonly'
        sd11l1_cb.pack(side='left', padx=5, pady=5)

        sd11l1to = ttk.Label(sd11l1, text=lc.text[lang]['to'], anchor="w")
        sd11l1to.pack(side='left', pady=5)

        sd11l2 = ttk.Label(sd11, text=lc.text[lang]['przS1'], anchor="w")
        sd11l2.grid(row=2, column=1, sticky="W")

        sd11l3 = tk.Frame(sd11)
        sd11l3.grid(row=3, column=1, sticky="w")

        sd11_stype = tk.StringVar()
        sd11st_cb = ttk.Combobox(sd11l3, width=16, textvariable=sd11_stype)
        sd11st_cb['values'] = lc.text[lang]['semwyjazd']
        sd11st_cb['state'] = 'readonly'
        sd11st_cb.pack(side='left', pady=5)

        sd11sem = tk.StringVar()
        sd11semget = tk.Entry(sd11l3, textvariable=sd11sem, width=5)
        sd11semget.pack(side='left', padx=5, pady=5)

        # Section 1-2
        sd12 = tk.Frame(sd1)
        sd12.grid(row=1, column=1, sticky="w")

        sd12n = tk.BooleanVar()
        sd12n.set(False)
        sd12need = tk.Checkbutton(sd12, var=sd12n)
        sd12need.grid(row=0, column=0)

        sd12l1 = tk.Frame(sd12)
        sd12l1.grid(row=0, column=1, sticky="w")

        sd12txt = ttk.Label(sd12l1, text=lc.text[lang]['wyjeztor'], anchor="w")
        sd12txt.pack(side='left', pady=5)

        sd12tor = tk.StringVar()
        sd12torask = tk.Entry(sd12l1, textvariable=sd12tor, width=5)
        sd12torask.pack(side='left', padx=5, pady=5)

        sd12txt = ttk.Label(sd12l1, text=lc.text[lang]['nposiad'], anchor="w")
        sd12txt.pack(side='left', pady=5)

        sd12l2 = ttk.Label(sd12, text=lc.text[lang]['wyjazdowego'], anchor="w")
        sd12l2.grid(row=1, column=1, sticky="w")

        sep12 = ttk.Separator(Sroot, orient='horizontal')
        sep12.pack(fill='x')

        # Section 2-1
        sd2 = tk.Frame(Sroot)
        sd2.pack()

        sd2no = ttk.Label(sd2, text=' 2.', font='bold', anchor="nw")
        sd2no.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

        sd21 = tk.Frame(sd2)
        sd21.grid(row=0, column=1)

        sd21n = tk.BooleanVar()
        sd21n.set(False)
        sd21need = tk.Checkbutton(sd21, var=sd21n)
        sd21need.grid(row=0, column=0)

        sd21l1 = tk.Frame(sd21)
        sd21l1.grid(row=0, column=1, sticky="w")

        sd21l1txt = ttk.Label(sd21l1, text=lc.text[lang]['zezpootrz'],
                              anchor="w")
        sd21l1txt.pack(side='left', pady=5)

        sd21_command = tk.StringVar()
        sd21l1_cb = ttk.Combobox(sd21l1, width=lc.text[lang]['otrzymsz'],
                                 textvariable=sd21_command)
        sd21l1_cb['values'] = lc.text[lang]['otrzym']
        sd21l1_cb['state'] = 'readonly'
        sd21l1_cb.pack(side='left', padx=5, pady=5)

        sd21l1to = ttk.Label(sd21l1, text=lc.text[lang]['to'], anchor="w")
        sd21l1to.pack(side='left', pady=5)

        sd21l2 = ttk.Label(sd21, text=lc.text[lang]['przS1'], anchor="w")
        sd21l2.grid(row=2, column=1, sticky="W")

        sd21l3 = tk.Frame(sd21)
        sd21l3.grid(row=3, column=1, sticky="w")

        sd21_stype = tk.StringVar()
        sd21st_cb = ttk.Combobox(sd21l3, width=16, textvariable=sd21_stype)
        sd21st_cb['values'] = lc.text[lang]['semwjazd']
        sd21st_cb['state'] = 'readonly'
        sd21st_cb.pack(side='left', pady=5)

        sd21sem = tk.StringVar()
        sd21semget = tk.Entry(sd21l3, textvariable=sd21sem, width=5)
        sd21semget.pack(side='left', padx=5, pady=5)

        # Section 2-2
        sd22 = tk.Frame(sd2)
        sd22.grid(row=1, column=1, sticky="w")

        sd22n = tk.BooleanVar()
        sd22n.set(False)
        sd22need = tk.Checkbutton(sd22, var=sd22n)
        sd22need.grid(row=0, column=0)

        sd22l1 = tk.Frame(sd22)
        sd22l1.grid(row=0, column=1, sticky="w")

        sd22txt = ttk.Label(sd22l1, text=lc.text[lang]['wyjeztor'], anchor="w")
        sd22txt.pack(side='left', pady=5)

        sd22tor = tk.Entry(sd22l1, width=5)
        sd22tor.pack(side='left', padx=5, pady=5)

        sd22txt = ttk.Label(sd22l1, text=lc.text[lang]['nposiad'], anchor="w")
        sd22txt.pack(side='left', pady=5)

        sd22l2 = ttk.Label(sd22, text=lc.text[lang]['wjazdowego'], anchor="w")
        sd22l2.grid(row=1, column=1, sticky="w")

        sep23 = ttk.Separator(Sroot, orient='horizontal')
        sep23.pack(fill='x')

        # Section 3
        sd3 = tk.Frame(Sroot)
        sd3.pack()

        sd3no = ttk.Label(sd3, text=' 3.', font='bold', anchor="nw")
        sd3no.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

        sd31 = tk.Frame(sd3)
        sd31.grid(row=0, column=1)

        sd31n = tk.BooleanVar()
        sd31n.set(False)
        sd31need = tk.Checkbutton(sd31, var=sd31n)
        sd31need.grid(row=0, column=0)

        sd31l1 = tk.Frame(sd31)
        sd31l1.grid(row=0, column=1, sticky="nw")

        sd31odkm = ttk.Label(sd31l1, text=lc.text[lang]['Od']+' km', anchor="w")
        sd31odkm.pack(side='left')

        sd31od = tk.StringVar()
        sd31odadd = tk.Entry(sd31l1, textvariable=sd31od, width=5)
        sd31odadd.pack(side='left', padx=5, pady=5)

        sd31dokm = ttk.Label(sd31l1, text=lc.text[lang]['do']+' km', anchor="w")
        sd31dokm.pack(side='left')

        sd31do = tk.StringVar()
        sd31doadd = tk.Entry(sd31l1, textvariable=sd31do, width=5)
        sd31doadd.pack(side='left', padx=5, pady=5)

        sd31potor = ttk.Label(sd31l1, text=lc.text[lang]['potor'] +
                              lc.text[lang]['nr'], anchor="w")
        sd31potor.pack(side='left')

        sd31tor = tk.StringVar()
        sd31toradd = tk.Entry(sd31l1, textvariable=sd31tor, width=5)
        sd31toradd.pack(side='left', padx=5, pady=5)

        sd313ponr = ttk.Label(sd31l1, text=lc.text[lang]['3ponr'], anchor="w")
        sd313ponr.pack(side='left')

        sd31l2 = ttk.Label(sd31, text=lc.text[lang]['3mid'], anchor="w")
        sd31l2.grid(row=1, column=1, sticky="nw")

        sd31l3 = tk.Frame(sd31)
        sd31l3.grid(row=2, column=1, sticky="nw")

        sd31l3last = ttk.Label(sd31l3, text=lc.text[lang]['3mlast'],
                               anchor="w")
        sd31l3last.pack(side='left')

        sd31poc = tk.StringVar()
        sd31pocadd = tk.Entry(sd31l3, textvariable=sd31poc, width=7)
        sd31pocadd.pack(side='left', padx=5, pady=5)

        sd31lprzyb = ttk.Label(sd31l3, text=lc.text[lang]['przybyl'],
                               anchor="w")
        sd31lprzyb.pack(side='left')

        sd31l4 = tk.Frame(sd31)
        sd31l4.grid(row=3, column=1, sticky="nw")

        sd31l4txt = ttk.Label(sd31l4, text=lc.text[lang]['do'], anchor="w")
        sd31l4txt.pack(side='left')

        sd31pdo = tk.StringVar()
        sd31pdoadd = tk.Entry(sd31l4, textvariable=sd31pdo, width=25)
        sd31pdoadd.pack(side='left', padx=5, pady=5)

        sd31l4ogodz = ttk.Label(sd31l4, text=lc.text[lang]['ogodz'],
                                anchor="w")
        sd31l4ogodz.pack(side='left')

        sd31godz = tk.StringVar()
        sd31godzadd = tk.Entry(sd31l4, textvariable=sd31godz, width=6)
        sd31godzadd.pack(side='left', padx=5, pady=5)

        sep23 = ttk.Separator(Sroot, orient='horizontal')
        sep23.pack(fill='x')

        # Section 4
        sd4 = tk.Frame(Sroot)
        sd4.pack()

        sd4no = ttk.Label(sd4, text=' 4.', font='bold', anchor="nw")
        sd4no.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

        sd41 = tk.Frame(sd4)
        sd41.grid(row=0, column=1)

        sd41n = tk.BooleanVar()
        sd41n.set(False)
        sd41need = tk.Checkbutton(sd41, var=sd41n)
        sd41need.grid(row=0, column=0)

        sd41l1 = ttk.Label(sd41, text=lc.text[lang]['inne'], anchor="w")
        sd41l1.grid(row=0, column=1, sticky="nw")

        sd41txt = tk.Text(sd41, font=("Helvetica", 9), width=52, height=8)
        sd41txt.grid(row=1, column=1, sticky="nw", pady=5)

        # N ===================================================================
        # First line
        l1 = tk.Frame(Nroot)

        # label
        rp = ttk.Label(l1, text=lc.text[lang]['rp']+': "N" ' + lc.text[lang]['nr'])
        rp.pack(side='left', padx=5, pady=5)

        # number entrybox
        nrpno = tk.StringVar()
        Order_no = tk.Entry(l1, textvariable=nrpno, width=5)
        Order_no.pack(side='left', padx=5, pady=5)
        l1.pack()

        # Second line
        l2 = tk.Frame(Nroot)

        # number label
        trno = ttk.Label(l2, text=lc.text[lang]['dla'])
        trno.pack(side='left', padx=5, pady=5)

        # train type
        npmtype = tk.StringVar()
        npmtype_cb = ttk.Combobox(l2, width=9, textvariable=npmtype)
        npmtype_cb['values'] = lc.text[lang]['pocman']
        npmtype_cb['state'] = 'readonly'
        npmtype_cb.pack(side='left', padx=5, pady=5)

        # number entrybox
        ntrno = tk.StringVar()
        Train_no = tk.Entry(l2, textvariable=ntrno, width=7)
        Train_no.pack(side='left', padx=5, pady=5)

        l2.pack()

        topsep = ttk.Separator(Nroot, orient='horizontal')
        topsep.pack(fill='x')

        # Sections ------------------------------------------------------------
        # Section 1
        nd1 = tk.Frame(Nroot)
        nd1.pack()

        nd1no = ttk.Label(nd1, text=' 1.', font='bold', anchor="nw")
        nd1no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        nd11 = tk.Frame(nd1)
        nd11.grid(row=0, column=1)

        nd11n = tk.BooleanVar()
        nd11n.set(False)
        nd11need = tk.Checkbutton(nd11, var=nd11n)
        nd11need.grid(row=0, column=0)

        nd11l1 = tk.Frame(nd11)
        nd11l1.grid(row=0, column=1, sticky="w")

        nd11l1od = ttk.Label(nd11l1, text=lc.text[lang]['Od'],
                             anchor="w")
        nd11l1od.pack(side='left')

        nd11od = tk.StringVar()
        nd11odsta = tk.Entry(nd11l1, textvariable=nd11od, width=21)
        nd11odsta.pack(side='left', padx=5, pady=1)

        nd11l1do = ttk.Label(nd11l1, text=lc.text[lang]['do'],
                             anchor="w")
        nd11l1do.pack(side='left')

        nd11do = tk.StringVar()
        nd11dosta = tk.Entry(nd11l1, textvariable=nd11do, width=21)
        nd11dosta.pack(side='left', padx=5, pady=1)

        nd11l2 = tk.Frame(nd11)
        nd11l2.grid(row=1, column=1, sticky="w")

        nd11l2nr = ttk.Label(nd11l2, text=lc.text[lang]['tor'] +
                             ' ' + lc.text[lang]['nr'],
                             anchor="w")
        nd11l2nr.pack(side='left')

        nd11tor1 = tk.StringVar()
        nd11tor1add = tk.Entry(nd11l2, textvariable=nd11tor1, width=4)
        nd11tor1add.pack(side='left', padx=5, pady=1)

        nd11l2txt = ttk.Label(nd11l2, text=lc.text[lang]['n1txt'],
                             anchor="w")
        nd11l2txt.pack(side='left')

        nd11l3 = tk.Frame(nd11)
        nd11l3.grid(row=2, column=1, sticky="w")

        nd11l3txt = ttk.Label(nd11l3, text=lc.text[lang]['n1txt2'] +
                              ' ' + lc.text[lang]['nr'], anchor="w")
        nd11l3txt.pack(side='left')

        nd11tor2 = tk.StringVar()
        nd11tor2add = tk.Entry(nd11l3, textvariable=nd11tor2, width=4)
        nd11tor2add.pack(side='left', padx=5, pady=1)

        sep12 = ttk.Separator(Nroot, orient='horizontal')
        sep12.pack(fill='x')

        # Section 2-1
        nd2 = tk.Frame(Nroot)
        nd2.pack()

        nd2no = ttk.Label(nd2, text=' 2.', font='bold', anchor="nw")
        nd2no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        nd21 = tk.Frame(nd2)
        nd21.grid(row=0, column=1)

        nd21n = tk.BooleanVar()
        nd21n.set(False)
        nd21need = tk.Checkbutton(nd21, var=nd21n)
        nd21need.grid(row=0, column=0)

        nd21l1 = tk.Frame(nd21)
        nd21l1.grid(row=0, column=1, sticky="w")

        nd21l1txt = ttk.Label(nd21l1, text=lc.text[lang]['zezpootrz'],
                              anchor="w")
        nd21l1txt.pack(side='left', pady=1)

        nd21_command = tk.StringVar()
        nd21l1_cb = ttk.Combobox(nd21l1, width=lc.text[lang]['otrzymsz'],
                                 textvariable=nd21_command)
        nd21l1_cb['values'] = lc.text[lang]['otrzym']
        nd21l1_cb['state'] = 'readonly'
        nd21l1_cb.pack(side='left', padx=5, pady=1)

        nd21l1to = ttk.Label(nd21l1, text=lc.text[lang]['to'], anchor="w")
        nd21l1to.pack(side='left', pady=1)

        nd21l2 = ttk.Label(nd21, text=lc.text[lang]['przS1'], anchor="w")
        nd21l2.grid(row=2, column=1, sticky="W")

        nd21l3 = tk.Frame(nd21)
        nd21l3.grid(row=3, column=1, sticky="w")

        nd21_stype = tk.StringVar() #need fix here
        nd21st_cb = ttk.Combobox(nd21l3, width=16, textvariable=nd21_stype)
        nd21st_cb['values'] = lc.text[lang]['semy']
        nd21st_cb['state'] = 'readonly'
        nd21st_cb.pack(side='left', pady=1)

        nd21sem = tk.Entry(nd21l3, width=5)
        nd21sem.pack(side='left', padx=5, pady=1)

        nd21l3iwy = ttk.Label(nd21l3, text=lc.text[lang]['iwy'], anchor="w")
        nd21l3iwy.pack(side='left')

        nd21l4 = tk.Frame(nd21)
        nd21l4.grid(row=4, column=1, sticky="w")

        nd21kier = tk.StringVar()
        nd21kieradd = tk.Entry(nd21l4, textvariable=nd21kier, width=20)
        nd21kieradd.pack(side='left', pady=1)

        nd21l4txt = ttk.Label(nd21l4, text=lc.text[lang]['nator'], anchor="w")
        nd21l4txt.pack(side='left', padx=5)

        nd21pl = tk.StringVar()
        nd21pl_cb = ttk.Combobox(nd21l4, width=5, textvariable=nd21pl)
        nd21pl_cb['values'] = lc.text[lang]['prawylewy']
        nd21pl_cb['state'] = 'readonly'
        nd21pl_cb.pack(side='left', pady=2)

        nd21l4tornr = ttk.Label(nd21l4, text=lc.text[lang]['tornr'], anchor="w")
        nd21l4tornr.pack(side='left', padx=5,)

        nd21tor = tk.StringVar()
        nd21toradd = tk.Entry(nd21l4, textvariable=nd21tor, width=5)
        nd21toradd.pack(side='left', padx=5, pady=1)

        # Section 2-2
        nd22 = tk.Frame(nd2)
        nd22.grid(row=1, column=1, sticky="w")

        nd22n = tk.BooleanVar()
        nd22n.set(False)
        nd22need = tk.Checkbutton(nd22, var=nd22n)
        nd22need.grid(row=0, column=0)

        nd22l1 = tk.Frame(nd22)
        nd22l1.grid(row=0, column=1, sticky="w")

        nd22txt = ttk.Label(nd22l1, text=lc.text[lang]['wyjeztor'], anchor="w")
        nd22txt.pack(side='left', pady=1)

        nd22tor = tk.StringVar()
        nd22toradd = tk.Entry(nd22l1, textvariable=nd22tor, width=5)
        nd22toradd.pack(side='left', padx=5, pady=1)

        nd22txt = ttk.Label(nd22l1, text=lc.text[lang]['nposiad'], anchor="w")
        nd22txt.pack(side='left', pady=1)

        nd22l2 = tk.Frame(nd22)
        nd22l2.grid(row=1, column=1, sticky="w")

        nd22txt = ttk.Label(nd22l2, text=lc.text[lang]['wjazdowego'] +
                           lc.text[lang]['wkier'], anchor="w")
        nd22txt.pack(side='left', pady=1)

        nd22kier = tk.StringVar()
        nd22kieradd = tk.Entry(nd22l2, textvariable=nd22kier, width=20)
        nd22kieradd.pack(side='left', padx=5, pady=1)

        nd22l3 = tk.Frame(nd22)
        nd22l3.grid(row=4, column=1, sticky="w")

        nd22l3txt = ttk.Label(nd22l3, text=lc.text[lang]['nator'], anchor="w")
        nd22l3txt.pack(side='left', padx=5)

        nd22pl = tk.StringVar()
        nd22pl_cb = ttk.Combobox(nd22l3, width=5, textvariable=nd22pl)
        nd22pl_cb['values'] = lc.text[lang]['prawylewy']
        nd22pl_cb['state'] = 'readonly'
        nd22pl_cb.pack(side='left', pady=1)

        nd22l4tornr = ttk.Label(nd22l3, text=lc.text[lang]['tornr'], anchor="w")
        nd22l4tornr.pack(side='left', padx=5,)

        nd22tor = tk.StringVar()
        nd22tor = tk.Entry(nd22l3, textvariable=nd22tor, width=2)
        nd22tor.pack(side='left', padx=5, pady=1)

        sep23 = ttk.Separator(Nroot, orient='horizontal')
        sep23.pack(fill='x')

        # Section 3
        nd3 = tk.Frame(Nroot)
        nd3.pack()

        nd3no = ttk.Label(nd3, text=' 3.', font='bold', anchor="nw")
        nd3no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        nd31 = tk.Frame(nd3)
        nd31.grid(row=0, column=1)

        nd31n = tk.BooleanVar()
        nd31n.set(False)
        nd31need = tk.Checkbutton(nd31, var=nd31n)
        nd31need.grid(row=0, column=0)

        nd31l1 = tk.Frame(nd31)
        nd31l1.grid(row=0, column=1, sticky="w")

        nd31jp = tk.StringVar()
        nd31jp_cb = ttk.Combobox(nd31l1, width=lc.text[lang]['jzdpopsz'],
                                 textvariable=nd31jp)
        nd31jp_cb['values'] = lc.text[lang]['jzdpop']
        nd31jp_cb['state'] = 'readonly'
        nd31jp_cb.pack(side='left', pady=1)

        nd31l1txt = ttk.Label(nd31l1, text=lc.text[lang]['odb'],
                              anchor="w")
        nd31l1txt.pack(side='left', padx=5, pady=1)

        nd31l2 = tk.Frame(nd31)
        nd31l2.grid(row=1, column=1, sticky="w")

        nd31kier = tk.StringVar()
        nd31kier = tk.Entry(nd31l2, textvariable=nd31kier, width=20)
        nd31kier.pack(side='left', pady=1)

        nd31l2txt = ttk.Label(nd31l2, text=lc.text[lang]['udo'] + ' km',
                              anchor="w")
        nd31l2txt.pack(side='left', padx=5, pady=1)

        nd31km = tk.StringVar()
        nd31dokm = tk.Entry(nd31l2, textvariable=nd31km, width=5)
        nd31dokm.pack(side='left', pady=1)

        nd31l2ska = ttk.Label(nd31l2, text=lc.text[lang]['skad'], anchor="w")
        nd31l2ska.pack(side='left', padx=5, pady=1)

        nd31l3 = tk.Frame(nd31)
        nd31l3.grid(row=2, column=1, sticky="w")

        nd31pp = tk.StringVar()
        nd31pp_cb = ttk.Combobox(nd31l3, width=9, textvariable=nd31pp)
        nd31pp_cb['values'] = lc.text[lang]['pocpop']
        nd31pp_cb['state'] = 'readonly'
        nd31pp_cb.pack(side='left', pady=1)

        nd31l3txt = ttk.Label(nd31l3, text=lc.text[lang]['wroc'] +
                              lc.text[lang]['nr'], anchor="w")
        nd31l3txt.pack(side='left', padx=5, pady=1)

        nd31tor = tk.StringVar()
        nd31toradd = tk.Entry(nd31l3, textvariable=nd31tor, width=4)
        nd31toradd.pack(side='left', pady=1)

        nd31l3txt2= ttk.Label(nd31l3, text=lc.text[lang]['najpoz'],
                              anchor="w")
        nd31l3txt2.pack(side='left', padx=5, pady=1)

        nd31l4 = tk.Frame(nd31)
        nd31l4.grid(row=3, column=1, sticky="w")

        nd31l4txt= ttk.Label(nd31l4, text=lc.text[lang]['ogodz2'],
                              anchor="w")
        nd31l4txt.pack(side='left', pady=2)

        nd31godz = tk.StringVar()
        nd31godzadd = tk.Entry(nd31l4, textvariable=nd31godz, width=4)
        nd31godzadd.pack(side='left', padx=5, pady=1)

        nd31l4txt2= ttk.Label(nd31l4, text=lc.text[lang]['min'],
                              anchor="w")
        nd31l4txt2.pack(side='left', pady=1)

        nd31min = tk.StringVar()
        nd31minadd = tk.Entry(nd31l4, textvariable=nd31min, width=4)
        nd31minadd.pack(side='left', padx=5, pady=1)

        sep34 = ttk.Separator(Nroot, orient='horizontal')
        sep34.pack(fill='x')

        # Section 4
        nd4 = tk.Frame(Nroot)
        nd4.pack()

        nd4no = ttk.Label(nd4, text=' 4.', font='bold', anchor="nw")
        nd4no.grid(row=0, column=0, sticky="nw", padx=5, pady=2)

        nd40l1 = tk.Frame(nd4)
        nd40l1.grid(row=0, column=2, sticky="w")

        nd40l1txt= ttk.Label(nd40l1, text=lc.text[lang]['wjaztor'] +
                             lc.text[lang]['nr'], anchor="w")
        nd40l1txt.pack(side='left', pady=1)

        nd40tor = tk.StringVar()
        nd40toradd = tk.Entry(nd40l1, textvariable=nd40tor, width=3)
        nd40toradd.pack(side='left', padx=5, pady=1)

        nd40l1txt2= ttk.Label(nd40l1, text=lc.text[lang]['na']+' ', anchor="w")
        nd40l1txt2.pack(side='left', pady=1)

        nd40sp = tk.StringVar()
        nd40sp_cb = ttk.Combobox(nd40l1, width=lc.text[lang]['stapodgsz'],
                                 textvariable=nd40sp)
        nd40sp_cb['values'] = lc.text[lang]['stapodg']
        nd40sp_cb['state'] = 'readonly'
        nd40sp_cb.pack(side='left', pady=1)

        nd40l2 = tk.Frame(nd4)
        nd40l2.grid(row=1, column=2, sticky="w")

        nd40sta = tk.StringVar()
        nd40staadd = tk.Entry(nd40l2, textvariable=nd40sta, width=18)
        nd40staadd.pack(side='left', padx=5, pady=1)

        nd40l2txt= ttk.Label(nd40l2, text=lc.text[lang]['odbe'], anchor="w")
        nd40l2txt.pack(side='left', pady=1)

        nd41n = tk.BooleanVar()
        nd41n.set(False)
        nd41need = tk.Checkbutton(nd4, var=nd41n)
        nd41need.grid(row=2, column=1)

        nd41l1 = ttk.Label(nd4, text=lc.text[lang]['sz1'], anchor="w")
        nd41l1.grid(row=2, column=2, sticky="w")

        nd41l2 = tk.Frame(nd4)
        nd41l2.grid(row=3, column=2, sticky="w")

        nd41l2txt= ttk.Label(nd41l2, text=lc.text[lang]['sz2'], anchor="w")
        nd41l2txt.pack(side='left')

        nd41pl = tk.StringVar()
        nd41pl_cb = ttk.Combobox(nd41l2, width=5, textvariable=nd41pl)
        nd41pl_cb['values'] = lc.text[lang]['lewprawej']
        nd41pl_cb['state'] = 'readonly'
        nd41pl_cb.pack(side='left', padx=5, pady=2)

        nd41l2txt= ttk.Label(nd41l2, text=lc.text[lang]['sz3'], anchor="w")
        nd41l2txt.pack(side='left')

        nd42n = tk.BooleanVar()
        nd42n.set(False)
        nd42need = tk.Checkbutton(nd4, var=nd42n)
        nd42need.grid(row=4, column=1)

        nd42l1 = ttk.Label(nd4, text=lc.text[lang]['rpn'], anchor="w")
        nd42l1.grid(row=4, column=2, sticky="w")

        sep45 = ttk.Separator(Nroot, orient='horizontal')
        sep45.pack(fill='x')

        # Section 5
        nd5 = tk.Frame(Nroot)
        nd5.pack()

        nd5no = ttk.Label(nd5, text=' 5.', font='bold', anchor="nw")
        nd5no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        nd51 = tk.Frame(nd5)
        nd51.grid(row=0, column=1)

        nd51n = tk.BooleanVar()
        nd51n.set(False)
        nd51need = tk.Checkbutton(nd51, var=nd51n)
        nd51need.grid(row=0, column=0)

        nd51l1 = tk.Frame(nd51)
        nd51l1.grid(row=0, column=1, sticky='w')

        nd51l1txt = ttk.Label(nd51l1, text=lc.text[lang]['zezwje'] +
                              lc.text[lang]['nr'], anchor="w")
        nd51l1txt.pack(side='left')

        nd51tor = tk.StringVar()
        nd51toradd = tk.Entry(nd51l1, textvariable=nd51tor, width=4)
        nd51toradd.pack(side='left', padx=5, pady=1)

        nd51l1txt2= ttk.Label(nd51l1, text=lc.text[lang]['zkier1'], anchor="w")
        nd51l1txt2.pack(side='left')

        nd51l2 = tk.Frame(nd51)
        nd51l2.grid(row=1, column=1)

        nd51l2txt1= ttk.Label(nd51l2, text=lc.text[lang]['zkier2'], anchor="w")
        nd51l2txt1.pack(side='left')

        nd51kier = tk.StringVar()
        nd51zsta = tk.Entry(nd51l2, textvariable=nd51kier, width=32-lc.text[lang]['stapodgsz'])
        nd51zsta.pack(side='left', padx=5, pady=1)

        nd51l2txt2= ttk.Label(nd51l2, text=lc.text[lang]['na'], anchor="w")
        nd51l2txt2.pack(side='left')

        nd51sp = tk.StringVar()
        nd51sp_cb = ttk.Combobox(nd51l2, width=lc.text[lang]['stapodgsz'],
                                 textvariable=nd51sp)
        nd51sp_cb['values'] = lc.text[lang]['stapodg']
        nd51sp_cb['state'] = 'readonly'
        nd51sp_cb.pack(side='left', padx=5, pady=1)

        nd51l3 = tk.Frame(nd51)
        nd51l3.grid(row=2, column=1, stick='w')

        nd51sta = tk.StringVar()
        nd51staadd = tk.Entry(nd51l3, textvariable=nd51sta, width=17)
        nd51staadd.pack(side='left', pady=1)

        nd51l3txt1= ttk.Label(nd51l3, text=lc.text[lang]['iprzeje'], anchor="w")
        nd51l3txt1.pack(side='left', padx=5)

        nd51sem = tk.StringVar()
        nd51semadd = tk.Entry(nd51l3, width=4)
        nd51semadd.pack(side='left', pady=1)

        sep56 = ttk.Separator(Nroot, orient='horizontal')
        sep56.pack(fill='x')

        # Section 6
        nd6 = tk.Frame(Nroot)
        nd6.pack()

        nd6no = ttk.Label(nd6, text=' 6.', font='bold', anchor="nw")
        nd6no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        nd61 = tk.Frame(nd6)
        nd61.grid(row=0, column=1)

        nd61n = tk.BooleanVar()
        nd61n.set(False)
        nd61need = tk.Checkbutton(nd61, var=nd61n)
        nd61need.grid(row=0, column=0)

        nd61l1 = ttk.Label(nd61, text=lc.text[lang]['inne'], anchor="w")
        nd61l1.grid(row=0, column=1, sticky="nw")

        nd61txt = tk.Text(nd61, font=("Helvetica", 9), width=52, height=3)
        nd61txt.grid(row=1, column=1, sticky="nw", pady=1)

        # O ===================================================================
        # First line
        l1 = tk.Frame(Oroot)

        # label
        rp = ttk.Label(l1, text=lc.text[lang]['rp']+': "O" ' + lc.text[lang]['nr'])
        rp.pack(side='left', padx=5, pady=5)

        # number entrybox
        orpno = tk.StringVar()
        Order_no = tk.Entry(l1, textvariable=nrpno, width=5)
        Order_no.pack(side='left', padx=5, pady=5)
        l1.pack()

        # Second line
        l2 = tk.Frame(Oroot)

        # number label
        trno = ttk.Label(l2, text=lc.text[lang]['dla'])
        trno.pack(side='left', padx=5, pady=5)

        # train type
        opmtype = tk.StringVar()
        opmtype_cb = ttk.Combobox(l2, width=9, textvariable=opmtype)
        opmtype_cb['values'] = lc.text[lang]['pocman']
        opmtype_cb['state'] = 'readonly'
        opmtype_cb.pack(side='left', padx=5, pady=5)

        # number entrybox
        otrno = tk.StringVar()
        Train_no = tk.Entry(l2, textvariable=otrno, width=7)
        Train_no.pack(side='left', padx=5, pady=5)

        l2.pack()

        topsep = ttk.Separator(Oroot, orient='horizontal')
        topsep.pack(fill='x')

        # Sections ------------------------------------------------------------
        # Section 1
        od1 = tk.Frame(Oroot)
        od1.pack()

        od11no = ttk.Label(od1, text=' 1.', font='bold', anchor="nw")
        od11no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        od11l1 = ttk.Label(od1, text=lc.text[lang]['1)'], anchor="w")
        od11l1.grid(row=0, column=1, sticky="nw")

        od11l2 = ttk.Label(od1, text=lc.text[lang]['2)'], anchor="w")
        od11l2.grid(row=1, column=1, sticky="nw")

        od12 = tk.Frame(od1)
        od12.grid(row=2, column=1)

        od12l00 = ttk.Label(od12, text=lc.text[lang]['napost'], anchor="c")
        od12l00.grid(row=0, column=0)

        od12l01 = ttk.Label(od12, text=lc.text[lang]['od'] + '\nkm', anchor="c")
        od12l01.grid(row=0, column=1)

        od12l02 = ttk.Label(od12, text=lc.text[lang]['do'] + '\nkm', anchor="c")
        od12l02.grid(row=0, column=2)

        od12l03 = ttk.Label(od12, text='1)\n2)', anchor="c")
        od12l03.grid(row=0, column=3)

        od12l04 = ttk.Label(od12, text=lc.text[lang]['powod'], anchor="c")
        od12l04.grid(row=0, column=4)

        # Line 1
        od12l10 = tk.Text(od12, font=("Helvetica", 9), width=22, height=2)
        od12l10.grid(row=1, column=0, sticky="nw", pady=1)

        od12l11 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l11.grid(row=1, column=1, sticky="nw", pady=1)

        od12l12 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l12.grid(row=1, column=2, sticky="nw", pady=1)

        od12l13 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l13.grid(row=1, column=3, sticky="nw", pady=1)

        od12l14 = tk.Text(od12, font=("Helvetica", 9), width=16, height=2)
        od12l14.grid(row=1, column=4, sticky="nw", pady=1)

        # Line 2
        od12l20 = tk.Text(od12, font=("Helvetica", 9), width=22, height=2)
        od12l20.grid(row=2, column=0, sticky="nw", pady=1)

        od12l21 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l21.grid(row=2, column=1, sticky="nw", pady=1)

        od12l22 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l22.grid(row=2, column=2, sticky="nw", pady=1)

        od12l23 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l23.grid(row=2, column=3, sticky="nw", pady=1)

        od12l24 = tk.Text(od12, font=("Helvetica", 9), width=16, height=2)
        od12l24.grid(row=2, column=4, sticky="nw", pady=1)

        # Line 3
        od12l30 = tk.Text(od12, font=("Helvetica", 9), width=22, height=2)
        od12l30.grid(row=3, column=0, sticky="nw", pady=1)

        od12l31 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l31.grid(row=3, column=1, sticky="nw", pady=1)

        od12l32 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l32.grid(row=3, column=2, sticky="nw", pady=1)

        od12l33 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l33.grid(row=3, column=3, sticky="nw", pady=1)

        od12l34 = tk.Text(od12, font=("Helvetica", 9), width=16, height=2)
        od12l34.grid(row=3, column=4, sticky="nw", pady=1)

        # Line 4
        od12l40 = tk.Text(od12, font=("Helvetica", 9), width=22, height=2)
        od12l40.grid(row=4, column=0, sticky="nw", pady=1)

        od12l41 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l41.grid(row=4, column=1, sticky="nw", pady=1)

        od12l42 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l42.grid(row=4, column=2, sticky="nw", pady=1)

        od12l43 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l43.grid(row=4, column=3, sticky="nw", pady=1)

        od12l44 = tk.Text(od12, font=("Helvetica", 9), width=16, height=2)
        od12l44.grid(row=4, column=4, sticky="nw", pady=1)

        # Line 5
        od12l50 = tk.Text(od12, font=("Helvetica", 9), width=22, height=2)
        od12l50.grid(row=5, column=0, sticky="nw", pady=1)

        od12l51 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l51.grid(row=5, column=1, sticky="nw", pady=1)

        od12l52 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l52.grid(row=5, column=2, sticky="nw", pady=1)

        od12l53 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l53.grid(row=5, column=3, sticky="nw", pady=1)

        od12l54 = tk.Text(od12, font=("Helvetica", 9), width=16, height=2)
        od12l54.grid(row=5, column=4, sticky="nw", pady=1)

        # Line 3
        od12l60 = tk.Text(od12, font=("Helvetica", 9), width=22, height=2)
        od12l60.grid(row=6, column=0, sticky="nw", pady=1)

        od12l61 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l61.grid(row=6, column=1, sticky="nw", pady=1)

        od12l62 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l62.grid(row=6, column=2, sticky="nw", pady=1)

        od12l63 = tk.Text(od12, font=("Helvetica", 9), width=5, height=2)
        od12l63.grid(row=6, column=3, sticky="nw", pady=1)

        od12l64 = tk.Text(od12, font=("Helvetica", 9), width=16, height=2)
        od12l64.grid(row=6, column=4, sticky="nw", pady=1)

        sep12 = ttk.Separator(Oroot, orient='horizontal')
        sep12.pack(fill='x')

        # Section 2
        od2 = tk.Frame(Oroot)
        od2.pack()

        od2no = ttk.Label(od2, text=' 2.', font='bold', anchor="nw")
        od2no.grid(row=0, column=0, sticky="nw", padx=5, pady=1)

        od21 = tk.Frame(od2)
        od21.grid(row=0, column=1)

        od21n = tk.BooleanVar()
        od21n.set(False)
        od21need = tk.Checkbutton(od21, var=od21n)
        od21need.grid(row=0, column=0)

        od21l1 = ttk.Label(od21, text=lc.text[lang]['inne'], anchor="w")
        od21l1.grid(row=0, column=1, sticky="nw")

        od21txt = tk.Text(od21, font=("Helvetica", 9), width=52, height=6)
        od21txt.grid(row=1, column=1, sticky="nw", pady=1)


        # Bottom --------------------------------------------------------------
        botbut = tk.Frame(master)
        botbut.pack()

        bot = tk.Frame(botbut)
        bot.grid(row=0, column=0, padx=20)

        botstalab = ttk.Label(bot, text=lc.text[lang]['stacja'])
        botstalab.grid(row=0, column=0)

        station = tk.StringVar()
        botsta = ttk.Combobox(bot, width=25, textvariable=station)
        botsta['values'] = stations
        botsta.grid(row=1, column=0)

        botposlab = ttk.Label(bot, text=lc.text[lang]['poster'])
        botposlab.grid(row=0, column=1)

        post = tk.StringVar()
        botpos = ttk.Combobox(bot, width=4, textvariable=post)
        botpos['values'] = posts
        botpos.grid(row=1, column=1)

        botposlan = ttk.Label(bot, text='lang.')
        botposlan.grid(row=0, column=2)

        outlang = tk.StringVar()
        botlan = ttk.Combobox(bot, width=3, textvariable=outlang)
        botlan['values'] = lc.langlist
        botlan.grid(row=1, column=2)

        def generator():
            rptype = tabs.index('current')
            t = datetime.datetime.now()
            olang = outlang.get()
            if olang == '':
                olang = 'PL'

            def chlang(inl, outl, s, ans):
                i = 0
                for j in lc.text[inl][s]:
                    if j == ans:
                        return lc.text[outl][s][i]
                    else:
                        i+=1

            def trimmer(string):
                wordlist = string.split(' ')
                counter = 0
                outstring = '┃     ┃   '
                for word in wordlist:
                    if len(word) + counter > 64:
                        outstring += "                                                                                                                                     "
                        outstring += '┃     ┃   ' + word + ' '
                        counter = len(word) + 1
                    else:
                        outstring += word + ' '
                        counter += len(word) + 1
                return outstring

            output= '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
            te = 0
            if rptype == 0:
                td2 = 0
                td4 = 0
                if outlang.get() == 'EN': # Rozkaz S Ang
                    output+="┃     <b>Written order „S” Nr <i>" + srpno.get()
                    output+="</i></b>                                                                                                                                     "
                    output+="┃ For " + chlang(lang, olang, 'pocman', spmtype.get())
                    output+=" <i>" + strno.get() + "</i>  date <i>" + t.strftime('%d.%m.%Y')
                    output+="</i>                                                                                                                                     "
                    output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    if sd11n.get() == True:
                        output+="┃ <b>1</b>  ┃  I give permission afer recieving " + chlang(lang, olang, 'otrzym', sd11_command.get()) + " to:"
                        output+="                                                                                                                                     "
                        output+='┃     ┃ ─ Pass the signal displaying a "Stop" signal aspect:                                                                                                                                     '
                        output+='┃     ┃   ' + chlang(lang, olang, 'semwyjazd', sd11_stype.get()) + " " + sd11sem.get()
                        output+='                                                                                                                                     '
                        te = 1
                    if sd12n.get() == True:
                        if te == 1:
                            output+="┃     ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                          "
                        else:
                            output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃     ┃ ─ Depart from track No: <i>" + sd12tor.get()
                        output+="</i> which does not posess an                                                                                                                                     "
                        output+="┃     ┃   exit signal                                                                                                                                     "
                        te = 1
                    if sd21n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        else:
                            output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>2</b>  ┃  I give permission afer recieving " + chlang(lang, olang, 'otrzym', sd21_command.get()) + " to:"
                        output+="                                                                                                                                     "
                        output+='┃     ┃ ─ Pass the signal displaying a "Stop" signal aspect:                                                                                                                                     '
                        output+='┃     ┃   ' + chlang(lang, olang, 'semwjazd', sd21_stype.get()) + " " + sd21sem.get()
                        output+='                                                                                                                                     '
                        te = 1
                        td2 = 1
                    if sd22n.get() == True:
                        if te == 1 and td2 == 0:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        elif te == 1 and td2 == 1:
                            output+="┃     ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                          "
                        else:
                            output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃     ┃ ─ Depart from track No: <i>" + sd22tor.get()
                        output+="</i> which does not posess an                                                                                                                                     "
                        output+="┃     ┃   exit signal                                                                                                                                     "
                        te = 1
                    if sd31n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        else:
                            output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>3</b>  ┃  From km <i>" + sd31od.get() + "</i>  to km <i>" + sd31do.get()
                        output+="</i>  over track No. <i>" + sd31tor.get()
                        output+="</i>  traffic is directed                                                                                    "
                        output+="┃     ┃   between the interval of follow-up posts. Aspects on SBL                                                                                    "
                        output+="┃     ┃   automatic block signals are invalid. Maintain caution from                                                                                    "
                        output+='┃     ┃   the last signal with "W18" indicator. Line clear, last                                                                                    '
                        output+="┃     ┃   train No.<i>" + sd31poc.get() + " </i>arrived at <i>" + sd31pdo.get()
                        output+="</i>                                                                                    "
                        output+="┃     ┃   at time <i>" + sd31godz.get()
                        output+="</i>                                                                                    "
                    if sd41n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>4</b>  ┃  Other:                                                                                    "
                        output+="                                                                                                                                      "
                        output+=trimmer(sd41txt.get("1.0","end-1c"))

                else:  # Rozkaz S Pol
                    output+="┃     <b>Rozkaz pisemny „S” Nr <i>" + srpno.get()
                    output+="</i></b>                                                                                                                                     "
                    output+="┃ dla " + chlang(lang, olang, 'pocman', spmtype.get())
                    output+=" <i>" + strno.get() + "</i>  dnia <i>" + t.strftime('%d.%m.%Y')
                    output+="</i>                                                                                                                                     "
                    output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    if sd11n.get() == True:
                        output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>1</b>  ┃  Zezwalam po otrzymaniu " + chlang(lang, olang, 'otrzym',sd11_command.get())
                        output+="                                                                                                                                     "
                        output+="┃     ┃ ─ przejechać obok wskazującego sygnał „Stój” semafora                                                                                                                                     "
                        output+='┃     ┃   <i>' + chlang(lang, olang, 'semwyjazd', sd11_stype.get()) + "</i> <i>" + sd11sem.get()
                        output+='                                                                                                                                     '
                        te = 1
                    if sd12n.get() == True:
                        if te == 1:
                            output+="┃     ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                           "
                        else:
                            output+="┃ <b>1</b>  ┃ Zezwalam po otrzymaniu " + chlang(lang, olang, 'otrzym',sd11_command.get())
                            output+="                                                                                                                                     "
                        output+="┃     ┃ ─ wyjechać z toru nr <i>" + sd12tor.get()
                        output+="</i> nie posiadającego semafora                                                                                                                                     "
                        output+="┃     ┃   wyjazdowego                                                                                                                                     "
                        te = 1
                    if sd21n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>2</b>  ┃  Zezwalam po otrzymaniu " + chlang(lang, olang, 'otrzym',sd21_command.get())
                        output+="                                                                                                                                     "
                        output+="┃     ┃ ─ przejechać obok wskazującego sygnał „Stój” semafora                                                                                                                                     "
                        output+='┃     ┃   <i>' + chlang(lang, olang, 'semwyjazd', sd21_stype.get()) + "</i> <i>" + sd21sem.get()
                        output+='                                                                                                                                     '
                        te = 1
                        td2 = 1
                    if sd22n.get() == True:
                        if te == 1 and td2 == 0:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                            output+="┃ <b>2</b>  ┃ Zezwalam po otrzymaniu " + chlang(lang, olang, 'otrzym',sd21_command.get())
                            output+="                                                                                                                                     "
                        elif te == 1 and td2 == 1:
                            output+="┃     ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                          "
                        else:
                            output+="┃ <b>2</b>  ┃ Zezwalam po otrzymaniu " + chlang(lang, olang, 'otrzym',sd21_command.get())
                            output+="                                                                                                                                     "
                        output+="┃     ┃ ─ wjechać z toru nr <i>" + sd22tor.get()
                        output+="</i> nie posiadającego semafora                                                                                                                                     "
                        output+="┃     ┃   wjazdowego                                                                                                                                     "
                        te = 1
                    if sd31n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>3</b>  ┃  Od km <i>" + sd31od.get() + "</i>  do km <i>" + sd31do.get()
                        output+="</i>  po torze nr <i>" + sd31tor.get()
                        output+="</i>  ruch pociągów                                                                                    "
                        output+="┃     ┃   prowadzony jest w odstępie posterunków następczych. Wskazania                                                                                    "
                        output+="┃     ┃   semaforów sbl są nieważne. Zachować ostrożność od ostatniego                                                                                    "
                        output+="┃     ┃   semafora ze wskaźnikiem „W18”. Szlak wolny, ostatni pociąg                                                                                    "
                        output+="┃     ┃   nr <i>" +sd31poc.get() + "</i> przybył do <i>" + sd31pdo.get()
                        output+="</i>                                                                                    "
                        output+="┃     ┃   o godzinie <i>" + sd31godz.get() + "."
                        output+="</i>                                                                                    "
                    if sd41n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>4</b>  ┃  Inne:                                                                                    "
                        output+="                                                                                                                                      "
                        output+=trimmer(sd41txt.get("1.0","end-1c"))
                output+="┣━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

            elif rptype == 1:
                td2 = 0
                if outlang.get() == 'EN':  # Rozkaz N Ang
                    output+="┃     <b>Written order „N” Nr <i>" + nrpno.get()
                    output+="</i></b>                                                                                                                                     "
                    output+="┃ For " + chlang(lang, olang, 'pocman', npmtype.get())
                    output+=" <i>" + ntrno.get() + "</i>  date <i>" + t.strftime('%d.%m.%Y')
                    output+="</i>                                                                                                                                     "
                    output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    if nd11n.get() == True:
                        output+="┃ <b>1</b>  ┃ From km <i>" + nd11od.get() + "</i>  to km <i>" + nd11do.get()
                        output+="</i>                                                                                                                                     "
                        output+="┃     ┃    Track No. <i>" + nd11tor1.get() + "</i> is closed, bi-directional"
                        output+="                                                                                  "
                        output+="┃     ┃    single line running in place on track No. <i>" + nd11tor2.get() + "</i>"
                        output+="                                                                                  "
                        te = 1
                    if nd21n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>2</b>  ┃  I give permission, after recieving " + chlang(lang, olang, 'otrzym', nd21_command.get())
                        output+="                                                                                                                                     "
                        output+='┃     ┃ ─ pass the signal displaying a "stop" aspect                                                                                                                                     '
                        output+='┃     ┃   <i>' + chlang(lang, olang, 'semy', nd21_stype.get()) + "</i> <i>" + nd21sem.get()
                        output+='                                                                                                                                     '
                        output+="┃     ┃   and depart in direction of " + nd21kier.get()
                        output+="</i>                                                                                                                                   "
                        output+="┃     ┃   on the <i>" + chlang(lang, olang, 'prawylewy', nd21pl.get()) + '</i>  track No. <i>' + nd21tor.get()
                        output+="</i>                                                                                                                                   "
                        te = 1
                        td2 = 1
                    if nd22n.get() == True:
                        if te == 1 and td2 == 0:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                            output+="┃ <b>2</b>  ┃ I give permission, after recieving <i>" + chlang(lang, olang, 'otrzym', nd21_command.get())
                            output+="</i>                                                                                                                                     "
                        elif te == 1 and td2 == 1:
                            output+="┃     ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                          "
                        else:
                            output+="┃ <b>2</b>  ┃ I give permission, after recieving <i>" + chlang(lang, olang, 'otrzym', nd21_command.get())
                            output+="</i>                                                                                                                                     "
                        output+="┃     ┃   from track nr <i>" + nd22tor.get() + "</i>, which does not posess an"
                        output+="                                                                                                                                   "
                        output+="┃     ┃   exit signal and depart in the direction of <i>" + nd22kier.get() + "</i>"
                        output+="                                                                                                                                   "
                        output+="┃     ┃   on the <i>" + chlang(lang, olang, 'prawylewy', nd22pl.get()) + "</i>  track No. <i>" + nd22tor.get() + "</i>"

                        output+="                                                                                                                                   "
                    if nd31n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>3</b>  ┃  <i>" + chlang(lang, olang, 'jzdpop', nd31jp.get()) + "</i>  will take place in the direction of:"
                        output+="                                                                                                                                     "
                        output+="┃     ┃  <i>" + nd31kier.get() + "</i>  up to km <i>" + nd31km.get() + "</i>,  where the"
                        output+="                                                                                                                                     "
                        output+="┃     ┃  <i>" + nd31pp.get() + "</i>  is to return on left track No. <i>" + nd31tor.get()
                        output+="</i>                                                                                                                                     "
                        output+="┃     ┃  by latest hour <i>" + nd31godz.get() + "</i>  min. <i>" + nd31min.get()
                        output+="</i>                                                                                                                                     "
                        te = 1
                    if nd41n.get() == True or nd42n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>4</b>  ┃  Arrival from track nr <i>" + nd40tor.get() + "</i>  into"
                        output+="                                                                                                                                     "
                        output+="┃     ┃  <i>" + chlang(lang, olang, 'stapodg', nd40sp.get()) + nd40sta.get() + "</i>  will occur after:"
                        output+="                                                                                                                                     "
                        if nd41n.get() == True:
                            output+="┃     ┃ ─ the replacement signal „Sz” on separate device"
                            output+="                                                                                                                                    "
                            output+="┃     ┃   located on the <i>" + chlang(lang, olang, 'lewprawej', nd41pl.get()) + "</i> side of the track"
                            output+="                                                                                                                                    "
                        if nd42n.get() == True:
                            output+='┃     ┃ ─ written order "N"                                                                                                                                     '
                        te = 1
                    if nd51n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>5</b>  ┃  I give permission to enter from track No. <i>" + nd51tor.get()
                        output+="┃     ┃  from direction of <i>" + nd51kier.get()
                        output+="</i>                                                                                                                                      "
                        output+="┃     ┃  into <i>" + nd51sp.get() + nd51sta.get()
                        output+="</i>                                                                                                                                      "
                        output+='┃     ┃  and pass the signal indicating "stop" aspect <i>' + nd51sem.get()
                        output+="</i>                                                                                                                                      "
                        te = 1
                    if nd61n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>6</b>  ┃  Other:                                                                                    "
                        output+="                                                                                                                                      "
                        output+=trimmer(nd61txt.get("1.0","end-1c"))

                else: # Rozkaz N Pol
                    output+="┃     <b>Rozkaz pisemny „N” Nr <i>" + nrpno.get()
                    output+="</i></b>                                                                                                                                     "
                    output+="┃ dla " + chlang(lang, olang, 'pocman', npmtype.get())
                    output+=" <i>" + ntrno.get() + "</i>  dnia <i>" + t.strftime('%d.%m.%Y')
                    output+="</i>                                                                                                                                     "
                    output+="┣━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    if nd11n.get() == True:
                        output+="┃ <b>1</b>  ┃   Od <i>" + nd11od.get() + "</i>  do <i>" + nd11do.get()
                        output+="</i>                                                                                                                                     "
                        output+="┃     ┃   tor nr <i>" + nd11tor1.get() + "</i> jest zamknięty, ruch jednorowy"
                        output+="                                                                                  "
                        output+="┃     ┃   dwukierunkowy wprowadzono po torze nr <i>" + nd11tor2.get() + "</i>"
                        output+="                                                                                  "
                        te = 1
                    if nd21n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>2</b>  ┃   Zezwalam po otrzymaniu " + chlang(lang, olang, 'otrzym', nd21_command.get())
                        output+="                                                                                                                                     "
                        output+="┃     ┃ ─ przejechać obok wskazującego sygnał „Stój” semafora                                                                                                                                     "
                        output+='┃     ┃   ' + chlang(lang, olang, 'semy', nd21_stype.get()) + " " + nd21sem.get()
                        output+='                                                                                                                                     '
                        output+="┃     ┃   i wyjechać w kierunku " + nd21kier.get()
                        output+="                                                                                                                                   "
                        output+="┃     ┃   na tor szlakowy " + chlang(lang, olang, 'prawylewy', nd21pl.get()) + ' nr ' + nd21tor.get()
                        output+="                                                                                                                                   "
                        te = 1
                        td2 = 1
                    if nd22n.get() == True:
                        if te == 1 and td2 == 0:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                            output+="┃ <b>2</b>  ┃ Zezwalam po otrzymaniu <i>" + chlang(lang, olang, 'otrzym', nd21_command.get())
                            output+="</i>                                                                                                                                     "
                        elif te == 1 and td2 == 1:
                            output+="┃     ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                          "
                        else:
                            output+="┃ <b>2</b>  ┃   Zezwalam po otrzymaniu <i>" + chlang(lang, olang, 'otrzym', nd21_command.get())
                            output+="</i>                                                                                                                                     "
                        output+="┃     ┃   z toru nr <i>" + nd22tor.get() + "</i> nie posiadającego semafora"
                        output+="                                                                                                                                   "
                        output+="┃     ┃   wyjazdowego wyjechać w kierunku <i>" + nd22kier.get() + "</i>"
                        output+="                                                                                                                                   "
                        output+="┃     ┃   na tor szlakowy <i>" + chlang(lang, olang, 'prawylewy', nd22pl.get()) + "</i> nr <i>" + nd22tor.get() + "</i>"

                        output+="                                                                                                                                   "
                    if nd31n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>3</b>  ┃  <i>" + chlang(lang, olang, 'jzdpop', nd31jp.get()) + "</i>  pociągu odbędzie się w kierunku:"
                        output+="                                                                                                                                     "
                        output+="┃     ┃   <i>" + nd31kier.get() + "</i>  do km <i>" + nd31km.get() + "</i>  skąd"
                        output+="                                                                                                                                     "
                        output+="┃     ┃   <i>" + nd31pp.get() + "</i> ma wrócić po torze lewym nr <i>" + nd31tor.get()
                        output+="</i>                                                                                                                                     "
                        output+="┃     ┃   najpóźniej o godz. <i>" + nd31godz.get() + "</i>  min. <i>" + nd31min.get()
                        output+="</i>                                                                                                                                     "
                        te = 1
                    if nd41n.get() == True or nd42n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>4</b>  ┃   Wjazd z toru szlakowego nr <i>" + nd40tor.get()
                        output+="</i>                                                                                                                                     "
                        output+="┃     ┃   na <i>" + chlang(lang, olang, 'stapodg', nd40sp.get()) + nd40sta.get()
                        output+="</i>                                                                                                                                     "
                        output+="┃     ┃   odbędzie się po otrzymaniu:                                                                                                                                     "
                        if nd41n.get() == True:
                            output+="┃     ┃ ─ sygnału „Sz” na osobowym urządzeniu "
                            output+="                                                                                                                                    "
                            output+="┃     ┃    ustawionym z <i>" + chlang(lang, olang, 'lewprawej', nd41pl.get()) + "</i> strony toru"
                            output+="                                                                                                                                    "
                        if nd42n.get() == True:
                            output+="┃     ┃ ─ rozkazu pisemnego „N”                                                                                                                                     "
                        te = 1
                    if nd51n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>5</b>  ┃  Zezwalam wyjechać z toru szlakowego nr <i>" + nd51tor.get()
                        output+="┃     ┃  z kierunku <i>" + nd51kier.get()
                        output+="</i>                                                                                                                                      "
                        output+="┃     ┃  na <i>" + nd51sp.get() + nd51sta.get()
                        output+="</i>                                                                                                                                      "
                        output+="┃     ┃  i przejechać obok sygnału „Stój” na <i>" + nd51sem.get()
                        output+="</i>                                                                                                                                      "
                        te = 1
                    if nd61n.get() == True:
                        if te == 1:
                            output+="┣━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>6</b>  ┃  Inne:                                                                                    "
                        output+="                                                                                                                                      "
                        output+=trimmer(nd61txt.get("1.0","end-1c"))
                output+="┣━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

            elif rptype == 2:
                if outlang.get() == 'EN':  # Rozkaz O Ang
                    output+="┃     <b>Written order „O” Nr <i>" + orpno.get()
                    output+="</i></b>                                                                                                                                     "
                    output+="┃ For " + chlang(lang, olang, 'pocman', opmtype.get())
                    output+=" <i>" + otrno.get() + "</i>  date <i>" + t.strftime('%d.%m.%Y')
                    output+="</i>                                                                                                                                     "
                    if od21n.get() == True:
                        if te == 1:
                            output+="┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>2</b>   Other:                                                                                    "
                        output+="                                                                                                                                      "
                        output+=trimmer(nd61txt.get("1.0","end-1c"))
                else: # Rozkaz O Pol
                    output+="┃     <b>Rozkaz pisemny „O” Nr <i>" + orpno.get()
                    output+="</i></b>                                                                                                                                     "
                    output+="┃ dla " + chlang(lang, olang, 'pocman', opmtype.get())
                    output+=" <i>" + otrno.get() + "</i>  dnia <i>" + t.strftime('%d.%m.%Y')
                    output+="</i>                                                                                                                                     "
                    if od21n.get() == True:
                        if te == 1:
                            output+="┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                        output+="┃ <b>2</b>   Inne:                                                                                    "
                        output+="                                                                                                                                      "
                        output+=trimmer(nd61txt.get("1.0","end-1c"))
                        output+="┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

            # Wszystkie rozkazy:
            output+="┃  <i>" + station.get() + "</i> ┃ <i>" + post.get()
            if outlang.get() == 'EN':  # Ang
                if master.drpolec.get() == 'z polecenia DR / On order of dispatcher':
                    output+="┣━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    output+="┃  On order of dispatcher ┃ <i>" + master.username.get()
                    output+="</i>                                                                                                                                     "
                    output+="┣━━━━━━━━━━━━━━━━━┳┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                else:
                    output+="┣━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    output+="┃  Dispatcher ┃ <i>" + master.username.get()
                    output+="</i>                                                                                                                                     "
                    output+="┣━━━━━━━━━━┻━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                output+="┃ Order Recieved Driver ┃"
                output+="                                                                                                                                      "
                output+="┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            else: # Pol
                if master.drpolec.get() == 'z polecenia DR / On order of dispatcher':
                    output+="┣━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    output+="┃  z polecenia dyżurnego ruchu  ┃ <i>" + master.username.get()
                    output+="</i>                                                                                                                                     "
                    output+="┣━━━━━━━━━━━━━━━━┳━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                else:
                    output+="┣━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    output+="┃  dyżurny ruchu ┃ <i>" + master.username.get()
                    output+="</i>                                                                                                                                     "
                    output+="┣━━━━━━━━━━━━┻━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                output+="┃  Rozkaz otrzymałem  ┃"
                output+="                                                                                                                                      "
                output+="┗━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

            # Kopiuj do schowka
            cp = tk.Tk()
            cp.withdraw()
            cp.clipboard_clear()
            cp.clipboard_append(output)
            cp.destroy()

        genbutton = tk.Button(botbut, command=generator,
                              text=lc.text[lang]['kop'], padx=5)
        genbutton.grid(row=0, column=1, padx=5, pady=20)


# Driver Code
if __name__ == "__main__":
    app = Rozkazownik()
    app.mainloop()
