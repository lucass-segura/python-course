# Son colecciones de datos ordenados y inmutables

message = "Hello World!"

print(message)
print(type(message))
print(len(message))
print(message[0])

print("!" in message)
print(message.index("!"))

# Tambien se puede usar el slice
message2 = message[::-1]
print(message2)