# CliArgTools
-----
Small and easy to use cross-platform Python library for working with command line arguments.

CliArgTools allows you to easily get the command line arguments, check if the flags are provided, check if filepath is valid and/or has expected filetype and generate and/or output error message if cli arguments given by the user is incorrect.

Made as simple to use as it gets and mostly for personal use because i was tired of making the same logic again and again for my own apps. So its more of a study project than a serious library.  

> This library is not intended to be used in any kind of important production environment

----

##### Code example:
```python
import cliargtools

FILEPATH = cliargtools.getArgByFlag('-fp')  # will add required flag -fp
FILEPATH_VALID = cliargtools.isPathValid(FILEPATH) # will check if path is valid
DEBUG = cliargtools.isFlagPresent(['-debug', '-dbg']) # will check for optional flag -debug
ALL_ARGS = cliargtools.getAllArgs()         # will return all the arguments given

if (DEBUG): 
     # printing our interesting stuff if -debug or -dbg argument is present
    print("debug: " + str(DEBUG))
    print("some filepath: " + FILEPATH)
    print("this path is valid: " + str(FILEPATH_VALID))   
    print("cli arguments: " + ' '.join(ALL_ARGS))
else: 
    print("Sadly, no debug, but the program still works!")
```

------


## ```GetArgsByFlag```
Can be used to get the value provided after any flag. 


#### arguments:
##### required:
- ```flag``` - string or array/tuple of strings that will be used to identify the argument (example: ```"-i"```, ```['-f', '-file']```)
##### optional:
- ```optional: bool = False``` specifies if the argument is optional or required
- ```defaultValue: any``` - value that will be returned if not value was given by user
- ```errorMessage: str``` - will be printed if any error is present and not optional
- ```errorMessageIfNoArg: str``` - will be printed if flag was given but the value wasn't provided
- ```errorMessageIfNoFlag: str``` - will be printed if required flag wasn't given
- ```defaultErrors: bool = True``` - specifies if default errors will be printed, ```True``` by default.

##### returns:  
- ```str``` - string if given by the user after the ```flag``` 
- ```defaultValue``` - if required argument is not given by the user

By default the flag argument will be required by the program, but can be set to optional with ```optional``` keyword argument. In this case will return ```None``` if the value wasn't present. 

If argument is not optional will print the default error message, specifying what is wrong with the arguments given by the user.


Error messages can be overriden by the ```errorMessage```, ```errorMessageIfNoArg```, and ```errorMessageIfNoFlag``` keyword arguments. 

Default error messages can be disabled by setting ```defaultErrors``` to ```False```

```python
getArgByFlag(flag: str | list | tuple, 
                optional:bool = False,
                defaultValue:str = None, 
                errorMessage:str = None,
                errorMessageIfNoArg:str = None, 
                errorMessageIfNoFlag:str = None, 
                defaultErrors:bool = True)
```


------



## ```isFlagPresent```
Can be used to check if the flag is given by the user. 

#### arguments:
##### required:
- ```flag``` - string or array/tuple of stings that will be used to identify the argument (example: ```"-d"```, ```['-d', '-debug']```)
##### optional:
- ```optional: bool = True``` specifies if the flag is optional or required
- ```errorMessage: str``` - will be printed if any error is present and not optional
- ```defaultErrors: bool = True``` - specifies if default errors will be printed, ```True``` by default.

##### returns:  
- ```bool``` - ```True``` or ```False``` value where ```True``` means that argument was given by the user, and ```False``` means that it is missing.


By default the flag is optional, it means that no error missage will be printed if the flag is missing and ```False``` will be returned.
This behaviour can be changed by the ```optional``` keyword argument. if ```optional=False``` will print ```errorMessage``` if the flag wasn't present.

Default error messages can be disabled by setting ```defaultErrors``` to ```False```
Error message can be overriden by the ```errorMessage``` keyword argument.

```python
isFlagPresent(flag: str | list | tuple,
                optional:bool = True, 
                errorMessage:str = None,
                defaultErrors:bool = True)
```

------



## ```isPathValid```
Can be used to check if the path is valid and/or file extension matches required.

#### arguments:
##### required:
- ```path: str``` - path to validate
##### optional:
- ```expectedFileExtensions: str | list | tuple``` string or array/tuple of strings specifying the expected file extensions
- ```errorMessageWrongType: str``` - will be printed if path exists but extension doesn't match any of specified
- ```errorMessagePathInvalid: str``` - will be printed if given path doesn't exist
- ```defaultErrors: bool: true```- specifies if default errors will be printed, ```True``` by default.

##### returns:  
- ```bool``` - ```True``` or ```False``` value where ```True``` means that path exists and file extension matches specified(if given), and ```False``` means that path is invalid or file extension doesn't match any of the specified.


Default error messages can be disabled by setting ```defaultErrors``` to ```False```
Error messages can be overriden by the ```errorMessageWrongType``` or ```errorMessagePathInvalid``` keyword arguments.

```python
isPathValid(path:str, 
                expectedFileExtensions: str | list | tuple = None,
                errorMessageWrongType: str=None, 
                errorMessagePathInvalid: str=None,
                defaultErrors: bool=True)
```

------

## ```getAllArgs```
Can be used to get the list of all the arguments given by the user


##### returns:  
- ```list``` - list of all the values given as a cli arguments by the user 

```python
getAllArgs()
```
