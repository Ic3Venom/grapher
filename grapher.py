from operator import index
import sys

class Term:
    def analyze(self):
        pass
    def __init__(self, term, xvalue):
        
        analyze(term)


def printGraph(graph):
    for row in graph:
        for column in row:
            if column == 0:
                sys.stdout.write('  ')
            elif column == 1:
                sys.stdout.write('0 ')
            elif column == 2:
                sys.stdout.write('- ')
            elif column == 3:
                sys.stdout.write('+ ')
        else:
            sys.stdout.write('\n')
    
    raw_input()

def setup(resolution):
    #sets up graph's origin and empty values using information from resolution[]
    #value codes: 0:empty; 1:point; 2:axis; 3:origin
    
    graph = []
    for row in range(int(resolution[0])):
        graph.append([])
        
        for column in range(int(resolution[1])):
            graph[row].append(0)
            
            if row == resolution[0]/2 and column == resolution[1]/2:
                graph[row][column] = 3
            
            elif row == resolution[0]/2:
                graph[row][column] = 2
                  
            elif column == resolution[1]/2:
                graph[row][column] = 2
                
    printGraph(graph)

def main():
    graph = []
    resolution    = [0,0,'']
    
    try:
        resolution[2] = raw_input("How many pixels do you want your graph to extend from the origin? (Format: xDistance x yDistance): ")
        resolution[0] = 2 * int(resolution[2][:resolution[2].index('x')])    + 1 #multiplying by 2 to get +/- x values, +1 for x axis
        resolution[1] = 2 * int(resolution[2][resolution[2].index('x') +1:]) + 1 #multiplying by 2 to get +/- y values, +1 for y axis
        
    except TypeError:
        print 'Unknown length arguments \'%s\'. Exiting program.' % resolution[2]
        exit(1)
        
    graph = setup(resolution)
    print resolution, resolution[0]/2, resolution[1]/2
 
if __name__ == '__main__':
    main()
    
    exit
