import ast
import os

# all_file_path = [{'file_name': 'setup.py', 'file_path': 'C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab\\setup.py'}, {'file_name': 'environment.py', 'file_path': 'C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab\\importlab\\environment.py'}, {'file_name': 'fs.py', 'file_path': 'C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab\\importlab\\fs.py'}]

def get_imports(all_file_path):
    file_name_imports = []
    for file_info in all_file_path:
        file_path = file_info["file_path"]
        file_name_ = file_info["file_name"].replace(".py", "")
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    # imports.append(("import", alias.name, alias.asname))#import pandas as pd
                    file_name_imports.append({"file_name":file_name_,"imports":[alias.name]})
            elif isinstance(node, ast.ImportFrom):#from numpy import array as arr
                for alias in node.names:
                    # imports.append(("from", node.module, alias.name, alias.asname))
                    file_name_imports.append({"file_name":file_name_,"imports":[node.module,alias.name]})
    return file_name_imports

# print(get_imports(all_file_path))