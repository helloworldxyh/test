import tkinter as tk
import pickle
import MySQLdb
from tkinter import messagebox

#1.初始化window界面

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('1000x600')
window.mainloop()

#2.插入logo用画布实现
#welcome image
#创建一个600X1000的画布
canvas =  tk.Canvas(window,height = 334,width = 500)
#logo的路径
image_file = tk.PhotoImage(file = 'F:\Lofter\PictureProject\traffic01.gif')
#什么位置插入logo图片
image = canvas.create_image(0,0,anchor = 'nw',image = image_file)
canvas.pack(side = 'top')

#3.登录界面代码实现
tk.Label(window,text = 'Username:').place(x = 50,y = 150)
tk.Label(window,text = 'Password:').place(x = 50,y = 190)

var_usr_name = tk.StringVar()
#默认值为MrZhangxd@python.com
var_usr_name.set('MrZhangxd@python.com')
var_usr_pwd = tk.StringVar()
entry_usr_name = tk.Entry(window,textvariable = var_usr_name)
entry_usr_name.place(x = 160,y = 150)

entry_usr_pwd = tk.Entry(window,textvariable = var_usr_pwd,show ='*')
entry_usr_pwd.place(x = 160,y = 190)

#4.登录和注册按钮的实现代码
#Login and Sign up button
# command = usr_login 调用usr_login函数
btn_login = tk.Button(window,text = 'Login',command = usr_login)
btn_login.place(x = 170,y = 230)
btn_sign_up = tk.Button(window,text = 'Sign up',command = usr_sign_up)
btn_sign_up.place(x = 270,y = 230)

#4.登录判断代码
# 声明usr_login函数
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info,pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you?' + usr_name)
        else:
            tk.messagebox.showinfo(message='Error,your password is wrong,try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'You hava not sign up yet.Sign up today?')

        if is_sign_up:
            usr_sign_up()

#6.注册代码
def usr_sign_up():
    def sign_to_Mofan_Python():

        np = new_pwd.get()

        npf = new_pwd_confirm.get()

        nn = new_name.get()
        with open('usrs_info', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('MrZhangxd@python.com')
    tk.Label(window_sign_up, text='Username:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password:').place(x=10, y=90)
    entry_comfirm_sign_up = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_comfirm_sign_up.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

