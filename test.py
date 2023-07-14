import requests
from flask_restful import fields, reqparse

BASE = 'http://127.0.0.1:5000/'

# response = requests.get(BASE +"hello")
# response2 = requests.post(BASE +"hello")
# print(response.json())
# print(response2.json())

dummy_data = [
    {"id": 0, "name": "Alice", "email": "allice@hh.pt", "note": "This customer is due to receive a gift card"},
    {"id": 1, "name": "Charlie", "email": "cc@ir.ie", "note": ""},
    {"id": 2, "name": "Darragh", "email": "darrage@ucc.ie", "note": ""},
    {"id": 3, "name": "Tina", "email": "Tina@travel.ir", "note": "Complained about size"}]

x = {"id": 4, "name": "Mario", "email": "Mario@gg.org", "note": "Hello, I am mario"}
y = {"id": 5, "name": "Abby", "email": "abby@klm.nl", "note": "Invalid Gift Card"}


def test():
    # Inserting 4 Dummy Customers above
    print("PUT (INSERT DATA)")
    for i, d in enumerate(dummy_data):
        res = requests.put(BASE + f"customers/{i}", json=d)  # use json attribute, or u will not json serializable error
        print(res.json())

    # Getting those 4 Customers
    print("\n GET (GET DATA) \n")
    for i in range(4):
        res2 = requests.get(BASE + f"customers/{i}")
        print(res2.json())

    # Updating Alice's email and her name
    print("\nPATCH (UPDATE DATA) \n")

    res3 = requests.patch(BASE + f"customers/0",
                          json={"email": "Alice@skydiving.ie", "note": "Alice has updated her email"})
    print(res3.json())
    res4 = requests.get(BASE + f"customers/0")
    print(res4.json())

    # Inserting more dummy data to delete
    print("\n Inserting data to delete \n")
    res5 = requests.put(BASE + "customers/4", json=x)
    res6 = requests.put(BASE + "customers/5", json=y)
    print(res5.json())
    print(res6.json())

    print("\n Final Data \n")
    for j in range(6):
        res7 = requests.get(BASE + f"customers/{j}")
        print(res7.json())

    # Deleting the dummy data
    print("\n DELETE (DELETE DATA) \n")
    requests.delete(BASE + f"customers/4")  # res 8
    requests.delete(BASE + f"customers/5")  # res 9

    print("\n Data After Deletion \n")
    for k in range(6):
        res10 = requests.get(BASE + f"customers/{k}")
        print(res10.json())

# Clears dummy data in the db thats left after running the test() , SO code can be re-run
def clear_this_data():
    for l in range(10):
        res11 = requests.delete(BASE + f"customers/{l}")


if __name__ == '__main__':
    test()  # run the script, see the requests in the FLASK Dev Server running on Commandline
    # clear_this_data()
