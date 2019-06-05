domain = 'http://walshbr.com/'
pages = ['about', 'blog', 'pedagogy', 'projects', 'cv']

new_list=[]
for word in pages:
    new_pages = domain + word
    new_list.append(new_pages)

print(new_list)

#OR as a comprehension:

new_list_2=[domain + word for word in pages]
print(new_list_2)
    
