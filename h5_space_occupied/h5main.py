import os #necessary import

def file_counter(f):
    list_dir = []
    list_dir = os.listdir(f)
    count = 0
    for file in list_dir:
        if file.endswith(''):
            count += 1
    return count

def folder_size(f):
    total_size = os.path.getsize(f)
    for i in os.listdir(f):
        path = os.path.join(f, i)
        if os.path.isfile(path):
            total_size += os.path.getsize(path)
        else:
            if os.path.isdir(path):
              total_size += path
    return total_size

print("There is/are",file_counter('subfoldr'),"file in your dir. Size of files and folder in the chosen folder is:",
      folder_size('subfoldr'), "bytes")