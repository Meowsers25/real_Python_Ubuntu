def convert_celsius(temp):
    cel	=	(temp	-	32)	*	5/9
    return cel

def convert_fahrenheit(temp):
    far = temp	*	9/5	+	32
    return far

temp1 = 72
temp2 = 37
print(temp1, "degrees F is", convert_celsius(temp1), "C")
print(temp2, "degrees C is", convert_fahrenheit(temp2), "F")
