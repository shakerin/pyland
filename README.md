# Pyland
This project aims to enable anyone to create a text generator+automator for themselves.

* **Text Generator** is something that can generate bunch of text files(with code or any 
type of text in it) and directories based on minimal user inputs.

* **Automator** is something that can execute any script based on certain inputs from
user or any equivalent system.

Users need to follow instruction as mentioned in this readme to leverage the power of pyland.

## General Information About The Project

### Developers
I am the only developer and planner of the project for now. Any idea or suggestion is welcome.

### Users
This project is not in a state yet to deliver to any user who is not experienced in python.

### Prerequisites
Until now different python libraries are used in the project. So, to make sure everything
is this project is functional make sure the following items are present in the system.

```
python3
docopt
pytest-3
```

### Installing

As per today, it is *not installable*.

### Common Terms

#### frame string
This is a string that contains (i) all text that has to be generated, (ii) scripts that
has to be executed when object of this frame string is used.
An automator, that uses Pyland structure, can have as many frame strings as required.
*frame string concept already delevoped in Pyland*

#### frame file
This is the file that contains frame strings. A frame string class is named after the
name of the frame file name.
*frame file concept already delevoped in Pyland*

#### frame object
It is also called frame string object. It is an instance that is created based on a 
frame string class.
*frame object concept already delevoped in Pyland*


## Running The Tests

Use pytest-3 to run all the tests. Run the following command from the project directory.
```
pytest-3 .
```

### Test Status
```
77/77 Tests Passing
```

### Project Status and Future Plan
See the [Project Status and Plan](https://github.com/shakerin/pyland/blob/master/Project%20Status%20and%20Plan.md)

## Author

* **Shakerin Ahmed** 

## License

See the [License File](https://github.com/shakerin/pyland/blob/master/LICENSE) for details.
