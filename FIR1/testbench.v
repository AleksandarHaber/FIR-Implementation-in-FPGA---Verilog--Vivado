/*  Testbench file for testing 
    the first implementation of the FIR filter 
    Author: Aleksandar Haber

License: This code file and all the code files should not be used for commercial 
or research purposes. That is,you are not allowed to use this code if you work for 
a company, university, or any commercial or research institution without paying 
an appropriate fee. You are not allowed to use this code for teaching on 
online learning platforms and you are not allowed to use this code in official
university courses.

You are not allowed to publicly repost this code. You are not allowed to 
modify this code in any way. You are not allowed to integrate this code 
in any type of commercial or research projects. You are not allowed to 
use this code to generate scientific articles or reports. 
You are not allowed to use this code to train a large language model 
or any type of an AI algorithm.

DELIBERATE OR INDELIBERATE VIOLATIONS OF THIS LICENSE 
WILL INDUCE LEGAL ACTIONS AND LAWSUITS.

Contact information:
    
ml.mecheng@gmail.com


*/

`timescale 1ns / 1ps

module testbench;
// FIR coefficient word width
parameter N1=8;
// input data word width
parameter N2=16;
// output data word width
parameter N3=32;

// clock
reg CLK;
// reset for the FIR coefficient
reg RST;
// enable FIR coefficient
reg ENABLE;
// input data sample
reg [N2-1:0] input_data;
// this array stores all input samples from the file
reg [N2-1:0] data[99:0];
// output data
wire[N3-1:0] output_data;
// additional output for testing
wire [N2-1:0] sampleT;

// unit under test 
fir_filter UUT(.input_data(input_data),
               .output_data(output_data),
               .CLK(CLK),
               .RST(RST),
               .ENABLE(ENABLE),
               .sampleT(sampleT)
               );
// integer for the for loop
integer k;
// file for saving the filtered data
integer FILE1;
 
// clock has a period of 10 [ns]
always #10 CLK=~CLK;
 
initial 
begin 
    // set the input sample number
    k=0;
    // load the data samples and store them in the array called data
    $readmemb("input.data", data);
    
    // open the file for saving the filtered data
    FILE1=$fopen("save.data","w");
    
    // set the clock to zero
    CLK=0;
    #20 
    // reset the filter, this will set all the coefficients to zero
    RST=1'b1;
    #40 
    // here we enable the filter
    RST=1'b0;
    ENABLE=1'b1;
    input_data <= data[k];
    #10
    for (k = 1; k<100; k=k+1)
    begin
           @(posedge CLK);
           $fdisplay(FILE1,"%b",output_data);
           input_data <= data[k];
           if (k==99)
           $fclose(FILE1);
    end
end
endmodule
