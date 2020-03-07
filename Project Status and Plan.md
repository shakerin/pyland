# Pyland

## Information about completed items
* TemplateInfo class represents the structure of each frame class,
* FileToTemplate class is same as TemplateInfo except, it reads the frame string from a file,
* TemplateLibrary class is the place where frame objects are created for all frame strings,
* frame objects from TemplateLibrary class can be utilized to generate text or execute accessible system commands,
* Finalize a structure that can be used for generating texts
* execute commands easily from users perspective

## Next Step
* create package for distribution


## Common Terms

### frame string
This is a string that contains (i) all text that has to be generated, (ii) scripts that
has to be executed when object of this frame string is used.
An automator, that uses Pyland structure, can have as many frame strings as required.
*frame string concept already delevoped in Pyland*

### frame file
This is the file that contains frame strings. A frame string class is named after the
name of the frame file name.
*frame file concept already delevoped in Pyland*

### frame object
It is also called frame string object. It is an instance that is created based on a 
frame string class.
*frame object concept already delevoped in Pyland*

### frame cmd
This is a method where user only provides the frame object name and input argument
values for code generation and python code execution.
*frame cmd concept already delevoped in Pyland*

### structure file
This is a text file containing all directory and file names for creation.
User can mention the frame object name and provide arguments in proper form
for text auto generation in that file and also execution of any python code.
*structure file concept already delevoped in Pyland*

## Structure to generate some code

### Existing Structure

#### From inside the TemplateLibrary class
    self.getAll(self.frame_simple_v2,{
        'something': "$name"
    })

#### From outside the TemplateLubrary class or, Through an object
    insname.getAll(insname.frame_simple_v2,{
        'something': "$name"
    })


### User Friendly Structure In FrameDir Files
    frame_simple_v2{'something': "$name"}
        This will call the frame_simple_v2 frame to generate text and 
        execute python codes based on the arguments provided in the 
        dictionary
    


## FrameDir File Example (aka 'Structure File')

    dir1//
        file11,,frameObj{<dict argument>}
        file12,,frameObj{<dict argument>}
    dir2//
        file21,,frameObj{<dict argument>}
        dir21//
            file211,,
            file212,,frameObj{<dict argument>}
            dir211//
    file1,,frameObj{<dict argument>}
    file2,,frameObj{<dict argument>}


## Basic Frame Commands

    -> users should be able to create files based on any frame
       using either frame commands or frameDir files


## Steps of operation (frames)

### step 1
    User needs to generate+execute something, does frame command exist?
    if yes, step 2 else step 1_1.

### step 1_1
    create new frame file/s and/or frameDir file/s based on requirement,
    place the new files in frame directory so that TemplateLibrary
    can find out the place,
    go to step 2.

### step 2
    Use that frame to generate+execute text.

### step 3
    Does generated text contain any frameDir file?
    if yes, step 4, else step 5.

### step 4
    Use the frameDir file to generate+execute text,
    go to step 3.

### step 5
    done.
    

## Steps of operation (structure file)

### step 1
    User provides a frame dir file that contains all information about
    the directory structure, file names, frame objects associated with
    files including parameters (for now)
    
### step 2
    All directories and files will be created based on the inputs
    
### More
    Further details will be added after initial coding is complete.













