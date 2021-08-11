def compare_num_of_chars(string1):
  return len(string1)
word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort()
print(word_list)
# ['C', 'Python', 'better', 'is', 'than']
word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort(key=compare_num_of_chars)
print(word_list)
#['C', 'is', 'than', 'Python', 'better']

#sort the list by second element of each list 
lists1=[[1, 2, 3], [2, 1, 3], [4, 0, 1]]
lists2=sorted(lists1, key=lambda x: x[1])
print (lists2)

#[[4, 0, 1], [2, 1, 3], [1, 2, 3]]
