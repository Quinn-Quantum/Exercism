def color_code(color):
    colorCode = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9  
}
    return colorCode[color]
    


def colors():
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue',  'violet', 'grey', 'white' ]



def value(colors):
    colorList = [
        'black','brown','red','orange','yellow','green','blue','violet','grey','white' 
    ]

    return int(str(colorList.index(colors[0])) + str(colorList.index(colors[1])))
