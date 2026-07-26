def greet(fx):
    # def mfx():
    #     print("Good Morning")
    #     fx()
    #     #result = fx(a, b)
    #     print("Thanks for using this function")
    #    # return result
    
    def  mfx(*args, **kwargs):
        print("Goog Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx

@greet
def hello():
    print("helo anku")

# greet(hello)()
hello()
@greet
def add(a, b):
    print( a + b)

add(6,6)
# greet(add)(3,4)