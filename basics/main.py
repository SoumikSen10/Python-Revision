# Internal working of python

"""

Raw python code -------> Byte code(mostly hidden) -------> [Python Virtual Machine] (Virtual Machine)

  
   Compile to Byte Code
   - low level and platform independent
   
   Byte Code runs faster
   - .pyc --> compiled python (frozen binaries)
   __pycache__  
   
   Source Change and Python Version
      
      hello_chai.cpython-312.pyc
      
      --> works only for imported files
      --> not for top level files

   -> Python Virtual Machine PVM
   -> Code loop to iterate byte code
   -> Run time engine
   -> Also known as python interpreter
   
   Byte Code is not machine code
   
   -> Python specific interpretation
   -> cpython (standard implementation), jython, Iron Python, Stackless, PyPy
    

"""