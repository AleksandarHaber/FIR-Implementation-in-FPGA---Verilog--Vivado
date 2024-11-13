'''
Title: FIR Filter Implementation in FPGAs

Author: Aleksandar Haber, PhD 

Description: This Python file is used to generate a noisy data sequence
and to convert numbers from a decimal to a binary representation. In addition, 
this file is used to plot the outputs of the FIR filter.

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

'''

import numpy as np
import matplotlib.pyplot as plt 

# this function is used to perform the transformation from a signed binary to 
# the signed decimal representation

def todecimal(x, bits):
    assert len(x) <= bits
    n = int(x, 2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s)
        

# compute a binary representation of the filter coefficients
# number of coefficients
tap=8
# for computing first scale, we want to represent filter coefficients 
# as 8 bit numbers
N1=8
# this is used to convert the filter inputs to 16-bit signed values
N2=16 
# this is the output bit width 
N3=32



real_coeff=(1/tap);

# bit representation of the coefficients
coeff_bit=np.binary_repr(int(real_coeff*(2**(N1-1))),N1)

# double check, invert, it should be equal to real_coeff
todecimal(coeff_bit, N1)/(2**(N1-1))

# generate a test sequence
timeVector=np.linspace(0,2*np.pi,100)

output=np.sin(2*timeVector)+np.cos(3*timeVector)+0.3*np.random.randn(len(timeVector))

plt.plot(output)
plt.show()

# convert to integers
# this list containst the N2-bit signed representation of the sin sequence
list1=[]
for number in output:
    list1.append(np.binary_repr(int(number*(2**(N1-1))),N2))

# save the converted sequence to the data file
with open('input.data', 'w') as file:
    for number in list1:
        file.write(number + '\n')  
        
# after this line, you need to run the Vivado code


# from here, we read the filtered values, convert them to decimal representation 
# and plot the filtered results
        
read_b=[]        
        
# read data
with open("save.data") as file: 
    for line in file:
        read_b.append(line.rstrip('\n'))

# this list contains the converted values
n_l=[]
for by in read_b:
    n_l.append(todecimal(by,N3)/(2**(2*(N1-1))))


# implementation of the FIR filter in Python
p_output=[]
samples=np.zeros(shape=(8,1))
for inputValue in output:
    samples[1:7,:]=samples[0:6,:]
    samples[0,0]=inputValue
    filteredOutput=0
    for i in range(8):
        filteredOutput=filteredOutput+(1/8)*samples[i,0]
        
    p_output.append(filteredOutput)    
    
p_output=np.array(p_output)  

# plot the data

plt.plot(output,color='blue',linewidth=3,label='Original signal')    
plt.plot(n_l,color='red',linewidth=3,label='Filtered signal FPGA')
plt.plot(p_output,color='black',linewidth=3,label='Filtered signal Python')
plt.legend()
plt.savefig('results.png',dpi=600)
plt.show()



