#Arch 441//Medium//Fall 2021//Ericson
#
#Jose Fernandez
#10.25.21
#
#Nakagin Capsule Towers
#This project creates a set of objects that are generated through the rule set of the Nakagin Capsule Tower
#
#Source:  
#Source:
    
#source:
#
#*****************************************************************************
#imported Libraries
#

import rhinoscriptsyntax as  rs
import random
import math
import scriptcontext as sc

def LinearColor (R,G,B,R2,G2,B2,scalar):
    
    Rdiff = R2 - R
    Gdiff = G2 - G
    Bdiff = B2 - B
    
    R3 = float(R + Rdiff*scalar) % 255
    G3 = float(G + Gdiff*scalar) % 255
    B3 = float(B + Bdiff*scalar) % 255
    
    return(R3,G3,B3)
    
def center_cube(Center,Radius):
    #Function to create cube centered on a point. 
    boxes = []
    for i in Center:
        #get the x,y,z values from the inputed tuple "center"
        Cx = i[0]
        Cy = i[1]
        Cz = i[2]

        
        #lower 4 points
        p1 = (Cx-Radius,Cy-Radius,Cz-Radius)
        p2 = (Cx+Radius,Cy-Radius,Cz-Radius)
        p3 = (Cx+Radius,Cy+Radius,Cz-Radius)
        p4 = (Cx-Radius,Cy+Radius,Cz-Radius)
        
        #upper 4 points
        p5 = (Cx-Radius,Cy-Radius,Cz+Radius)
        p6 = (Cx+Radius,Cy-Radius,Cz+Radius)
        p7 = (Cx+Radius,Cy+Radius,Cz+Radius)
        p8 = (Cx-Radius,Cy+Radius,Cz+Radius)
        
        #make a box
        Box = rs.AddBox([p1,p2,p3,p4,p5,p6,p7,p8])
        boxes.append(Box)
    #return the box
    return(boxes)


def city_grid(pts, size):
    
    
    x_dim = int(rs.Distance(pts[0], pts[1]))
    y_dim = int(rs.Distance(pts[1], pts[2]))
    print (x_dim)
    print (y_dim)
    points = []
    for i in range(0,x_dim,size):
        for j in range(0,y_dim,size):
            #for p in range(0,z_dim,size):
                x = i
                y = j
                z = 0
                
                dPoints = RandomPoints(5, x_dim, y_dim)
                distance = rs.Distance(dPoints[1],(x,y,z))
                distance_2 = rs.Distance(dPoints[2],(x,y,z))
                distance_3 = rs.Distance(dPoints[3],(x,y,z))
                distance_4 = rs.Distance(dPoints[4],(x,y,z))
                distance_5 = rs.Distance(dPoints[0],(x,y,z))
            
                x = x + pts[0].X
                y = y + pts[0].Y

                if distance > 300 and distance_2 >  0 and distance_3 > 20 and distance_4 > 50 and distance_5 > 50:
                #if distance > dist and distance_2 >  dist and distance_3 > dist and distance_4 > dist and distance_5 > dist:
                    rs.AddPoint(x,y,z)
                    rs.EnableRedraw(False)
                    points.append((x,y,z))
                    print ("found Point")
    return(points)
    


def savecity_grid(x_dim, y_dim, z_dim, size):
    
    #print (x_dim)
    #print (y_dim)
    #print (size)
    
    points = []
    for i in range(0,x_dim,size):
        for j in range(0,y_dim,size):
            #for p in range(0,z_dim,size):
                x = i
                y = j
                z = 0
                
                dPoints = RandomPoints(5, x_dim, y_dim)
                distance = rs.Distance(dPoints[1],(x,y,z))
                distance_2 = rs.Distance(dPoints[2],(x,y,z))
                distance_3 = rs.Distance(dPoints[3],(x,y,z))
                distance_4 = rs.Distance(dPoints[4],(x,y,z))
                distance_5 = rs.Distance(dPoints[0],(x,y,z))
            
            
                if distance > 900 and distance_2 >  900 and distance_3 > 300 and distance_4 > 100 and distance_5 > 300:
                    rs.AddPoint(x,y,z)
                    rs.EnableRedraw(False)
                    points.append((x,y,z))
    return(points)
    
