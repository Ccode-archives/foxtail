# foxtail
A simple shell language made for Linux computers. It compiles to bash as it is typed.

# usage
Foxtail is made to work as fast as or a little slower than bash. To run run shelly.py






ls:```l```  
pwd:```cwd```  
echo stays the same between languages  
mkdir directory:```mdir directory```  
rm file:```rem file```  
rm -r file:```remdir file```  
touch file:```mf file```  
cat file:```read file```  
exit to end shell run  




# in action
The code below will delete file ```hi.txt``` and then remake it.
```
rem hi.txt
mf hi.txt
```

# needed modules (python3)
termcolor (```pip3 install termcolor```)
