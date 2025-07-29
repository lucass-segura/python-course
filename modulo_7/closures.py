def multiply(n1): # Local
    def operation(n2):
        return n1 * n2
    
    return operation

func_operation = multiply(10)
print('>>> El resultado es:', func_operation(5))