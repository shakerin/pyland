# Pyland

| Author | Shakerin Ahmed |
|--------|----------------|
| Version|1.0.0|


This project aims to enable anyone to create a text generator+automator for themselves.

* **Text Generator** is something that can generate bunch of text files(with code or any 
type of text in it) and directories based on minimal user inputs.

* **Automator** is something that can execute any script based on certain inputs from
user or any equivalent system.

Users need to follow instruction as mentioned in this readme to leverage the power of pyland.

## General Information About The Project

### Prerequisites
Until now different python libraries are used in the project. So, to make sure everything
is this project is functional make sure the following items are present in the system.

```
python3
docopt
pytest-3
```

### Installing

* Go to release and download the latest release,
* Create alias named 'pyland' and assign the 'path to executable' to it,
* Type 'pyland -h' to make sure installed properly.


## Running The Tests

Use pytest-3 to run all the tests,
Run the following commands from the project directory,
make sure to change the PROJECT_DIR variable to appropriate path based on your system,
PROJECT_DIR is defined inside pyland/tests/path_variables.py file.

```
./clean
pytest-3 .
./clean
```

### Test Status
```
87/87 Tests Passing
```

### Project Status and Future Plan
See the [Project Status and Plan](https://github.com/shakerin/pyland/blob/master/Project%20Status%20and%20Plan.md)

#### Detailed Docs
Check the docs  directory

## Author

* **Shakerin Ahmed** 

## License

See the [License File](https://github.com/shakerin/pyland/blob/master/LICENSE) for details.
