# FPU Profiling

The purpose of this simulation is to assess how FP multiplications compare against FP additions in terms of CPU time. 

The results showed that FP adds are actually more time-consuming than multiplications on an Intel i5 CPU using a Python script.

This is likely related to the FP add algorithm, which has a preprocessing step where the exponents of both operands are aligned.
