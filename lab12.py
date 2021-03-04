#Steven Cisneros
#Professor Nguyen
#CIS 103-20324-LEC
#30 April 2020

def main():
    print("F","\t","              C")
    for x in range(11):
        celsius_temp = f_to_c(x*10)
        print (x*10, "\t\t", "{:.2f}".format(celsius_temp))

def f_to_c(tempF):
    tempC = (5/9) * (tempF - 32)
    return tempC
main()
