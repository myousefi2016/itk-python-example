'''
 Author: QIN Shuo
 Date:   2015/11/10
 This is a example file for vtk
 Description:
   This file demostrate how to get the position of a 
   picked point.


 Tips:

1. In class
 class MyStyle(vtk.vtkInteractorStyleImage):
    def __init__(self):
        pass
    def OnMouseWheelForward(self):
        pass

 the above method will not re-load the mouse wheel function
 the real functional method are applied by adding event observer
 Solution:
 Register this event: self.AddObserver(...)

2. AddObserver, Observer function conflict
Solution: call RemoveObservers() first to unregister all event functions
'''


import vtk


drawing = vtk.vtkImageCanvasSource2D()
drawing.SetScalarTypeToUnsignedChar()
drawing.SetNumberOfScalarComponents(3)
drawing.SetExtent(0,20,0,50,0,0)
drawing.FillBox(0,20,0,50)


drawing.SetDrawColor(255,0,0,0)
drawing.DrawCircle(9,10,5)
drawing.Update()

actor = vtk.vtkImageActor()
actor.GetMapper().SetInputData(drawing.GetOutput())
actor.InterpolateOff()

renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)

renderWinInteractor = vtk.vtkRenderWindowInteractor()
renderWinInteractor.SetRenderWindow(renderWin)

renderer.AddActor(actor)
renderer.SetBackground(1,1,1)

renderer.GradientBackgroundOn()
renderer.SetBackground2(0,0,1)

renderWin.Render()

def LeftButtonPressEvent(obj,event):
    global renderWinInteractor
    global renderer
    picker = renderWinInteractor.GetPicker()
    print "indexs on window view is ", renderWinInteractor.GetEventPosition()
    picked = renderWinInteractor.GetPicker().GetSelectionPoint()
    print "coordinate on 2d plane view is", picked
    picker.Pick(renderWinInteractor.GetEventPosition()[0],renderWinInteractor.GetEventPosition()[1],0,renderer)
    picked = renderWinInteractor.GetPicker().GetPickPosition()
    print "3d position is ",picked


renderWinInteractor.RemoveObservers(vtk.vtkCommand.LeftButtonPressEvent)  # this line to solve event conflict
renderWinInteractor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent,LeftButtonPressEvent)
renderWinInteractor.Initialize()

vtk.vtkCommand.TDxButtonPressEvent

renderWinInteractor.Start()


