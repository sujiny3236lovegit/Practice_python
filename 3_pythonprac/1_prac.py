a_dict = {'name': 'sujin', 'age': 31}
a_dict['height'] = 166

print(a_dict)


# -----------------------------------------------

def sum(num1, num2):
    print('안녕')
    return num1 + num2


result = sum(2, 3)
print(result)


# -----------------------------------------------

def is_adult(age):
    if age > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')


is_adult(30)
is_adult(17)

# -----------------------------------------------

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for f in fruits:
    if f == '배':
        count += 1

print(count)

# -----------------------------------------------

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    # print(person['name'], person['age'])
    if person['age'] < 20:
        print(person['name'], person['age'])
