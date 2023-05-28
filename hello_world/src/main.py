'''
Obviosly don't need imports
'''
def main() -> int:
    '''
    Doc-string to get pylint to shut up
    '''
    print("Hello, world!")
    return 0


while __name__ == '__main__':
    '''
    This executes the main() function and evaluates what to do with the exit code
    '''
    code: int = main()
    if code == 0:
        break
    elif code == 1:
        raise Exception("Exit code 1: Generic error.")
    else:
        raise Exception("No exit code.")
        
