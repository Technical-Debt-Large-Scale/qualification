import os
from os import path
from pathlib import Path
from tabulate import tabulate

def create_markdown_table(my_df, my_path, my_file_name):
    file_path = my_path + '/' + my_file_name
    try:
        with open(file_path,'w', encoding='utf-8') as my_file:
            my_file.write( tabulate(my_df, tablefmt="pipe", headers="keys",  ) )
        print("Arquivo " + file_path + "  gerado com sucesso!")
    except Exception as e:
        print("Erro " + str(e)+ " ao tentar gerar o arquivo markdown! " + file_path)
        
def show_names(my_list):
    list_temp = list()
    for each in my_list:
        each = each.first_names + each.last_names
        each = ' '.join(each)
        list_temp.append(each)
    return list_temp
