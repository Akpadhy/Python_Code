def TowerOfHanoi(numberofdisk,startpeg,endpeg):
    if numberofdisk:
        TowerOfHanoi(numberofdisk-1,startpeg,6-startpeg-endpeg)
        print "Move disk %d from peg %d to peg %d" %(numberofdisk,startpeg,endpeg)
        TowerOfHanoi(numberofdisk-1,6-startpeg-endpeg,endpeg)

def main():
    height = int(input('Height of hanoi: '))
    TowerOfHanoi(height,1,3,)

if __name__ == '__main__':
    main()        