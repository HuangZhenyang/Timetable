# -*- coding:utf-8 -*-
#--------Import------------
import sys
from selenium import webdriver
from Tkinter import*
import tkMessageBox
from random import choice
#--------END Import-------

def getTimetable():
    timetable = str(entryFile.get())
    if timetable == '':
    	timetable = "timetable.png"
    userID = str(entryID.get())
    pswd = str(entryPSWD.get())
    #--------Login------------
    # driver = webdriver.Chrome()
    #driver = webdriver.Ie()
    #driver = webdriver.Firefox()
    driver = webdriver.PhantomJS('phantomjs/bin/phantomjs.exe')
    driver.get('http://zhjw.scu.edu.cn/login.jsp')

    user_id = driver.find_element_by_name('zjh')
    user_id.clear
    user_id.send_keys(userID)

    password = driver.find_element_by_name('mm')
    password.clear
    password.send_keys(pswd)


    driver.find_element_by_id('btnSure').click()
    #-------END Login---------
    driver.implicitly_wait(10)

    #-------Switch Frame---------
    driver.implicitly_wait(10)
    driver.switch_to.frame('bottomFrame')
    driver.implicitly_wait(10)
    driver.switch_to.frame('mainFrame')
    #------END Switch Frame------

    #-------Get Timetable--------
    kebiao = driver.find_element_by_xpath('//*[@id="divCoHome"]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td/a')
    print kebiao.is_enabled()
    kebiao.click()

    driver.execute_script("""
            (function () {
                var y = 0;
                var step = 100;
                window.scroll(0, 0);

                function f() {
                    if (y < document.body.scrollHeight) {
                        y += step;
                        window.scroll(0, y);
                        setTimeout(f, 50);
                    } else {
                        window.scroll(0, 0);
                        document.title += "scroll-done";
                    }
                }

                setTimeout(f, 1000);
            })();
        """)

    driver.save_screenshot(timetable)
    #-------END Get Timetable-----
    entryFile.delete(0, END)
    entryID.delete(0, END)
    entryPSWD.delete(0, END)
    tkMessageBox.showinfo('Done')
    

def func_entry():
    if entryID.get() == '' or entryPSWD.get() == '':
        entryFile.delete(0, END)
        entryID.delete(0, END)
        entryPSWD.delete(0, END)
        tkMessageBox.showinfo('Please input your id or password')
    else:
        getTimetable()


def quitThisProgram():
    sys.exit()

root = Tk()
root.title('Get Timetable')

labelFile = Label(root, text='path to store timetable(no need) eg.C://timetable.png:')
labelFile.grid(row=0, column=0)
entryFile = Entry(root, font=('微软雅黑,12'))
entryFile.grid(row=0, column=1)
labelID = Label(root, text='StudentId:')
labelID.grid(row=1, column=0)
entryID = Entry(root, font=('宋体,16'))
entryID.grid(row=1, column=1)
labelID = Label(root, text='Password:')
labelID.grid(row=2, column=0)
entryPSWD = Entry(root, font=('宋体,16'))
entryPSWD.grid(row=2, column=1)
masks = ['*', '@', '#', '%']
mask = choice(masks)
entryPSWD['show'] = mask

buttonLogin = Button(root, text='Login', font=('宋体,13'), command=func_entry)
buttonLogin.grid(row=3, column=0)
buttonQuit = Button(root, text='Exit', font=('微软雅黑,13'), command=quitThisProgram)
buttonQuit.grid(row=3, column=1)

root.mainloop()
