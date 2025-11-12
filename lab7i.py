#!/usr/bin/env python3
# Student ID: asmodi2
def function1():
    # make the change GLOBAL so main sees SICT after this call
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    # also global so main sees SSDO after this call
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
