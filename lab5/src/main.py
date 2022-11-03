import random

from panda3d.core import loadPrcFile
from panda3d.core import *
loadPrcFile("config/config.prc")
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import os, sys
import math

class MyGame(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Get the location of the 'py' file I'm running:
        self.mydir = os.path.abspath(sys.path[0])
        # convert to panda's specific notation
        self.mydir = Filename.fromOsSpecific(self.mydir).getFullpath()

        # load skull obj
        self.skullModel = self.loader.loadModel(self.mydir + "/skull.obj")
        self.skullModel.setPos(5, 0, -5)
        self.skullModel.reparentTo(self.render)

        # move camera
        self.disableMouse()
        self.camera.setPos(0, -30, 0)

        # scale down the skull
        self.skullModel.setScale(0.35, 0.35, 0.35)

        # add task to be executed
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # add ambient light
        self.alight = AmbientLight("alight")
        self.alight.setColor((0.8, 0.8, 0.8, 1))
        self.alnp = self.render.attachNewNode(self.alight)
        self.render.setLight(self.alnp)

        # load panda obj
        self.pandaModel = self.loader.loadModel("models/panda")
        self.pandaModel.setPos(0.0, 0.0, 30.0)
        self.pandaModel.setP(90)
        self.pandaModel.setScale(.6, .6, .6)
        self.pandaModel.reparentTo(self.skullModel)
        self.pandaOrientation = 0

        # addd task to rotate panda
        self.taskMgr.add(self.spinPandaTask, "SpinPandaTask")

        # add taskt o cahnge radius
        self.taskMgr.add(self.moveTask, "MoveTask")


    def spinCameraTask(self, task):
        self.cameraRadius = 30.0
        angleDegrees = task.time * 20.0
        angleRadians = angleDegrees * (math.pi / 180)

        self.camera.setPos(
            self.cameraRadius * math.sin(angleRadians),
            -self.cameraRadius * math.cos(angleRadians), 
            0)

        self.camera.lookAt(0.0, 0.0, 0.0)
        
        return Task.cont


    def spinPandaTask(self, task):
        self.pandaRadius = 10.0
        angleDegrees = task.time * 90.0
        angleRadians = angleDegrees * (math.pi / 180)

        self.pandaModel.setPos(
            self.pandaRadius * math.sin(angleRadians),
            self.pandaRadius * math.cos(angleRadians),
            30.0
        )
        
        self.pandaOrientation = angleDegrees - 45
        self.pandaModel.setH(-self.pandaOrientation)

        return Task.cont


    def moveTask(self, task):
        isDown = base.mouseWatcherNode.isButtonDown

        if isDown(KeyboardButton.asciiKey("+")):
            self.cameraRadius += 1

        if isDown(KeyboardButton.asciiKey("-")):
            self.cameraRadius -= 1

        return task.cont


# create an object for the game and run it
if __name__ == "__main__":
    game = MyGame()
    game.run()