'''
/** 
    * Instructions to candidate.
    * 1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
    * 2) Consider adding some additional tests in doTestsPass(). 
    * 3) Implement def shortestPath(self, fromStationName, toStationName)
    method to find shortest path between 2 stations
    * 4) If time permits, some possible follow-ups. 
    */ 
    
/** 
*   Visual representation of the Train map used 
* 
*   King's Cross St Pancras --- Angel ---- Old Street 
*   |                 \                             |
*   |                  \                             |
*   |                   \                             |
*   Russell Square       Farringdon --- Barbican --- Moorgate
*   |                                                /
*   |                                               /
*   |                                              /
*   Holborn --- Chancery Lane --- St Paul's --- Bank
*/
'''
from functools import reduce 
'''
/** 
 * class Station
 * 
 * Respresents Station in the rail network. Each station is identified by
 * unique name. Station is connected with other stations - this information
 * is stored in the 'neighbours' field. Two station objects with the same name are
 * equal therefore they are considered to be same station. 
 */
'''
import sys
class Station: 
    def __init__(self, name):
        self._name = name
        self._neighbours = [] 
        
    def getName(self):
        return self._name 
        
    def addNeighbour(self, station):
        self._neighbours.append(station) 
        
    def getNeighbours(self):
        return self._neighbours 
        
    def __eq__(self, other):
        return isinstance(other, Station) and self._name == other.getName() 
        
    def hash (self):
        return hash((self._name)) 
        
''' 
/**
 * class TrainMap 
 * Respresents whole rail network - consists of number of the Station objects
 * Stations in the map are bi-directionally connected. Distance between any 2 stations 
 * is of same constant distance unit. This implies that shortest distance between any 
 * 2 stations depends only on number of stations in between
 */
'''
class TrainMap: 
    def __init__(self):
        self._stations = {}
        
    def addStation(self, stationName):
        self._stations[stationName] = Station(stationName) 
        return self 
        
    def getStation(self, stationName):
        return self._stations[stationName] 
        
    def connectStations(self, fromStation, toStation):
        fromStation.addNeighbour(toStation) 
        toStation.addNeighbour(fromStation) 
        return self 
        
    def convertPathToString(self, path): 
        if(len(path) == 0): 
            return "" 
        else:
            print(reduce(lambda sl, s2: sl + "->" + s2, map(lambda station: station.getName(), path)))
            return reduce(lambda sl, s2: sl + "->" + s2, map(lambda station: station.getName(), path)) 
            
    def shortestPath(self, start, goal):
        visited=[]
        q=[[self._stations[start]]]
        if self._stations[start]==self._stations[goal]:
            return [self._stations[start]]
        while q:
            path=q.pop(0)
            node=path[-1]

            if node not in visited:
                neighbours=self.getStation(node.getName()).getNeighbours()

                for neighbour in neighbours:
                    new_path=list(path)
                    new_path.append(neighbour)
                    q.append(new_path)


                    if neighbour.getName() == goal:
                        return new_path

                visited.append(node)
        
        return new_path
        


def doTestsPass(): 
    # todo: implement more tests, please 
    # feel free to make testing more elegant
    trainMap = TrainMap() 
    trainMap.addStation("King's Cross St Pancras").addStation("Angel").addStation("Old Street").addStation("Moorgate").addStation("Farringdon").addStation("Barbican").addStation("Russel Square").addStation("Holborn").addStation("Chancery Lane").addStation("St Paul's").addStation("Bank") 
    trainMap.connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Angel")).connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Farringdon")).connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Russel Square")).connectStations(trainMap.getStation("Russel Square"), trainMap.getStation("Holborn")).connectStations(trainMap.getStation("Holborn"), trainMap.getStation("Chancery Lane")).connectStations(trainMap.getStation("Chancery Lane"), trainMap.getStation("St Paul's")).connectStations(trainMap.getStation("St Paul's"), trainMap.getStation("Bank")).connectStations(trainMap.getStation("Angel"), trainMap.getStation("Old Street")).connectStations(trainMap.getStation("Old Street"), trainMap.getStation("Moorgate")).connectStations(trainMap.getStation("Moorgate"), trainMap.getStation("Bank")).connectStations(trainMap.getStation("Farringdon"), trainMap.getStation("Barbican")).connectStations(trainMap.getStation("Barbican"), trainMap.getStation("Moorgate")) 
    solution = "King's Cross St Pancras->Russel Square->Holborn->Chancery Lane->St Paul's" 
    return solution == trainMap.convertPathToString(trainMap.shortestPath("King's Cross St Pancras", "St Paul's")) 


if __name__ =="__main__":
    if(doTestsPass()):
        print('All Tests Pass')
    else:
        print('Some tests fail')

 
 
