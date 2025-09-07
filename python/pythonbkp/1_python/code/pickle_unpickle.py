import pickle

# Sample data to be pickled
data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science', 'History']
}

# Pickling: Serialize the Python object (data) and save it to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
    print("Data has been pickled and saved to data.pkl.")

# Unpickling: Load the pickled data back into a Python object
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print("Data has been unpickled:")
    print(loaded_data)