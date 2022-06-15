# Diffractive_Optics_on_Python
Make python implementation of diffractive elements on Python. Implementing all code according to MatLab code from here:

_Book_: **Shanti Bhattacharya and Anand Vijayakumar. Design and fabrication of diffractive optical elements with MATLAB, 2017**

_In addition, making some exercises from book_

## Assumption
1. The amplitude and phase values are assigned assuming the size of each pixel to be 1 &mu;m.

## Abbreviation:

**DOE** - Diffractive Optical Element
**FZP** - Fresnel Zone Plate
**SPP** - Spiral Phase Plate
**IFTA** - Iterative Fourier Transform Algorithm

## CAUTION!
1. Equivalent of function rem() in MATLAB is np.fmod(). NOT np.remainder() - different behavior with negative numbers. For positive everything OK.
2. Initialize amplitude array as array of complex number. If not plotting don't see phase changes in complex form. 
