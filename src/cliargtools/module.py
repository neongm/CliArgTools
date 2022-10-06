from sys import argv 
import os.path
from types import NoneType


def getArgByFlag(flag: str, optional:bool = False, defaultValue:str = None, 
                 errorMessage:str = None, errorMessageIfNoArg:str = None, 
                 errorMessageIfNoFlag:str = None, defaultErrors:bool = True):
    argValue = defaultValue
    argFlagIndex = None
    flagPresent = False
    argPresent = False
    
    try:
        argFlagIndex = argv.index(flag)
        flagPresent = True
        argValue = argv[argFlagIndex+1]
        argPresent = True
        
    except:

        if optional: return argValue
        if defaultErrors: # we don't really need to do it if there is no error in the first place, right?
            if errorMessage == None: 
                errorMessage = f'Command line argument error: {flag} <value>'
            if errorMessageIfNoArg == None: 
                errorMessageIfNoArg = 'Argument value not provided'
            if errorMessageIfNoFlag == None and not optional: 
                errorMessageIfNoFlag = f'Required flag {flag} not provided'
        if errorMessage: print(errorMessage)
        if flagPresent and not argPresent and errorMessageIfNoArg: print(errorMessageIfNoArg)
        if not flagPresent and not optional and errorMessageIfNoFlag: print(errorMessageIfNoFlag)

    return argValue


def isFlagPresent(flag, optional=True, errorMessage=None, defaultErrors:bool = True):
    if flag in argv: return True
    if optional: return False
    if not errorMessage and defaultErrors:
        print(f'Required flag {flag} not provided')
        return False
    if errorMessage:
        print(errorMessage)
        return False


def isPathValid(path:str, expectedFileExtensions: str | list | tuple = None,
                errorMessageWrongType: str=None, errorMessagePathInvalid: str=None,
                defaultErrors: bool=True):
    
    # check if the filepath was even passed first
    if type(path) is NoneType: return False 
    
    pathValid = os.path.exists(path)
    
    # if file doesn't exist
    if not pathValid: 
        if defaultErrors:
            print(f"Invalid path: {path}")
        elif errorMessagePathInvalid is not None: 
            print(errorMessagePathInvalid)
        return pathValid
    
    # if file exists check for type stuff
    if expectedFileExtensions == None: return pathValid
    if path.endswith(expectedFileExtensions): return pathValid
    else:  
        if defaultErrors:
            if type(expectedFileExtensions) is str: 
                print(f"Expected file path extension type: {expectedFileExtensions}") 
            else: 
                print(f"Expected file path extension type: {' '.join(expectedFileExtensions)}") 
        else:
            print(errorMessageWrongType)
            
    return pathValid


def getAllArgs(): 
    return argv
