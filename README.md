# 2023-software-engineering-miniproject

This is a package to simulate the PK models finished by Yunli Qi, Dou Hong and Junde Wu.

## An Overview

This project has the following features:
 - It is pip installable. You can use the following command to install this project as a package: `pip install your/path/to/this/this/folder`
 - In the folder `tests` under `pkmodel`, you can find unit tests of functions in this project. Code coverage can be 100% when excluding code to plot and code to input a default model.
 - Everything is on the github and a automated workflow to run unit tests mentioned above is enabled using Github Action.

## Code Structure

For different scripts in the folder `pkmodel`, all functions and features are packed in classes.

### `solution.py`: a class named `Solution` is defined here. 

It is used to contain the solution of a set of initial conditions. You need to specify the number of compartments and the initial conditions to introduce a new instance. You can also determine the length of time you want to simulate.

### `model.py`: a class named `Model` is defined here. 

This class inherits from `Solution`. It has an extra attributes `eqn` to contain the governing equation of the model. You also need to specify the type of dosing protocol to define an instance. You are recommended to specify the argument `dose` to set the initial conditions under `'instantaneous'` dosing or adjust injection speed under `'steady'` dosing. 

#### Methods in class `Model`

Three more methods are introduced: 

 - `sim` method is used for generating simulation solutions
 - `plot` method is used for plotting simulation solutions
 - `compare` method is used for comparing plots of two different models

### protocol.py: classes named `intravenous` and `subcutaneous` are defined here. 

They are both subclasses of `Model`. When you specify every parameters needed in the model, specify the dosing protocol and dosing amount, a default model will be created. 