def RandomPoints(Number,MaxX,MaxY):
    Plist = []
    Count = 0
    while Count < Number:
        Count += 1
        
        x = random.randint(0,MaxX)
        y = random.randint(1,MaxY)
        z = random.randint(1,SideLength)
        
        point = rs.CreatePoint(x,y,0)
        Plist.append(point)
        
    return(Plist)

def RandomPoint():
    r = random.uniform(0,360)
    y =math.sin(math.radians(r))*SideLength
    x = math.cos(math.radians(r))*SideLength2
    z = random.uniform(0,20)
    point = rs.AddPoint(x,y,0)
    return(point)


def square(SideLength, Corner):
    
    sL = SideLength
    sL2 = SideLength2
    
    point1 = rs.AddPoint(0,0,0)
    point2 = rs.AddPoint(sL,0,0)
    point3 = rs.AddPoint(sL,sL2,0)
    point4 = rs.AddPoint(0,sL2,0)
    
    Side = rs.AddPolyline([point1,point2,point3,point4,point1])
    return(Side)

def capsule(coreH, capH, sL, cList):
    sLL = sL/2
    Corner = rs.CreatePoint(cList[0])
    cap = box(sL, sLL, capH, Corner.X, Corner.Y, 0)
    
    #LinearColor(255,255,255,12,59,101,cap)
    #Color = rs.CreateColor(cv[0],cv[1],cv[2])
    
    Color = rs.CreateColor(10,74,77)
    rs.AddMaterialToObject(cap)
    Index = rs.ObjectMaterialIndex(cap)
    rs.MaterialColor(Index,Color)
    midpoint = rs.CreatePoint(Corner.X + sL, Corner.Y + sLL, Corner.Z)
    cap2 = rs.RotateObject(cap, midpoint, 90.0, None, copy=True)
    
    midpoint2  =rs.CreatePoint(midpoint.X, midpoint.Y + sLL, Corner.Z)
    midPointCore = rs.CreatePoint(midpoint.X + sLL, midpoint.Y + sLL, Corner.Z)
    cItems  = []
    cItems.append(cap)
    cItems.append(cap2)
    
    for i in range(4):
        cap3 = rs.RotateObject(cap, midpoint2, 90.0*i, None, copy=True)
        cap4 = rs.RotateObject(cap2, midpoint2, 90.0*i, None, copy=True)
        cItems.append(cap3)
        cItems.append(cap4)

    scaleVec = rs.CreatePoint(1.5,1.5,1.15)
    #scaleVec = rs.CreatePoint(xScale,yScale,zScale)
    nscaleVec = rs.CreatePoint(0.65,0.65,.6)
    
    endPoint = rs.CreatePoint(midpoint2.X+20, midpoint2.Y, midpoint2.Z)
    newCaps = rs.MirrorObjects(cItems, midpoint2, endPoint,copy=True)
    groupCaps = rs.BooleanUnion(newCaps, delete_input=False)
    groupItems = rs.BooleanUnion(cItems, delete_input=False)
    shiftvec = rs.CreatePoint(1,2,capH)
    shiftItems = rs.CopyObjects(groupItems)
    
    boolTest = rs.BooleanUnion((groupCaps, groupItems), delete_input=False)
    
    Color = rs.CreateColor(10,74,77)
    rs.AddMaterialToObject(shiftItems)
    Index = rs.ObjectMaterialIndex(shiftItems)
    rs.MaterialColor(Index,Color)
    
    shiftCaps = rs.CopyObject(groupCaps, shiftvec)
    
    Color = rs.CreateColor(10,74,77)
    rs.AddMaterialToObject(shiftCaps)
    Index = rs.ObjectMaterialIndex(shiftCaps)
    rs.MaterialColor(Index,Color)
    

    i = 2
    j = coreH/capH

    #scaleVec = rs.CreatePoint(1.45,1.5,1.40)
    capH = (capH * 1)
    capZ = capH * 2
    capO = capH

    startColorR = 10
    startColorG = 74
    startColorB = 77
    
    endColorR = 255
    endColorG = 255
    endColorB = 255

    while (i < (j)):
        dColor = LinearColor (startColorR, startColorG, startColorB, endColorR, endColorG, endColorB, i*.025)
        shiftvec = rs.CreatePoint(0,0,capH+capO)
        midPointCore = rs.CreatePoint(midpoint.X + sLL, midpoint.Y + sLL, capZ)

        if ((i%2) == 0):
           shiftItems = rs.CopyObject(shiftItems, shiftvec)
           rs.ScaleObject(shiftItems, midPointCore, scaleVec, copy=False)
           Color = rs.CreateColor(dColor[0],dColor[1],dColor[2])
           rs.AddMaterialToObject(shiftItems)
           Index = rs.ObjectMaterialIndex(shiftItems)
           rs.MaterialColor(Index,Color)
           capO = capH
           capH = capH * 1.1
        else:
            shiftCaps = rs.CopyObject(shiftCaps, shiftvec)
            rs.ScaleObject(shiftCaps, midPointCore, scaleVec, copy=False)
            Color = rs.CreateColor(dColor[0],dColor[1],dColor[2])
            rs.AddMaterialToObject(shiftCaps)
            Index = rs.ObjectMaterialIndex(shiftCaps)
            rs.MaterialColor(Index,Color)
            capO = capO * 1.1
        capZ = capZ + capH
        i = i + 1
    i = 2
    
    zscale = .6
    nscaleVec = rs.CreatePoint(0.7,0.7,zscale)
    while (i < (j)):
        dColor = LinearColor (startColorR, startColorG, startColorB, endColorR, endColorG, endColorB, i*.025)
        shiftvec = rs.CreatePoint(0,0,capH+capO)
        midPointCore = rs.CreatePoint(midpoint.X + sLL, midpoint.Y + sLL, capZ)
        print(i)
        if ((i%2) == 0):
           shiftItems = rs.CopyObjects(shiftItems, shiftvec)
           rs.ScaleObject(shiftItems, midPointCore, nscaleVec, copy=False)
           Color = rs.CreateColor(dColor[0],dColor[1],dColor[2])
           rs.AddMaterialToObject(shiftItems)
           Index = rs.ObjectMaterialIndex(shiftItems)
           rs.MaterialColor(Index,Color)
           capO = capH
           capH = capH * zscale
        else:
           shiftCaps = rs.CopyObject(shiftCaps, shiftvec)
           rs.ScaleObject(shiftCaps, midPointCore, nscaleVec, copy=False)
           Color = rs.CreateColor(dColor[0],dColor[1],dColor[2])
           rs.AddMaterialToObject(shiftCaps)
           Index = rs.ObjectMaterialIndex(shiftCaps)
           rs.MaterialColor(Index,Color)
           capO = capO * zscale
        capZ = capZ + capH
        i = i + 1
