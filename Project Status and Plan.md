# Pyland

## Information about completed items
* TemplateInfo class represents the structure of each frame class,
* FileToTemplate class is same as TemplateInfo except, it reads the frame string from a file,
* TemplateLibrary class is the place where frame objects are created for all frame strings,
* frame objects from TemplateLibrary class can be utilized to generate text or execute accessible system commands,

## Next Step
* Finalize a structure that can be used for generating texts and execute commands easily from users perspective,
* Plan the directory structure development as well where TemplateLibrary instance has to be used for automation


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
    frame_simple_v2({'something': "$name"})
        This will call the frame_simple_v2 frame to generate text and 
        execute python codes based on the arguments provided in the 
        dictionary
    


## FrameDir File Example

    dir1//
        file11<frameObj(<dict argument>)>,,
        file12<frameObj(<dict argument>)>,,
    dir2//
        file21<frameObj(<dict argument>)>,,
        dir21//
            file211,,
            file212<frameObj(<dict argument>)>,,
            dir211//,,
    file1<frameObj(<dict argument>)>,,
    file2<frameObj(<dict argument>)>,,


## Basic Frame Commands

    -> users should be able to create files based on any frame
       using either frame commands or frameDir files


## Steps of operation

### step 1
    User needs to generate+execute something, does frame command exist?
    if yes, step 2 else step 6.

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

### step 6
    create new frame file/s and/or frameDir file/s based on requirement,
    place the new files in frame directory so that TemplateLibrary
    can find out the place,
    go to step 5.












