string="ABDUL RAHMAN"
print("printing my name in * pattern.\nName: ABDUL RAHMAN")

############# START ##############
print()

#for A alphabet 
st="";    
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):
            st+="*"    
        else:      
            st+=" "    
    st+="\n"
print(st,"\n")

#for B alphabet
st="";
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 6))):
            st+="*"    
        else:      
            st+=" "    
    st += "\n"  
print(st,"\n");

#for D alphabet
st="";
for row in range(0,7):    
    for col in range(0,7):     
        if (col == 1 or ((row == 0 or row == 6) and (col > 1 and col < 5)) or (col == 5 and row != 0 and row != 6)):
            st+="*"    
        else:      
            st+=" "    
    st += "\n"  
print(st,"\n");

#for U alphabet
st="";
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 or col == 5) and row != 6) or (row == 6 and col > 1 and col < 5)):
            st+="*"    
        else:      
            st+=" "    
    st += "\n"  
print(st,"\n");

#for L alphabet
st="";
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 )) or (row == 6 and col > 1 and col < 6)):
            st+="*"    
        else:      
            st+=" "    
    st += "\n"  
print(st,"\n");


#for R alphabet
st="";
for row in range(0,7):    
    for col in range(0,7):     
        if (col == 1 or ((row == 0 or row == 3) and col > 1 and col < 5) or (col == 5 and row != 0 and row < 3) or (col == row - 1 and row > 2)):
            st+="*"    
        else:      
            st+=" "    
    st += "\n"  
print(st,"\n")

#for A alphabet 
st="";    
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):
            st+="*"    
        else:      
            st+=" "    
    st+="\n"
print(st,"\n")

#for H alphabet 
st="";    
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 or col == 5) ) or ((row == 3) and (col > 1 and col < 5))):
            st+="*"    
        else:      
            st+=" "    
    st+="\n"
print(st,"\n")

#for M alphabet 
st="";    
for row in range(0,7):    
    for col in range(0,7):     
        if (col == 1 or col == 5 or (row == 2 and (col == 2 or col == 4)) or (row == 3 and col == 3)):
            st+="*"    
        else:      
            st+=" "    
    st+="\n"
print(st,"\n")

#for A alphabet 
st="";    
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):
            st+="*"    
        else:      
            st+=" "    
    st+="\n"
print(st,"\n")

#for N alphabet 
st="";    
for row in range(0,7):    
    for col in range(0,7):     
        if (((col == 0 or col == 6) ) or ((row==col ))): 
            st+="*"    
        else:      
            st+=" "    
    st+="\n"
print(st,"\n")

###############  THE END #####################
