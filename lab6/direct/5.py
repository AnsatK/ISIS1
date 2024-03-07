def list_to_txt(path, lst):
    with open(path, 'w') as file:
        for i in lst:
            file.write(str(i)+'\n')

my_list = [1, "sssd", 3, "sasasa"]
list_to_txt('sa.txt', my_list)
