from random import randrange

def getdailyquote(filepath: str) -> str:
    '''
        read file and return quote
    '''
    print(filepath)
    try:
        with open(filepath,"r") as fobj:
            content = fobj.readlines()
            rn = randrange(0,len(content))
    except:
        print("File Not Found")
        raise Exception
    return content[rn]

