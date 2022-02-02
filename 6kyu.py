def cake(candles,debris):
    total = 0
    alpha_position = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    # debris = list(debris)
    for x in range(len(debris)):
        if x % 2 == 0:
            total += ord(debris[x])
            # print(f'current even total: {ord(debris[x])}')
        else:
            if debris[x] in alpha_position:
                total += alpha_position[debris[x]]
                # print(f'current odd total: {alpha_position[debris[x]]}')
    return "Fire!" if (candles * .7) < total else "That was close!"

print(cake(12, 'jaam'))