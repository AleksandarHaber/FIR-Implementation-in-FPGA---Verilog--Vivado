# FIR-Implementation-in-FPGA---Verilog--Vivado

![Filtered results](https://github.com/AleksandarHaber/FIR-Implementation-in-FPGA---Verilog--Vivado/blob/main/results.png)

![Filter diagram](https://github.com/AleksandarHaber/FIR-Implementation-in-FPGA---Verilog--Vivado/blob/main/drawing.png)

This repository contains Verilog, Vivado, and FPGA files that implement the Finite Impulse Response Filter (FIR Filter) in Verilog and Vivado.  

The YouTube tutorial explaining the posted files and how to implement the FIR filter in FPGAs is given here:  
https://www.youtube.com/watch?v=3NAnW3HShpY  

The webpage tutorial is given here:  
https://aleksandarhaber.com/finite-impulse-response-filter-fir-filter-implementation-in-verilog-fpga-and-vivado/

Explanation of the folders and files. There are two implementations of the FIR filter in Verilog. The folder FIR1 contains the first implementation. The folder FIR2 contains the second implementation. The difference between the first and the second implementations is that in the first implementation, the FIR filter equation is implemented inside of the always block. In the second implementation, the FIR filter is implemented outside of the always block by using a single assign statement. The second implementation is faster. 

In both FIR1 and FIR2 folders there are two files: 

- fir_filter.v - this file contains a Verilog module that implements the FIR filter
- testbench.v  - this file contains a Verilog testbench module that simulates the FIR filter

For more details, see the above tutorials. 

Then, in the base folder of this repository there is a Python file called "generate_show_data.py". This file is used to generate an input sequence for testing the FIR filter and for displaying the filtered outputs. Also, this file contains the Python implementation of the FIR filter. You need to run the first part of this file to generate the file called "input.data". This file contains a binary input sequence that is used to test the FIR filter. The Verilog testbench file "testbench.v" will generate the filtered data and save the data in the file called "save.data". This file is loaded by the file "generate_show_data.py" and results are plotted. 

