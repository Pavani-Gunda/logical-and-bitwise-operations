# logical operators and bitwise operators
#logical operators-- and, or, and not

#truthy values--- all numbers expect 0,
#all strings expect empty string
#truth is truthy value
#false is not truthy value
#none is falsy value


#and gate--
#operands depends on second operand, third one etc.
print(True and True) #true
print(True and False) #false
print(False and True) #false
print(True and "") #empty string
print(True and(True and False)) #false
print(False and (True and False)) #false
print(False and (False and False)) #false
print(True and(True and True)) #true
print(False and (True and True)) #false
print(True and(False and False)) #false
print(2 and 3) #3
print( 3 and 0) #0
print( 4 and "") # ""
print("" and 0) #""
print(0 and "") #""
print(0 and "")#""
print("" and "")#""
print(None and "") #none
print(None and 0)#none
print(0 and None) #0
#or gate

print(2 or 3) #2
print(True or False) #true
print(False or True) #true
print(True or True) #true
print(False  or False) #false
print(False and (True or False)) #false
print(True or (False or False)) #false
print(False or (True and True)) #true
print(0 or "") #""
print(""or"") #""
print(0 or 0) #0
print(0 or True) #true
print(0 or 0 or 1)#1


#not operator
print(not True)
print(not False)
print(not(2 or 3))
print(not("" and 3))


#bitwise operators --- &, ^, ~, >>, <<, |

print(2 &3) 
print(bin(2)) #b10
print(bin(3)) #0b11
#0b10 & 0b11--- 0b10 -- 2

print(15 & 16) #0
print(bin(15)) #1111

print(bin(16)) #10000
 #15 &16 --- 1111 &10000---- 00000 --0

 #bitwise  --- or |
print(12|14)  #1100| 1110==== >  1110- 14


#xor opeartors -^
print(12^14) 
print(15^16) 


#leftshifts
#right shifts
print(3>>1)  
print(2<<1) 
print(29>>1)
print(23<<1)

#~-
print(~177) #-178
print(~134)#-135