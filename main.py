import kivy
kivy.require('1.4.0')
 
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.graphics import *
from kivy.factory import Factory
from kivy.uix.dropdown import DropDown
from PIL import Image, ImageStat
import os
 
class MyApp(App):
          # Function to take a screenshot
          def doscreenshot(self,*largs):
                Logger.info('Progress: Made it to screenshot')
                Window.screenshot(name='top04d.jpg')
          
          def butstep(self):
                self.layout.clear_widgets()
                self.layout.canvas.clear()
                self.initiate_stuff()
                
          def setden(self, text):
                Logger.info('Progress: We are making it here right?')
                if text == 'Styrofoam':
                    Logger.info('Progress: We are making it here right?...or are we')
                    self.den=75
                if text == 'Cork':
                    self.den=240
                if text == 'Wood':
                    self.den=700
                if text == 'Plastic':
                    self.den=1175
                if text == 'Aluminum':
                    self.den=2700
                if text == 'Paper':
                    self.den=800
                if text == 'Leather':
                    self.den=860
                if text == 'Iron':
                    self.den=7870
                if text == 'Copper':
                    self.den=8940
                varlblmass=Label(text="Here is the mass if it is solid: " + str("{:.2f}".format(self.vartupleone[0]*self.vartupleone[1]*self.vartupletwo[0]*self.den*.000016387064) + "kg"), padding_y=120)
                varlblmassh=Label(text="Here is the mass if it is hollow: " + str("{:.2f}".format((self.vartupleone[0]*self.vartupleone[1]*self.vartupletwo[0]*self.den*.000016387064)-((self.vartupleone[0]-.25)*(self.vartupleone[1]-.25)*(self.vartupletwo[0]-.25)*self.den*.000016387064)) + "kg"), padding_y=140)
                self.layout.add_widget(varlblmass)
                self.layout.add_widget(varlblmassh)
                
          def pop_list(self):
                btn = Button(text="Styrofoam", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Cork", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Wood", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Plastic", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Aluminum", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Titanium", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Tin", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Iron", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
                btn = Button(text="Copper", size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn:self.ddown.select(btn.text))
                self.ddown.add_widget(btn)
                
          def initiate_stuff(self):
                Logger.info('Progress: Runnum=' + str(self.runnum))
                  #Create a camera Widget
                self.cam.play=True         #Start the camera
                self.layout.add_widget(self.cam)
                if self.runnum == 0:
                    self.cam.bind(on_touch_down = lambda x,y: self.analyze)
                if self.runnum == 1:
                    self.cam.bind(on_touch_down = lambda x,y: self.analyzetwo)

                with self.cam.canvas:
                    Color(.5,.5,.5,.25)
                    Rectangle(pos=(self.cam.x+self.cam.resolution[0]/10, self.cam.y), size=(self.cam.resolution[0]-self.cam.resolution[0]/5, self.cam.resolution[1]/10))
                    Rectangle(pos=(self.cam.x, self.cam.y), size=(self.cam.resolution[0]/10, self.cam.resolution[1]))
                    Rectangle(pos=(self.cam.x+self.cam.resolution[0]/10, self.cam.resolution[1]-self.cam.resolution[1]/10), size=(self.cam.resolution[0]-self.cam.resolution[0]/5, self.cam.resolution[1]/10))
                    Rectangle(pos=(self.cam.resolution[0]-self.cam.resolution[0]/10, 0), size=(self.cam.resolution[0]/10, self.cam.resolution[1]))
                    Rectangle(pos=(self.cam.resolution[0]/2-self.cam.resolution[0]/20, self.cam.y+self.cam.resolution[1]/10), size=(self.cam.resolution[0]/10, self.cam.resolution[1]-self.cam.resolution[1]/5))
                 
          def simplify(self, data, num):
                Logger.info('Progress: Simplifying')
                datafile = open(num, "w")
                datafile.write("R\n")
                ave=sum(data)/len(data)
                incval=0
                cnt=False
                for i in xrange(0, len(data)):
                    datafile.write(str(data[i])+"\n")
                for j in xrange(0, len(data)):
                    if data[j]<(ave):
                        data[j]=0
                        if cnt==True:
                            incval+=1
                            data[j]=10000
                    if data[j]>(ave):
                        cnt=True
                        data[j]=10000
                    if incval>400:
                        for k in xrange(0,400):
                            data[j-k]=0
                        cnt=False
                        incval=0
                        
                datafile = open("new" + num, "w")
                datafile.write("R\n")
                for l in xrange(0, len(data)):
                    datafile.write(str(data[l])+"\n")
                return data
                
          def show_variance(self, src):
            Logger.info('Progress: Made it to Variance Function')
            im = Image.open(src)
            im_rgb = im.convert("RGB")
            imx, imy = im.size
            iteratx = imx
            iteraty = imy
            dcutoff = 100
            varfactoru = 0
            varfactord = 0
            varfactorroofu = 0
            varfactorroofd = 0
            rdata = []
            finlist = []
            deriv = []
            poper = []
            xboundup = []*20
            xbounddown = []*20
            yboundup = []*20
            ybounddown = []*20
            filebufferx = [0]*iteratx
            filebuffery = [0]*iteraty
            pix = im_rgb.load()
            for z in xrange(1, iteratx):
                rdata[:] = [pix[i, j][0] for j in xrange(0,imy) for i in xrange(z-1,z)]
                mean = sum(rdata)/len(rdata)
                finlist[:] = [(rdata[i]-mean)**2 for i in xrange(len(rdata))]
                varianr = sum(finlist)/len(finlist)
                filebufferx[z-1] = varianr
                rdata[:] = []
            filebufferx = self.simplify(filebufferx, "xfile.txt")
            deriv[:] = [filebufferx[h]-filebufferx[h-1] for h in xrange(1, len(filebufferx))]
            for l in xrange(300, len(deriv) - 500):
                if deriv[l]>dcutoff:
                    xboundup.append(l)
            k = 1
            Logger.info('Data: XboundUp Pre Popper' + str(xboundup))
            while k<len(xboundup):
                if xboundup[k]-xboundup[k-1]<180:
                    poper.append(k)
                k+=1
            inc = 0
            for u in xrange(0, len(poper)):
                xboundup.pop(poper[u]-inc)
                inc+=1
            poper[:] = []
            Logger.info('Debug: XboundUp ' + str(xboundup))
            for m in xrange(300, len(deriv)-500):
                if deriv[m]<-dcutoff:
                    xbounddown.append(m)
            n = 1
            while n<len(xbounddown):
                if xbounddown[n-1]-xbounddown[n]>(-180):
                    poper.append(n)
                n+=1
            inc = 1
            for u in xrange(0, len(poper)):
                xbounddown.pop(poper[u]-inc)
                inc+=1
            Logger.info('Debug: XboundDown ' + str(xbounddown))
            dxcard = xbounddown[-1]-xboundup[-1]
            dxbowl = xbounddown[0]-xboundup[0]
            lengthobj = dxbowl*2.15/dxcard
            objmid = xboundup[-1]-((xboundup[-1]-xbounddown[0])/2)
            poper[:] = []
        
            for d in xrange(1, iteraty):
                rdata[:] = [pix[i, j][0] for j in xrange(d-1,d) for i in xrange(0,objmid)]
                mean = sum(rdata)/len(rdata)
                finlist[:] = [(rdata[i]-mean)**2 for i in xrange(len(rdata))]
                varianr = sum(finlist)/len(finlist)
                filebuffery[d-1] = varianr
                rdata[:] = []
            filebuffery = self.simplify(filebuffery, "yfile.txt")
            deriv[:] = [filebuffery[h]-filebuffery[h-1] for h in xrange(1, len(filebuffery))]
            for l in xrange(300, len(deriv)-300):
                if deriv[l]>dcutoff:
                    yboundup.append(l)
            k = 1
            while k<len(yboundup):
                if yboundup[k]-yboundup[k-1]<150:
                    poper.append(k)
                k+=1
            inc = 0
            for u in xrange(0, len(poper)):
                yboundup.pop(poper[u]-inc)
                inc+=1
            poper[:] = []
            Logger.info('Debug: YboundUp ' + str(yboundup))
            for m in xrange(300, len(deriv)-300):
                if deriv[m]<-dcutoff:
                    ybounddown.append(m)
            g = 1
        
            while g<len(ybounddown):
                if ybounddown[g-1]-ybounddown[g]>(-150):
                    poper.append(g)
                g+=1
            inc = 1
            for u in xrange(0, len(poper)):
                ybounddown.pop(poper[u]-inc)
                inc+=1
            Logger.info('Debug: YboundDown ' + str(ybounddown))
            dybowl = ybounddown[-1]-yboundup[0]
            heightobj = dybowl*2.15/dxcard
            vartuple=(lengthobj, heightobj)
            return vartuple
        
        
          def analyze(self):
                if self.runnum == 0:
                    Logger.info('Progress: Have we made it this far')
                    self.cam.play=False
                    self.doscreenshot()
                    self.vartupleone=self.show_variance("Black Shoe Side.jpg")
                    with self.layout.canvas:
                        Color(.5,.1,.5,1)
                        Rectangle(pos=(0,0), size=(self.cam.resolution[0], self.cam.resolution[1]))
                    varlbl=Label(text="Here are the dimensions" + str("{:.2f}".format(self.vartupleone[0])) + ", " + str("{:.2f}".format(self.vartupleone[1])), padding_y=60)
                    self.layout.add_widget(varlbl)
                    self.runnum = 1
                    Logger.info('Progress: Have we made it this far maybe')
                    os.remove("top04d.jpg")
                    self.cam.unbind(on_touch_down = lambda x,y: self.analyze())
                    self.layout.remove_widget(self.cam)
                    nextbutlayout = AnchorLayout(anchor_x="center", anchor_y="top")
                    nextbut = Button(text="NEXT", size=(100, 80))
                    nextbut.bind(on_press = lambda x: self.butstep())
                    nextbutlayout.add_widget(nextbut)
                    self.layout.add_widget(nextbutlayout)
                
          def analyzetwo(self):
                if self.runnum==1:
                    Logger.info('Progress: Have we made it this far two')
                    self.cam.canvas.clear()
                    self.cam.play=False
                    self.doscreenshot()
                    self.vartupletwo=self.show_variance("Black Shoe Top.jpg")
                    with self.layout.canvas:
                        Color(.5,.1,.5,1)
                        Rectangle(pos=(0,0), size=(self.cam.resolution[0], self.cam.resolution[1]))
                    varlblone=Label(text="Here are the dimensions of the first picture: " + str("{:.2f}".format(self.vartupleone[0])) + "in, " + str("{:.2f}".format(self.vartupleone[1]) + "in"), padding_y=60)
                    varlbltwo=Label(text="Here are the dimensions of the second picture: " + str("{:.2f}".format(self.vartupletwo[0])) + "in, " + str("{:.2f}".format(self.vartupletwo[1]) + "in"), padding_y=80)
                    varlblvol=Label(text="Here is the volume: " + str("{:.2f}".format(self.vartupleone[0]*self.vartupleone[1]*self.vartupletwo[0]) + "in^3"), padding_y=100)
                    ddownbut=Button(text="Density", size_hint=(None, None))
                    ddownbut.bind(on_release=self.ddown.open)
                    #self.ddown.bind(on_select=lambda instance, x:setattr(self.text, 'text', x), self.setden)
                    self.ddown.bind(on_select=lambda instance, x:self.setden(x))
                    self.layout.add_widget(ddownbut)
                    self.layout.add_widget(varlblone)
                    self.layout.add_widget(varlbltwo)
                    self.layout.add_widget(varlblvol)
                    self.runnum=2
                    
                
          def build(self):
                self.den=0
                self.runnum = 0
                self.cam = Camera()        #Get the camera
                self.cam=Camera(resolution=(640, 480), size_hint=(1,1))
                self.ddown=DropDown()
                self.pop_list()
                self.layout = AnchorLayout(anchor_x="center", anchor_y="top")
                self.initiate_stuff()
                return self.layout
          def on_stop(self):
                os.remove("top04d.jpg")
             
if __name__ == '__main__':
    MyApp().run()            