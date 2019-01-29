def with_default_parameters(number1=10,number2=10):
    if(number1!=number2):
        return(number1+number2)
    else:
        return(number1+number2)*2
print(with_default_parameters())
print(with_default_parameters(2))


