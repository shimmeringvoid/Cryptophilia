'''
 File: CryptophiliaGUI.py

 Author: Rafael Espericueta
         Professor of Mathematics
         Bakersfield College

 Desc: Encodes or decodes text and text files with user entered key.
       The key consists of an irrational number.  Some examples:
            pi,  pi**2, exp(3.14), sqrt(127), sqrt(5+pi), etc...
            
 Feel free to use this as you like, free of any copyright concerns;
 please just keep it thusly unemcumbered, credit the author,
 & have fun!
 
'''
import string as st
import Tkinter as tk
import tkSimpleDialog, tkFileDialog, tkMessageBox
from CryptoClass import crypto


class CryptoGUI_tk(tk.Frame):
    #
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Cryptophilia!")
        self.parent.config(width=1000, height=900)
        
        # create a menu bar
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        #self.parent.grid()

        # create the main pulldown menus
        filemenu = tk.Menu(menubar, tearoff=0)
        helpmenu = tk.Menu(menubar, tearoff=0)

        # File Menu
        menubar.add_cascade( label="File", menu=filemenu, underline=0)
        filemenu.add_command(label="Open file to be encrypted",
                             command=self.open_text, underline=0)
        filemenu.add_command(label="Open file to be decrypted",
                             command=self.open_codedtext)
        filemenu.add_separator()
        filemenu.add_command(label="Save decrypted file",
                             command=self.save_text)
        filemenu.add_command(label="Save encrypted file",
                             command=self.save_codedtext, underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="New encryption key",
                             command=self.enter_newkey, underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",
                             command=self.parent.quit, underline=0)
 
        # Help Menu
        menubar.add_cascade( label="Help", menu=helpmenu, underline=0)
        helpmenu.add_command(label="About",
                             command=self.About, underline=0)
                
        #---- Non-menu related initializations ----  

        bigframe = tk.Frame(self.parent, width=800, height=800)   # more initializations needed?
        bigframe.grid(row=0, column=0)

        blanktext1_label = tk.Label(bigframe, text="  ")
        blanktext1_label.grid(row=0, column=0)
        
        decodedtext_label = tk.Label(bigframe, text="Decoded Text:")
        decodedtext_label.grid(row=1, column=1, sticky=tk.W)
        decodedtext_frame = tk.Frame(bigframe, width=1000, height=400)
        decodedtext_frame.grid(row=2, column=1)

        #decodedtext_frame.grid_rowconfigure(0, weight=1)  # to help the scrollbar resize properly
        decodedtext_frame.grid_columnconfigure(0, weight=1)
        scrollbarD = tk.Scrollbar(decodedtext_frame)
        scrollbarD.grid(row=0, column=1, sticky=tk.N+tk.S)  
        self.decodedtext = tk.Text(decodedtext_frame, wrap=tk.WORD, yscrollcommand=scrollbarD.set)
        scrollbarD.config(command=self.decodedtext.yview)
        self.decodedtext.grid(row=0, column=0)

        encodedtext_label = tk.Label(bigframe, text="Encoded Text:")
        encodedtext_label.grid(row=1, column=3, sticky=tk.W)
        encodedtext_frame = tk.Frame(bigframe, width=1000, height=400)
        encodedtext_frame.grid(row=2, column=3)

        encodedtext_frame.grid_columnconfigure(0, weight=1)
        scrollbarE = tk.Scrollbar(encodedtext_frame)
        scrollbarE.grid(row=0, column=1, sticky=tk.N+tk.S)  
        self.encodedtext = tk.Text(encodedtext_frame, yscrollcommand=scrollbarE.set)
        scrollbarE.config(command=self.encodedtext.yview)
        self.encodedtext.grid(row=0, column=0)

        EncodeButton = tk.Button(bigframe, text="Encode", 
                              borderwidth=1, command=self.On_EncodeButton,)
        EncodeButton.grid(row=3, column=1, padx=15, pady=15, sticky=tk.E)

        ResetButton = tk.Button(bigframe, text="Reset", 
                              borderwidth=1, command=self.On_ResetButton,)
        ResetButton.grid(row=3, column=2, padx=0, pady=15)

        DecodeButton = tk.Button(bigframe, text="Decode", 
                              borderwidth=1, command=self.On_DecodeButton,)
        DecodeButton.grid(row=3, column=3, padx=15, pady=15, sticky=tk.W)

        self.parent.config(cursor="watch")  # startup the busy cursor
        self.cod = crypto()
        self.key = 'pi'   # default key
        self.parent.config(cursor="")  # cursor no longer busy


    def open_text(self):
        # Which file is to be opened ?
        TextFileFormat = [ ('Text File', '*.txt'), ('CSV', '*.csv'),]
        filename = tkFileDialog.askopenfilename(title='Open text file to be encoded:',
                                                defaultextension='.txt', filetypes=TextFileFormat,
                                                parent=self)
        if filename==None:  return  #  user may have cancelled...

        f = open(filename, 'r')
        self.dtext = f.read(-1)
        f.close()
        # In case the text has strange characters, not in st.printable
        for c in self.dtext:
            if c not in st.printable: self.dtext = self.dtext.replace(c,'')
        self.decodedtext.delete(1.0, tk.END)  # delete old text
        self.decodedtext.insert(tk.END, self.dtext)


    def open_codedtext(self):
        # Which file is to be opened ?
        TextFileFormat = [ ('Text File', '*.txt'), ('CSV', '*.csv'),]
        filename = tkFileDialog.askopenfilename(title='Open text file to be decoded:',
                                                defaultextension='.txt', filetypes=TextFileFormat,
                                                parent=self)
        if filename==None:  return  #  user may have cancelled...

        f = open(filename, 'r')
        self.etext = f.read(-1)
        f.close()
        # In case the text has strange characters, not in st.printable
        for c in self.etext:
            if c not in st.printable: self.etext = self.etext.replace(c,'')
        self.encodedtext.delete(1.0, tk.END)  # delete old text
        self.encodedtext.insert(tk.END, self.etext)
        

    def save_text(self):
        TextFileFormat = [ ('Text File', '*.txt'), ('CSV', '*.csv'),]

        # obtain a file name for our new decoded text file
        filename = tkFileDialog.asksaveasfilename(title='Enter file name for decoded text:',
                                                  defaultextension='.txt', filetypes=TextFileFormat,
                                                  parent=self)
        if filename==None:      return  #  user may have cancelled...

        self.dtext = self.decodedtext.get(1.0, tk.END)
        
        f = open(filename,'w')
        f.write(self.dtext[:-1])
        f.close()


    def save_codedtext(self):
        TextFileFormat = [ ('Text File', '*.txt'), ('CSV', '*.csv'),]

        # obtain a file name for our new decoded text file
        filename = tkFileDialog.asksaveasfilename(title='Enter file name for encoded text:',
                                                  defaultextension='.txt', filetypes=TextFileFormat,
                                                  parent=self)
        if filename==None:      return  #  user may have cancelled...

        self.etext = self.encodedtext.get(1.0, tk.END)
        
        f = open(filename,'w')
        f.write(self.etext[:-1])
        f.close()


    def enter_newkey(self):
        self.key = tkSimpleDialog.askstring('Enter Key',
                                            'Enter an irrational number > 1:',
                                            parent=self,
                                            initialvalue=self.key
                                            )  
        self.cod.change_key(self.key)


    def On_EncodeButton(self):
        self.dtext = self.decodedtext.get(1.0, tk.END)
        self.etext = self.cod.encode(self.dtext[:-1])
        # In case the text has strange characters, not in st.printable
        for c in self.etext:
            if c not in st.printable: self.etext = self.etext.replace(c,'')
        self.encodedtext.delete(1.0, tk.END)  # delete old text
        self.encodedtext.insert(tk.END, self.etext)


    def On_DecodeButton(self):
        self.etext = self.encodedtext.get(1.0, tk.END)
        self.dtext = self.cod.decode(self.etext[:-1])
        # In case the text has strange characters, not in st.printable
        for c in self.dtext:
            if c not in st.printable: self.dtext = self.dtext.replace(c,'')
        self.decodedtext.delete(1.0, tk.END)  # delete old text
        self.decodedtext.insert(tk.END, self.dtext)


    def On_ResetButton(self):
        self.encodedtext.delete(1.0, tk.END)
        self.decodedtext.delete(1.0, tk.END)


    def About(self):
        tkMessageBox.showinfo('About',
                              '     Cryptophilia!\n' +
                              'an encryption program  \n' +
                              '             by\n'
                              ' Rafael Espericueta\n'+
                              ' mathprof@bak.rr.com',
                              parent=self.parent)

        
        
        