def core (coreH, capH, SideLength, Corners):
    
    for i in range(len(Corners)):
      #rs.Sleep(10000)
      #sc.escape_test()
      #i = 1
      Corner = rs.CreatePoint(Corners[i])
      #Corner = rs.CreatePoint(0,0,0)
      sL = SideLength
      cList = []
      
      mycore=box(SideLength, SideLength, coreH, Corner.X, Corner.Y, Corner.Z)
      
      
      Color = rs.CreateColor(255,255,255)
      rs.AddMaterialToObject(mycore)
      Index = rs.ObjectMaterialIndex(mycore)
      rs.MaterialColor(Index,Color)
      
      #ox(SideLength, Corner)
      cLength = SideLength /2
      cCorner = rs.AddPoint(Corner.X - cLength, Corner.Y - cLength,0)
      cList.append(cCorner)
      capsule(coreH, capH, sL, cList)
      coreH = coreH + 2
      

def box(sL, sW, sH, CornerX,CornerY,CornerZ):
      pList = []
      point1 = rs.AddPoint(CornerX, CornerY, CornerZ)
      point2 = rs.AddPoint(CornerX + sL,CornerY, CornerZ)
      point3 = rs.AddPoint(CornerX + sL,CornerY +sW,CornerZ)
      point4 = rs.AddPoint(CornerX,CornerY+sW,CornerZ)
      point5 = rs.AddPoint(CornerX, CornerY, CornerZ+sH)
      point6 = rs.AddPoint(CornerX + sL,CornerY, CornerZ+sH)
      point7 = rs.AddPoint(CornerX + sL,CornerY +sW,CornerZ+sH)
      point8 = rs.AddPoint(CornerX,CornerY+sW,CornerZ+sH)
    
      pList.append(point1)
      pList.append(point2)
      pList.append(point3)
      pList.append(point4)
      pList.append(point5)
      pList.append(point6)
      pList.append(point7)
      pList.append(point8)
      return(rs.AddBox(pList))
      
      
      


