def dep_search(file_to_check, files_inform,visited=None,tupled_dependencies=None):
    if visited is None:
        visited = set()
    dependencies = set()
    if tupled_dependencies is None:
        tupled_dependencies = []
    visited.add(file_to_check)
    for file_info in files_inform:
        file_to_check = file_to_check.replace(".py","")
        if file_to_check in file_info['imports']:
            dependencies.add(file_info['file_name'])  # Direct dependency
    result = [(file_to_check, item) for item in dependencies]#creating a list of tuple
    tupled_dependencies.extend(result)
    
    # Indirect dependency  
    for imp_file in list(dependencies):
        if imp_file not in visited:
            new_dependencies, new_tupled_dependencies = dep_search(imp_file, files_inform, visited, tupled_dependencies)
            dependencies.update(new_dependencies)#here we updating the dependencies only. 
    return list(dependencies),tupled_dependencies