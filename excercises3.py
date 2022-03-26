
    
        
 ###
#   #
#   #
#   #
#   #
#   #
 ###    
output_o = ""
for x in range (0,7):
    for y in range (0, 5):
        if (((y==0 or y==4) and x>0 and x<6) or ((x==0 or x==6)and y>0 and y<4)):
            output_o += '#'

        else:
            output_o += "_"
    output_o += "\n"

print (output_o)


result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
            result_str=result_str+"#"    
        else:      
            result_str=result_str+"_"    
    result_str=result_str+"\n"    
print(result_str);


