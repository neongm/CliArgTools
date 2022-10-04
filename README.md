# CliArgTools
-----

### Use pip to install the CliArgTools:  ```pip install CliArgTools```
Small and easy to use cross-platform Python library for working with command line arguments.
CliArgTools allows you to easily get the command line arguments, check if the flags are provided and generate and/or output error message if cli arguments given by the user is incorrect.


##### Code example:
```python
import cliargtools

FILEPATH = cliargtools.getArgByFlag('-fp')  # will add required flag -fp
DEBUG = cliargtools.isFlagPresent('-debug') # will check for optional flag -debug
ALL_ARGS = cliargtools.getAllArgs()         # will return all the arguments given

if (DEBUG): 
    print("debug: " + str(DEBUG))
    print("some filepath: " + FILEPATH)                 # printing given filepath  and all the arguments
    print("cli arguments: " + ' '.join(ALL_ARGS))       # if -debug argument is present
else: 
    print("Sadly, no debug, but the program still works!")
```

------


## ```GetArgsByFlag```
Can be used to get the value provided after any flag. 


#### arguments:
##### required:
- ```flag``` - string that will be used to identiry the argument (example: ```"-i"```)
##### optional:
- ```optional: bool = False``` specifies if the argument is optional or required
- ```defaultValue: any``` - value that will be returned if not value was given by user
- ```errorMessage: str``` - will be printed if any error is present
- ```errorMessageIfNoArg: str``` - will be printed if flag was given but the value wasn't provided
- ```errorMessageIfNoFlag: str``` - will be printed if required flag wasn't given
- ```defaultErrors: bool = True``` - specifies if default errors will be printed, ```True``` by default.

##### returns:  
- ```str``` - string if given by the user after the ```flag``` 
- ```defaultValue``` - if required argument is not given by the user

By default the flag argument will be required by the program, but can be set to optional with ```optional``` keyword argument. In this case will return ```None``` if the value wasn't present. 

If argument is not optional will print the default error message, specifying what is wrong with the arguments given by the user.


Error messages can be overriden by the ```errorMessage```, ```errorMessageIfNoArg```, and ```errorMessageIfNoFlag``` keyword arguments. 

Default error messages can be disabled by setting ```defaultArgumets``` to ```False```

```python
getArgByFlag(flag: str, optional:bool = False, defaultValue:str = None, 
                 errorMessage:str = None, errorMessageIfNoArg:str = None, 
                 errorMessageIfNoFlag:str = None, defaultErrors:bool = True)
```


------



## ```isFlagPresent```
Can be used to check if the flag is given by the user. 

#### arguments:
##### required:
- ```flag``` - string that will be used to identiry the argument (example: ```"-i"```)
##### optional:
- ```optional: bool = True``` specifies if the flag is optional or required
- ```errorMessage: str``` - will be printed if any error is present
- ```defaultErrors: bool = True``` - specifies if default errors will be printed, ```True``` by default.

##### returns:  
- ```bool``` - ```True``` or ```False``` value where True means that argument was given by the user, and ```False``` means that it is missing.


By default the flag is optional, it means that no error missage will be printed if the flag is missing and ```False``` will be returned.
This behaviour can be changed by the ```optional``` keyword argument. if ```optional=False``` will print ```errorMessage``` if the flag wasn't present.

Default error messages can be disabled by setting ```defaultArgumets``` to ```False```
Error message can be overriden by the ```errorMessage``` keyword argument.

```python
isFlagPresent(flag, optional=True, errorMessage=None, defaultErrors:bool = True)
```

------


## ```getAllArgs```
Can be used to get the list of all the arguments given by the user


##### returns:  
- ```list``` - list of all the values given as a cli arguments by the user 

```python
getAllArgs()
```
