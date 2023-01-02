'''
No: 1251
Tier: sliver 5
Name: 단어나누기 
Language:Python3
'''

#Code


usr_string = input()
string_length = len(usr_string)
reverse_string = ""
dictionary_list = []
for a in range(1, string_length - 1): #ex) string_length = 8, 0<= a <= 6) 
	for b in range(a+1, string_length): #ex) string_length = 8, 1<= b <= 7-a

		first_char = usr_string[0:a] #set range
		second_char = usr_string[a:b]
		third_char = usr_string[b:string_length]

		reverse_string += first_char[::-1] #using silce(string reverse) 
		reverse_string += second_char[::-1]
		reverse_string += third_char[::-1]
		dictionary_list.append(reverse_string) # append maked_string
		reverse_string = "" #reset
 
dictionary_list.sort() # sort 
print(dictionary_list[0])


