
#User enters n, and then n elements of the list
#After entering elements of the list, show him options



#1) Print the entire list
#2) Add a new one to the list
#3) Average odd from the whole list
#4) The product of all elements that is divisible by 3 or by 4
#5) The largest element in the list
#6) The sum of those that is higher than the average of the whole list


# User choose an option and based on that option you print
n = int(input("Enter list lenth: "))
list_elements = []
for i in range(n):
    number = int(input("Enter number:"))
list_elements.append(number)
print(list_elements)
while True:

    print("""
    1) Print the entire list
    2) Add a new one to the list
    3) Average odd from the whole list
    4) The product of all elements that is divisible by 3 or by 4 
    5) The largest element in the list 
    6) The sum of those that is higher than the average of the whole list 


    0) Exit program

    """)

    option = int(input("Choose an option:"))
    if option == 0:
        print("End of the line")
        exit(1)
    elif option == 1:
        print(list_elements)

    elif option == 2:
        number = int(input("Enter new element to the list: "))
        list_elements.append(number)
    elif option == 3:
        sum = 0
        counter = 0
        lenth_list = len(list_elements)
        for i in range(lenth_list):
            if list_elements[i] % 2 != 0:
                sum = sum + list_elements[i]
                counter = counter + 1
                if counter != 0:
                    average = sum / counter
                    print(" Average odd from the whole list is {average}")
                else:
                    print("No odd elements")
    elif option == 4:
        product = 1
        for i in range(n):
            if list_elements[i] % 3 == 0 or list_elements[i] % 4 == 0:
                product = product * list_elements[i]
            print("Product is {product}")
    elif option == 5:
        maximum = list_elemens[0]
        for number in list_elements:
            if number > maximum:
                maximum = number
                print(maximum)
    elif option == 6:
        sum_higher = 0
        sum = 0
        for number in list_elements:
            sum += number
            average = sum / len(list_elements)
            for number in list_elements:
                if number > average:
                    sum_higher += number
                    print(sum_higher)
