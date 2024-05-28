a=10.6
#print(type(a))
c=10+90j
#print(type(c))
#a=30
#b=float(a)
#print(b)
#c=complex(a)
#print(type(a))
a=97+5j
#c=int(b)
#b=complex(a)
#b=int(a)
#print(a)

#string to integer
'''
a="305"
b=int(a)
print(b)
print(type(b))'''



'''print("8","7","10",sep="&")'''

'''print("hiii","good","mrng",sep="hello")'''

'''print("hiii","good","mrng",sep=" ")'''

'''
print("welcome",end=" ")
print("irfan")'''

 # print("10","05","2001",sep="-")

 
#ticket task
'''
Tickets=int(input("No.Of Tickets:"))
if Tickets==6:
     print("weekdays->20 rs charge")
     print("weekend->50 rs charge")

age=int(input("Enter Your Age:"))
if age<18:
    if date=="weekdays":
        total=(150*6)+20
        print(total)
    elif date=="weekend":
        total=(150*6)+50
        print(total)
elif age>=18:
    date=str(input("enter date="))
    if date=="weekdays":
        total=(200*6)+20
        print(total)
    elif date=="weekend":
        total=(200*6)+50
        print(total)'''

                   



'''
print("ELECTRICITY BILL COUNTER\n")

unit=int(input("Enter the unit counts:"))
if unit>=50:
          total=(unit*3)+10
          print("total:", total)
elif unit>=100:
          total=(unit*7)+15
          print("total:", total)
elif unit>=200:
          total=(unit*11)+20
          print("total:", total) '''
'''

#dictionary task

data = {
    (1, 'madan'): {'manager': {800, 'chennai'}},
    (2, 'sam'): {'ceo': {500, 'goa'}},
    (3, 'john'): {'manager': {400, 'mumbai'}},
    (4, 'cherry'): {'hr': {350, 'chennai'}},
    (5, 'ram'): {'hr': {100, 'goa'}}
}

# Find the maximum value within the 'manager' keys
max_value = max(max(inner_dict.get('manager', {0})) for inner_dict in data.values())

print(f"The maximum value within the 'manager' keys is: {max_value}")'''


         #task
'''

dict_list = {
    (1, 'madhan'): {'manager': (800, 'chennai')},
    (2, 'sam'): {'ceo': (700, 'goa')},
    (3, 'john'): {'manager': (650, 'mumbai')},
    (4, 'cherry'): {'hr': (450, 'chennai')},
    (5, 'ram'): {'hr': (250, 'goa')}
}

max_value = float('-inf')
max_key = None

for key, value in dict_list.items():
    for sub_dict in value.values():
        if sub_dict[0] > max_value:
            max_value = sub_dict[0]
            max_key = key

print("Maximum value:", max_value)
print("Key with maximum value:", max_key)
print("Dictionary with maximum value:", dict_list[max_key])'''




#task
'''
print("#staff:")
n = int(input('No.of patients:'))


patients_data = {}


for i in range(1, n+1):
    id = int(input('Enter the id: '))
    name = input('Enter the patient name: ')
    disease = input('Enter the disease name: ')
    dob = input('Enter DOB: ')
    patients_data[id] = {'Name': name, 'Disease': disease, 'DOB': dob}
    print("Registration successfully")


edit = int(input("Enter 1 to edit patient data, 0 to exit: "))


if edit == 1:
    patient_id = int(input("Enter the patient ID to edit: "))
    if patient_id in patients_data:
        print("Current Patient Data:")
        print("ID:", patient_id)
        print("Name:", patients_data[patient_id]['Name'])
        print("Disease:", patients_data[patient_id]['Disease'])
        print("DOB:", patients_data[patient_id]['DOB'])
        
        
        new_name = input("Enter new name: ")
        new_disease = input("Enter new disease: ")
        new_dob = input("Enter new DOB: ")

        
        patients_data[patient_id]['Name'] = new_name
        patients_data[patient_id]['Disease'] = new_disease
        patients_data[patient_id]['DOB'] = new_dob

        print("Patient data edited successfully!")
    else:
        print("Invalid patient ID. Edit operation failed.")
else:
    print("Exiting the program.")'''





#task.
'''
def manager():
    n=int(input('no.of books:'))

    book_details={}
    
    for i in range(1,n+1):
        book_name=input('enter the book_name:')
        Author_name=input('enter the Author_name:')
        rate=int(input('enter the amount:'))
        publish_year=int(input('enter the year of published:'))

        book_details={'book_name':book_name, 'Author_name':Author_name, 'rate':rate, 'publish_year':publish_year}
    while(True):
        print('successfully registered.')
        break

manager()


def customer():
    book_name=input('Enter the book name:')

customer() '''


'''

def manager():
    n = int(input('Number of books:'))
    book_details = []

    for i in range(1, n+1):
        book_name = input('Enter the book name:')
        author_name = input('Enter the author name:')
        rate = int(input('Enter the amount:'))
        publish_year = int(input('Enter the year of publication:'))

        
        book_details.append({'book_name': book_name,'author_name':author_name,'rate':rate,'publish_year': publish_year})

    print('Successfully registered.')
    return book_details

def customer(book_details):
    book_name_input = input('Enter the book name to search:')

    found_books = []

    
    for book in book_details:
        if book['book_name'] == book_name_input:
            found_books.append(book)

    
    for found_book in found_books:
        print('Author:', found_book['author_name'])
        print('Publishing Year:', found_book['publish_year'])
        

book_details = manager()

customer(book_details)'''





#interviewed sir  
'''
a = [1, 2, 3, 4, 5]
b = [x**2 for x in a]
print(b)'''

#without using / find even and odd.

'''
for i in range(1+1,11,2):
    print(i)'''
    
'''
for j in range(-1+2,11,2):
    print(j)  '''  


#factorial num:

'''

i=int(input('enter a num:'))
fact=1
while i>0:
    fact=fact*i
    i=i-1
print(fact)  '''




#vowels finding program:

'''
word= input("enter the word:")

def vowels():
    vowels="aeiouAEIOU"
    vowel_list=[char for char in word if char in vowels]

    if vowel_list:
        print(vowel_list)
    else:
        print('there is no vowels word')

                 
vowels()   '''     



#polindrome:

'''
a=input('enter the words:')
b=a[::-1]
if a==b:
    print('polindrome')
else:
    print('not a polindrome')'''



#to reverse a string :
'''
a=input('enter the words:')
b=a[::-1]
print(b)  '''



#to check the count in string
'''
word=input("enter the word:")
s = len(word)

print(f"The length of the string is: {s}")   '''



#converting integer to decimal
'''
integer_value =int(input("enter a number:"))
decimal_value = float(integer_value)

print(f"Integer: {integer_value}")
print(f"Decimal: {decimal_value}")'''




# one of the asked this question during interview:

''' #question
lst_A = ['H','E','L','L','O','C','A','R','E','S','O','F','T']
 
lst_B = ['O','C','A','F','S','T','R','E','O','E','L','H','L','D','X','Z']

# program:
common_elements=[]
for element in lst_A:
    if element in lst_B:
        common_elements.append(element)
print("common elements:",common_elements)   '''





        


    




