def spam1():

    def spam2():

        def spam3():
            z = " Even"
            z += y
            print("In spam3 locals are {} ".format(locals()))
            return z

        y = " More" + x  # y must exist before spam3 is called
        y += spam3()  # Do not combine these assignments
        print("In spam2 locals are {} ".format(locals()))
        return y

    x = " Spam!"  # x must exist before spam2 is called
    x += spam2()  # Do not combine these assignments
    print("In spam1 locals are {} ".format(locals()))
    return x

print(spam1())
print(locals())
print(globals())
