# David Martinez
#
# October 2021


from OpenGL import GL
from OpenGL.GL.ARB import invalidate_subdata
import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLU import *
from sympy.printing.latex import translate

from tabulate import tabulate
from sympy import *

trK = -3
componentsEnabled = True

winM = 10

def main():
        
    print("")
    l = [["Vector Visualization", "3D drawing of Vector", 1], ["Vector +/-", "Add or Subtract Vectors", 2], ["Vector Function Over Time", "x(t), v(t), a(t)", 3]]
    table = tabulate(l, headers=['Function/Operation',
                    'Description', 'Code'], tablefmt='fancy_grid')

    print(table)
    # bool
    
    # init functions

    def formatVector(strV):
        vL = []
        strV.replace("(", "")
        strV.replace(")", "")
        strV.replace(" ", "")
        vL = strV.split(",")

        for x in range(0, len(vL)):
            vL[x] = int(vL[x])
        if len(vL) < 3:
            vL.append(0)
        # print(vL)
        return vL

    # def line(vecList):


    def rendVector(vL):
        glLineWidth(1.7)
        glColor3f(0.8, 0.8, 0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        i = vL[0] / 10
        j = vL[1] / 10
        k = vL[2] / 10
        glVertex3f(i, j, k)
        glEnd()

        if(componentsEnabled):
            glLineWidth(0.9)
            glBegin(GL_LINES)
            glColor3f(0.8, 0, 0)
            glVertex3f(0, j, 0)
            glVertex3f(i, j, 0)
            glEnd()
            glBegin(GL_LINES)
            glColor3f(0, 0, 0.8)
            glVertex3f(i, 0, 0)
            glVertex3f(i, j, 0)
            glEnd()
            glBegin(GL_LINES)
            glColor3f(0, 0.8, 0)
            glVertex3f(i, j, 0)
            glVertex3f(i, j, k)
            glEnd()


    #
    pointDir = []


    def rendVector2(vL):
        glPointSize(4)
        glColor3f(0.8, 0.8, 0)
        glBegin(GL_POINTS)
        i = vL[0] / 10
        j = vL[1] / 10
        k = vL[2] / 10
        glVertex3f(i, j, k)
        #print("coord form: "  + str(i) + str(j), str(k))
        tempTup = [i, j, k]
        pointDir.append(tempTup)
        glEnd()

        glBegin(GL_POINTS)
        for x in pointDir:
            i2 = x[0]
            j2 = x[1]
            k2 = x[2]
            glVertex3f(i2, j2, k2)
        glEnd()
        global partialD
        global timeInst
        di = str(partialD[0])
        dj = str(partialD[1])
        dk = str(partialD[2])
        di = di.replace("t", str(timeInst))
        dj = dj.replace("t", str(timeInst))
        dk = dk.replace("t", str(timeInst))
        di = eval(di) / (winM+1)
        dj = eval(dj) / (winM+1)
        dk = eval(dk) / (winM+1)

       # print(di)
       # print(dj)
       # print(dk)
        glLineWidth(0.9)

        glBegin(GL_LINES)
        glColor3f(0.8, 0, 0)
        glVertex3f(i, j, k)
        glVertex3f(i + di, j, k)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0, 0, 0.8)
        glVertex3f(i, j, k)
        glVertex3f(i, j + dj, k)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0, 0.8, 0)
        glVertex3f(i, j, k)
        glVertex3f(i, j, k + dk)
        glEnd()
        if(componentsEnabled):
            glLineWidth(0.9)
            # x
            glBegin(GL_LINES)
            glColor3f(0.8, 0, 0)
            glVertex3f(0, j, 0)
            glVertex3f(i, j, 0)
            glEnd()
            # y
            glBegin(GL_LINES)
            glColor3f(0, 0, 0.8)
            glVertex3f(i, 0, 0)
            glVertex3f(i, j, 0)
            glEnd()
            # z
            glBegin(GL_LINES)
            glColor3f(0, 0.8, 0)
            glVertex3f(i, j, 0)
            glVertex3f(i, j, k)
            glEnd()
    #


    def main(vecL):
        pygame.init()
        display = (1000, 900)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(1.2)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslate(0, 0, -4)
        # glRotate(-45,0,0,0)
        glRotate(-90, 1, 0, 0)
        glRotate(-110, 0, 0, 1)
        glRotate(10, -1, 1, 0)
        glRotate(10, 0, 1, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if(keys[K_RIGHT]):
                glRotate(0.5, 0, 0, 1)
            elif (keys[K_LEFT]):
                glRotate(-0.5, 0, 0, 1)

            #glRotatef(0, 0, 0, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glBegin(GL_LINES)
            glColor(1, 0, 0)
            glVertex3f(0, 0, 0)
            glVertex3f(1, 0, 0)
            glEnd()
            glBegin(GL_LINES)
            glColor3f(0, 0, 1)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 1, 0)
            glEnd()
            glBegin(GL_LINES)
            glColor3f(0, 1, 0)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 0, 1)
            glEnd()
            rendVector(vecL)
            glClearColor(0.1, 0.1, 0.1, 1)
            pygame.display.flip()
            pygame.time.wait(2)
    
    
    def main2(vecL, final):
        global trK
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if(keys[K_RIGHT]):
            glRotate(0.8, 0, 0, 1)
        elif (keys[K_LEFT]):
            glRotate(-0.8, 0, 0, 1)
    

        #glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_LINES)
        glColor(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 0, 0)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 1, 0)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 1)
        glEnd()
        rendVector2(vecL)
        glClearColor(0.1, 0.1, 0.1, 1)
        pygame.display.flip()
        pygame.time.wait(2)
        if (final == True):
            # print("directory")
            # print(pointDir)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                keys = pygame.key.get_pressed()
                if(keys[K_RIGHT]):
                    glRotate(0.5, 0, 0, 1)
                elif (keys[K_LEFT]):
                    glRotate(-0.5, 0, 0, 1)

                #glRotatef(0, 0, 0, 0)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glBegin(GL_LINES)
                glColor(1, 0, 0)
                glVertex3f(0, 0, 0)
                glVertex3f(1, 0, 0)
                glEnd()
                glBegin(GL_LINES)
                glColor3f(0, 0, 1)
                glVertex3f(0, 0, 0)
                glVertex3f(0, 1, 0)
                glEnd()
                glBegin(GL_LINES)
                glColor3f(0, 1, 0)
                glVertex3f(0, 0, 0)
                glVertex3f(0, 0, 1)
                glEnd()
                global componentsEnabled
                componentsEnabled = True
                rendVector2(vecL)
                glClearColor(0.1, 0.1, 0.1, 1)
                pygame.display.flip()
                pygame.time.wait(10)
    # end main 2 function


    def formatFunction(strF):
        l = strF
        l = l.replace(' ', '')
        l = l.replace("^", "**")
        i = l.split(',')

        newL = []

        for x in i:
            eval1 = ''
            y = 0
            a = len(x)
            x += '  '
            while (y < a):
                #print(eval1)
                #print(a)
                # print(x[y])
                if(x[y].isnumeric() & (x[y+1] == "t")):
                    if (x[y-1] == "-"):
                        eval1 += "-" + x[y] + '*'
                        tempChar1 = x[y+1]
                        while((tempChar1 != "+") | (tempChar1 != "-") | (tempChar1 != " ")):
                            if(y < a):
                                tempChar1 = x[y+1]
                                eval1 += tempChar1
                                y += 1
                            else:
                                break
                            #

                    else:

                        if(x[y-1] == "+"):
                            eval1 += "+"
                        tempChar1 = x[y+1]
                        eval1 += x[y] + '*'
                        while((tempChar1 != "+") | (tempChar1 != "-")):
                            if(y < a):
                                tempChar1 = x[y+1]
                                eval1 += tempChar1
                                y += 1
                            else:
                                break
                elif(x[y].isnumeric() & x[y+1].isnumeric() & (x[y+2] == "t")):
                    eval1 +=  x[y:y+1] + '*'
                    tempChar1 = x[y+1]       
                    while((tempChar1 != "+") | (tempChar1 != "-") |  (tempChar1 != " ") ):
                        if(y<a):
                            tempChar1 = x[y+1]
                            eval1 += tempChar1
                            y += 1
                        else:
                            break
                    #
                elif(x[y].isalpha() & x[y+1].isalpha() & (y < (a-2))):
                    #i = y
                    tempChar = x[y]
                    while(tempChar != ")"):
                        tempChar = x[y]
                        eval1 += tempChar
                        y += 1
                else:
                    y += 1

            newL.append(eval1)

        finalL = []
        for el in newL:
            for index in range(0, len(el)-1):
                if((el[index].isnumeric()) & (el[index+1] == "t")):
                    el = el[0:index+1] + "*" + el[index+1:]
        

            finalL.append(el)

        print(finalL)
        return newL


    def drawVector(vecL):
        # print(vecL)
        l1 = [["Red", "X / i"], ["Blue", "Y / j"], ["Green", "Z / k"]]
        table2 = tabulate(l1, headers=['Color', 'Axis'], tablefmt='fancy_grid')

        print(table2)
        print("Loading window ...")
        magSum = 0
        for i in vecL:
            magSum += i * i
        mag = magSum ** (0.5)
        l2 = [["Yellow", mag]]
        table2 = tabulate(
            l2, headers=['Vector', 'Magnitude'], tablefmt='fancy_grid')

        print(table2)
        main(vecL)


    partialD = []
    timeInst = 0
    # Animate path over time


    def vectorFx():
        global componentsEnabled
        componentsEnabled = False
        l3 = [["x(t)", "3t^2, 5t + 1, 4t"],
            ["v(t)", "5t^2, 6t, 4"], ["a(t)", "5t, 2t, 3"]]
        table3 = tabulate(
            l3, headers=['Type', 'Example Input'], tablefmt='fancy_grid')
        funcType = input(
            "Is your function for position, velocity, or acceleration?  Please enter  x , v, or a  to indicate: ")
        print(table3)
        func = input("What is your function in repect to time? ")
        fL = formatFunction(func)
        print(fL)
        initX = input("Initial Point or Value?  ex.  (4,3,5)  ")
        iX = formatVector(initX)
        #print(componentsEnabled)
        minT = input("Start Time (seconds): ")
        maxT = input("End Time (seconds: ")
        # derivative   1st
        global partialD
        partialD = []
        for z in fL:
            print("partial derivative of " + z + "is: ")
            print(diff(z, 't'))
            partialD.append(diff(z, 't'))

        pygame.init()
        display = (1000, 900)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(1.2)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslate(0,0, -4)
        # glRotate(-45,0,0,0)
        glRotate(-90, 1, 0, 0)
        glRotate(-110, 0, 0, 1)
        glRotate(10, -1, 1, 0)
        glRotate(10, 0, 1, 0)
        t = int(minT)
    # print(t)

        testBounds = []
        for x in fL:
            x = x.replace('t', maxT)
            x = eval(x)
            vI2 = float(x)
            # print(vI2)
            testBounds.append(vI2)
        testBounds[0] += float(iX[0])
        testBounds[1] += float(iX[1])
        testBounds[2] += float(iX[2])

        testBounds.sort()
        # print(testBounds)
        winMax = testBounds[2] * 0.12
        global winM
        winM = winMax

        while(t <= float(maxT)):
            insVector = []
            for y in fL:
                t2 = str(t)
                y = y.replace('t', t2)
                y = eval(y)
                vI = float(y)/winMax
                insVector.append(vI)


            # ALPHA k
            t += 0.08





            insVector[0] += (iX[0]/winMax)
            insVector[1] += (iX[1]/winMax)
            insVector[2] += (iX[2]/winMax)

            global timeInst
            timeInst = t
            # print(insVector)

            #diffComp(insVector, partialD, t, winMax)
            main2(insVector, False)

        main2(insVector, True)
    # diffComp(insVector, partialD, t, winMax)

    #


    def sumVector():
        print("2")


    def initPrompt():
        userIn = input("Please Enter the Operation Code (1,2,3,4..):  ")
        if (userIn == "1"):
            vec = input("Enter your vector in cartesian coordinates ex. (2,1,4):  ")
            vL = formatVector(vec)
            drawVector(vL)
        elif (userIn == "2"):
            sumVector()
        elif (userIn == "3"):
            vectorFx()
        else:
            print("Sorry, that is not a numerical code that is available")
            initPrompt()
    #


    # initPrompt
    initPrompt()


if __name__ == '__main__':
    main()
