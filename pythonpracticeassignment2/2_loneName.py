def func():
    student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad","Samalla Akshay"]
    lone_name=filter(lambda x:len(x)>6,student_name_list)
    print(list(lone_name))
func()