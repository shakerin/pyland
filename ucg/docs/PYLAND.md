# Pyland Class

## Class Internal Information

|Attribute|Type|Description
|---------|----|-----------|
|frame_dirs|list of strings|each item in list represents a directory that contains frame files|
|TL1|TemplateLibrary Object|it uses frame_dirs to extract frames as TemplateInfo objects|
|ST1|Structure Object|it uses structure file to analyse directory structure|
|frame_generated_code|a string|it represents the generated code from frame cmd|



## Usage

There are mainly 2 methods of using this class.


* To Generate Code and/or Execute Python Commands Based on Frame Cmd
```
import Pyland
frame_dirs = ['path1/', 'path2']
structure_file_path_main = "frameName{'arg1':'value1', 'arg2':'value2'}"
output_file_name = 'outputpath.txt'
var = Pyland(frame_dirs, structure_file_path_main, output_file_name)
```


* To Generate Structure Based on Structure File
```
import Pyland
frame_dirs = ['path1/', 'path2']
structure_file_path_main = 'structurefile.struct'
var = Pyland(frame_dirs, structure_file_path_main)
```

## About Frame Cmd

A frame command is nothing but name of a frame followed by arguments required
to generate text and execute python code inside that frame file.

### Example Frame Cmd
```
frameName{'arg1':'value1', 'arg2':'value2'}
```
### Example Frame File 

* Frame file name without the extension is the frame name.
* If frame file name is : frameName.ext, then frame name is 'frameName'.

```
This is $arg1.
I am Text
<<<
with open('$arg2') as f:
  f.write("This section inside <<< and >>> is refered as python code in Pyland.")
>>>
```



## About Structure File

### An Example Structure File
```
dir1//
  file1.txt,,frame1{'arg1':'something'}
  dir2//
    file2.txt,,frame2{'arg2':'something'}
  dir3//
```

### Output Of The Example Structure File
* Following directories will be created if not present
```
dir1/
dir1/dir2/
dir1/dir3/
```

* Following files will be created
```
dir1/file1.txt
dir1/dir2/file2.txt
```

* Following Frames will be used to generate text and/or execute python code
```
frame1 frame will be executed and generated code will be copied to dir1/file1.txt
frame2 frame will be executed and generated code will be copied to dir1/dir2/file2.txt
```

#### Notes
* frame1 and frame2 frames must be present in any directory listed in 'frame_dirs'
