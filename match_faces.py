import face_recognition
import glob

from sqlalchemy import true
print("TESTasdf")

# get all the missing cases submitted by user  ie in known files
directory = "./resources/static/assets/uploads/"
missing_cases = glob.glob(directory+"known/*")

# get all the new cases submitted by user  ie in unknown files
new_cases = glob.glob(directory+"unknown/*")

known_cases = []
unknown_cases = []
for case in missing_cases: 
    load_image = face_recognition.load_image_file(case)
    load_encoding = face_recognition.face_encodings(load_image)[0]
    known_cases.append(load_encoding)

for case in new_cases:
    load_image = face_recognition.load_image_file(case)
    unknown_cases.append(face_recognition.face_encodings(load_image)[0])

data = []
print("*******************")
print(missing_cases)

for match in unknown_cases:
    results = face_recognition.compare_faces(known_cases,match)  
    print(results)                                                 
    known_index = [i for i, x in enumerate(results) if x]
    print(known_index)
    print('aaaaaaaaaa')
    print(type(missing_cases[0]))
        
    for idx in known_index:
        data.append(missing_cases[idx].split(directory+"unknown/")[0])
          
print(data)        

        


