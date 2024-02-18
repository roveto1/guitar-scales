#         0   1    2   3    4   5   6    7   8    9   10  11
typeA = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
typeB = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
extra = ['B#','Cb','E#','Fb']
extrc = ['C','B','F','E']

major = [0,2,4,5,7,9,11]
minor = [0,2,3,5,7,8,10]
hminor = [0,2,3,5,7,8,11]
mminor = [0,2,3,5,7,9,11]
pent = [0,3,5,7,10]
Blues = [0,3,5,6,7,10]
notes = [0,1,2,3,4,5,6,7,8,9,10,11]

scaleList = [major,minor,hminor,mminor,pent,Blues,notes]
scaleListName = ['  Major  ','  Minor  ','HMinor ','MMinor ','  Pent   ', '  Blues  ','    All    ']

TITLE = "Escalas na Guitarra"
WIDTH = 800*2
HEIGHT = 416*2
FPS = 60

# define colors
WHITE = (255, 255, 255)
GRAY = (255/4, 255/4, 255/4)
LGRAY = ((255/4)*3, (255/4)*3, (255/4)*3)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)