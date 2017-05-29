from operator import index
class Term:
    
    def __init__(self, xvalue):
        pass



def main():
    resolution    = [0,0,raw_input("What resolution do you want your graph to be? (Format: x*y): ")]
    resolution[0] = resolution[2][:resolution[2].index('*')]
    resolution[1] = resolution[2][resolution[2].index('*') +1:]
    
    print resolution
 
if __name__ == '__main__':
    main()
    
    exit