#SideLength = rs.GetInteger("Please provide size of field(1-500)(X Axis)")
SideLength = 12
#SideLength2 = rs.GetInteger("Please provide size of field(1-500)(Y Axis)")
SideLength2 = 12
#Number = rs.GetInteger("Please provide the number of towers(1-15).")
#Number = 10
#CoreLength = rs.GetInteger("Please provide Core Width (Ex. 10)")
CoreLength = 5
#coreH = rs.GetInteger("Please provide Core Hiegth(Ex. 100)")
coreH = 80
#capH = rs.GetInteger("Please provide Capsule Hiegth(Ex. 10) ")
capH = 8
sq = square(SideLength,0)

#xScale = rs.GetReal("Please provide X-Axis scale factor for capsules.(Ex.1.5)")
#yScale = rs.GetReal("Please provide Y-Axis scale factor for capsules.(Ex.1.5)")
#zScale = rs.GetReal("Please provide Z-Axis scale factor for capsules.(Ex.1.1)")



dRegion = rs.GetObject("Select desired region:")
dRegionPts = rs.BoundingBox(dRegion)

#distGridPoints = rs.GetInteger("Please provide distance between points")
#dist = rs.GetInteger("Please provide radius of circle to remove random points.")

#groupCaps = rs.BooleanUnion(newCaps, delete_input=False)
#groupItems = rs.BooleanUnion(cItems, delete_input=False)

#boolTest = rs.BooleanUnion((groupCaps, groupItems), delete_input=False)

bPts = city_grid(dRegionPts, 100)
#bPts = city_grid(dRegionPts, distGridPoints)
P = []
for i, point in enumerate(bPts):
    if rs.PointInPlanarClosedCurve(point, dRegion):
       P.append(point)
# get a list of random points
#P = RandomPoints(Number,SideLength,SideLength2)
#cgX = rs.GetInteger("Please provide size of field(X Axis) try 300")
#cgY = rs.GetInteger("Please provide size of field(Y Axis) try 700")
#pDis = rs.GetInteger("Provide distance between points(try 100)")


#P = city_grid(400,800,0,100)
#P = city_grid(cgX,cgY,0,pDis)

#x_dim = rs.GetInteger("Please provide size of field(1-500)(X Axis)")
#y_dim = rs.GetInteger("Please provide size of field(1-500)(Y Axis)")
#size = rs.GetInteger("Please provide the number of towers(1-15).")

#P = city_grid(x_dim, y_dim, 0, size)

#dx = 
#dy =
#d2x = 
#d2y = 
#d3x = 
#d3y = 

#sq = square(SideLength, P[1])
core(coreH, capH, CoreLength, P) 




#objs = rs.GetObjects("Select all objects to rotate")
#if objs:
#    point = rs.GetPoint("Center point of rotation")
#    #point = rs.AddPoint(0,0,0)
#    if point:
#        rs.RotateObjects( objs, point, 180, None , True )





