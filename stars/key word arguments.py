'''car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

y = car.items()
print(y)
'''
def bottle(**k):
    for key,value in k.items():
        print(f'{key}:{value}')
bottle(color="red",name="muni",capacity=1)
