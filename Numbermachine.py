# Challenge 2
# Number machine

#reverse digit numbers
def reverse(digit_number):
    d_input = 0
    d_output = 0

    while (digit_number > 0):
        #the digit numbers between 0 and 10
        d_input = digit_number % 10
        digit_number = int(digit_number / 10)
        d_output = d_output * 10 + d_input

    return d_output

#generating new number by adding 1 to every digits in the sum
def gen_new(sum):
    while True:
        final = str(sum)
        #sum digits equal to 5
        if len(str(sum)) == 5:
            first = int(final[0])
            second = int(final[1])
            third = int(final[2])
            fourth = int(final[3])
            last = int(final[4])
            addition = str(first + 1) + "" + str(second + 1) + "" + str(third + 1) + "" + str(fourth + 1) + "" + str(
                last + 1)
            print("The new number after adding 1 to each digit =", addition)
            break
        #sum digits more than 5
        elif len(str(sum)) > 5:

            first = int(final[0])
            second = int(final[1])
            third = int(final[2])
            fourth = int(final[3])
            last = int(final[4])
            other = int(final[5])
            addition = str(first + 1) + "" + str(second + 1) + "" + str(third + 1) + "" + str(fourth + 1) + "" + str(
                last + 1) + "" + str(other + 1)
            print("The new number after adding 1 to each digit =", addition)
            break
        else:
            print("Catch-All Error")




while True:
    try:
        digit_number = int(input("Enter 5 digit number: "))
    except:
        print("You have entered an invalid input, please try again")
    else:
        if len(str(digit_number)) != 5:
           print("The length is not equal to 5, Please enter 5 digits")
        elif len(str(digit_number)) == 5:
            number = int(digit_number)
            rev = reverse(digit_number)
            print("Before the tranformation the digit number was : ", digit_number)
            print("Reverse number is: ", rev)

            sum = rev + digit_number
            sum = int(sum)
            print("The sum of the digit number:", rev, '+', digit_number, '=', sum)
            #calling the generating new num function
            gen_new(sum)

            break
        else:
            print("Catch-All Error")
