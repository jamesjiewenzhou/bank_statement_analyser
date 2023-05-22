# bank_statement_analyser

## Updated GUI Organisation
### OOP Conversion
Key functions:
- __init__
    - declares the app
    - opens the file dialog (calls function?) - done
    - calls function to read the file - done
- function to open file dialog
    - returns string associated with file dialog to save in __init__ as an attribute - done
- read csv function
    - returns a dataframe with all the data to save in __init__ as an attribute
- header declaration function
    - saves a header frame to self.header_frame
- canvas declaration function
    - creates the scrollable canvas and saves it into self.canvas
- calculator frame
    - creates the calculator frame and defines the buttons to save value to self.sum?
- resize window function
    - resizes the window based on the root, canvas, and other window stuff


### Post OOP Conversion
Key changes and updates
- create that utils package for any additional non gui related functions
- graphing of spending patterns
- 