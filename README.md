# Harris Corner Detection Algorithm


This Python program implements the Harris Corner Detection algorithm from first principles to identify corner features in images. 

### The implementation:

Calculates image gradients in x and y directions
Computes the structure tensor components (Ixx, Iyy, Ixy)
Evaluates cornerness using the Harris response function
Provides two different corner detection methods:

Method 1: Global threshold approach
Method 2: Block-based adaptive thresholding



## Key Features

Custom Gradient Calculation: Implements image derivative calculations without relying on built-in filters
Complete Harris Pipeline: Full implementation of all steps in the Harris corner detection algorithm

Multiple Detection Methods:

Global thresholding based on percentage of maximum response
Adaptive block-based thresholding for more distributed corner detection

Interactive Interface: Menu-driven selection of test images and detection methods
Visual Output: Corner visualization with green circles on the original image

## Requirements

Python 3.x
NumPy
OpenCV (cv2)

## Usage

### Run the program:
Copypython HarrisCorner_MontgomeryDimitri.py

### Select a test image from the menu:

Option 1: Checker board
Option 2: High contrast mushroom
Option 3: City scape
Option 4: Landscape
Option 5: Low contrast dog
Option 6: Person
Option 7: Your own image (provide filename)


### Choose a detection method:

Method 1: Basic global threshold approach
Method 2: Block-based computation method


The program will display the image with detected corners and save it as "assign3_HarrisCorner_Detection.png"

## Implementation Details
The Harris Corner Detection algorithm is implemented in these main steps:

### Gradient Calculation:

Computes image gradients (Ix, Iy) using simple pixel differences
Calculates gradient products (Ixx, Iyy, Ixy) for each pixel


### Cornerness Response Calculation:

Uses a sliding 3x3 window to sum gradient products
Applies the Harris formula: det(M) - k * trace(M)²
Creates a cornerness response map for the entire image


### Corner Detection Methods:

Method 1 (Global): Applies a threshold of 10% of maximum cornerness value
Method 2 (Block-based): Divides image into blocks and finds local maxima above a threshold


### Visualization:

Marks detected corners with green circles on the original image
Displays and saves the result for further analysis



Author
Dimitri Montgomery
