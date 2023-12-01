import itertools
import argparse
import sys
from itertools import combinations

def angle(set1,set2,key,i,total): 
  a1 = set1[0]
  b1 = set1[1]
  a2 = set2[0]
  b2 = set2[1]
  if (a2-a1) != 0 : 
    ang = (b2-b1)/(a2-a1) 
    add = b1 -(ang * a1)
    lines[total] = [[set1, set2], ang, add,0]
    if ang == 0: 
      lines[total] = [[set1, set2], ang, add,1]
    for line in points:
      if (line > i): 
        if (points[line][0][1] == (ang * points[line][0][0] + add)):
          lines[total][0].append(points[line][0]) 
          points[key][1].append(str(line))
          points[i][1].append(str(line))
          points[line][1].append(str(key))
          points[line][1].append(str(i))
  else:
    add =  a1
    ang = "-"
    lines[total] = [[set1, set2], ang, add,1]
    for line in points:  
      if (line > i):
        if (points[line][0][0] == a1): 
          lines[total][0].append(points[line][0])
          points[key][1].append(str(line))
          points[i][1].append(str(line))
          points[line][1].append(str(key))
          points[line][1].append(str(i))

def finding_max():  
  max = -1
  position = -1
  for key in lines:
      if len(lines[key][0]) > max:
        if key not in positions:
          max= len(lines[key][0])
          position = key
  if position != -1:
    positions.append(position)
  return position

def finding_maxg(): 
  max = -1
  position = -1
  for key in lines:
    if lines[key][3] == 1:
      if len(lines[key][0]) > max:
        if key not in positions:
          max = len(lines[key][0])
          position = key
  if position != -1:
    positions.append(position)        
  return position

def rSubset(arr, r):  
  return list(combinations(arr, r))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    argumentList = sys.argv[1:] 
    l = len(argumentList)
    cross_file = argumentList[l-1] 
    points={}
    count = 0
      
    with open(cross_file) as schema:
       rows = schema.readlines() 
       sorted_rows = sorted(rows, key=lambda x: int(x.split()[0]), reverse=False) 
       for line in sorted_rows:
         parts = [x for x in line[:-1].split()] 
         pos = (int(parts[0]), int(parts[1])) 
         connected = []
         points[count] = [pos,connected] 
         count = count + 1 
    lines = {}
    total = 0
    for key in points: 
      set1 = points[key][0] 
      if (key + 1 != len(points)): 
        for i in range(key + 1, len(points)):
          if (str(i) not in points[key][1]):  
            points[key][1].append(str(i)) 
            points[i][1].append(str(key))  
            set2 = points[i][0]  
            angle(set1,set2,key,i,total)  
            total = total+1
    unvisited = []
    visited = []
    count = 0
    for key in points:
      count = count +1 
    for key in points:
      unvisited.append(points[key][0]) 
    result={}
    positions = []
    how = 0 
    final={}
  
    if l == 2 and (argumentList[l-2] == '-g'):   
        while len(visited) != count: 
            position = finding_maxg() 
            if position != -1:
                for i in range(0,len(lines[position][0])): 
                    if lines[position][0][i] not in visited:
                        visited.append(lines[position][0][i])  
                result[how] = (lines[position][0]) 
                how = how + 1
            elif (position == -1) and (len(visited)!= count): 
                for key in points:
                    if points[key][0] not in visited:
                        visited.append(points[key][0]) 
                        one = points[key][0][0] 
                        two = points[key][0][1]
                        result[how] = (points[key][0],(one+1,two)) 
                        how = how +1

    elif l == 2 and (argumentList[l-2] != '-g'): 
        print('Can not find')
    elif l == 3: # -f and -g
        arr = []
        counter = 0
        for key in lines:
          if lines[key][3] == 1:  
            arr.append(key)
            counter = counter + 1
        back = 0
        backup={}
        backupvisited = []
        how2 = 0
        for r in range(2,counter): 
          block = False
          flag = True
          diction = {}  
          keydiction = 0 
          f = rSubset(arr,r) 
          for i in range(0,len(f)):  
            diction[keydiction] = f[i]
            keydiction=keydiction + 1
          for key in diction: 
            visited = [] 
            linescount = 0
            comb = (diction[key])    
            for i in range(0,len(comb)): 
              flag = True
              myline = lines[comb[i]]
              for x in range(0,len(myline[0])): 
                if myline[0][x] in visited:
                  flag = False
                  break
              if flag:
                for x in range(0,len(myline[0])):
                  visited.append(myline[0][x])
                linescount = linescount + 1 
              else: 
                  break
            if linescount == r:
              if len(visited) == count:
                for i in range(0,len(comb)):
                  myline2 = lines[comb[i]] 
                  result[how] = myline2[0] 
                  how = how + 1
                  block = True
                break 
              else:  
                if len(visited) > back:
                  how2 = 0 
                  backup= {}
                  backupvisited = visited
                  for i in range(0,len(comb)): 
                    back = len(visited) 
                    myline2 = lines[comb[i]]
                    backup[how2] = myline2[0]
                    how2 = how2 + 1
          if block:
            break;
        if result == {}:
          result = backup
          for key in points:
            if points[key][0] not in backupvisited:  
                visited.append(points[key][0])
                one = points[key][0][0]
                two = points[key][0][1]
                result[how2] = (points[key][0],(one+1,two))
                how2 = how2 +1 
    else:
        while len(visited) != count: 
           flag= True
           position = finding_max()
           for i in range(0,len(lines[position][0])):
              if lines[position][0][i] in visited:
                    flag = False 
                    break
           if flag:
                for i in range(0,len(lines[position][0])):  
                    visited.append(lines[position][0][i])
                result[how] = (lines[position][0])
                how = how + 1
    
    for key in result: 
        print(*result[key])
        
