
import tkinter as tk

def list_to_str(list):
    output=''
    for key in list:
        output=output+str(key)
    return output

def binstr_to_int(input):
    remainder=0
    times_1=0
    counter=[]
    times=0
    before=str(input)
    while times_1<len(before):
        counter.append(before[times_1])
        times_1+=1
    for key in counter:
        if key=='1' or key=='0':
            pass
        else:
            raise TypeError('\''+str(input)+'\' is not a binary number')
    counter.reverse()
    counter_out=list_to_str(counter)
    while times<len(before):
        number=counter_out[times]
        power=2**times*int(number)
        remainder=power+remainder
        times+=1
    return remainder

def encrypt(in_put):
    times=0
    encrypt_list=[]
    while times<(len(in_put)):
        times=times+1
        encrypt=str(bin(ord(in_put[times-1])).replace('0b','').zfill(16))
        encrypt_list.append(encrypt+' ')
    encrypt_str=list_to_str(encrypt_list)
    encrypted='['+(encrypt_str.replace('1','\u200b').replace('0','\u200c').replace('\\','\u200d'))+']'
    return encrypted

def unencrypt(in_put):
    
    unencrypt_list=[]
    unencrypted_before=[]
    unencrypted=[]
    times=0
    counter=0
    putin=str(in_put).replace('[','').replace(']','')
    unencrypt=putin.replace('\u200b','1').replace('\u200c','0').replace('\u200d','')
    while times<len(unencrypt)/16:
        unencrypt_list.append(unencrypt[counter:counter+16])
        times+=1
        counter+=16
    for key in unencrypt_list:
        unencrypted_before.append(binstr_to_int(key))
    for key in unencrypted_before:
        unencrypted.append(chr(int(key)))
    output=list_to_str(unencrypted)
    return output

def Button1_press():
    Text2.delete('1.0','end')
    Text2.insert('0.0',encrypt(Text1.get('0.0','end')).replace(' ',''))
def Button2_press():
    Text1.delete('1.0','end')
    Text1.insert('0.0',unencrypt(str(Text2.get('0.0','end')).replace('\n','')).replace('\\n',''))
Main=tk.Tk()

Text1=tk.Text(exportselection=0,font=150)
Text1.place(x=8,y=8,height=41,width=320)

Button1=tk.Button(text='加密 encrypt',command=Button1_press)
Button1.place(x=8,y=57,height=42,width=154)

Button2=tk.Button(text='解密 unencrypt',command=Button2_press)
Button2.place(x=170,y=57,height=42,width=154)

Text2=tk.Text(exportselection=0,font=150)
Text2.place(x=8,y=107,height=41,width=320)

Main.title('encryption')
Main.geometry("334x156")
Main.resizable(False,False)
Main.mainloop()