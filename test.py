import requests, unittest

BASE = 'http://127.0.0.1:5000/'

dummy_data = [
    {"id": 0, "name": "Alice", "email": "allice@hh.pt", "note": "This customer is due to receive a gift card"},
    {"id": 1, "name": "Charlie", "email": "cc@ir.ie", "note": ""},
    {"id": 2, "name": "Darragh", "email": "darrage@ucc.ie", "note": ""},
    {"id": 3, "name": "Tina", "email": "Tina@travel.ir", "note": "Complained about size"}]

x = {"id": 4, "name": "Mario", "email": "Mario@gg.org", "note": "Hello, I am mario"}
y = {"id": 5, "name": "Abby", "email": "abby@klm.nl", "note": "Invalid Gift Card"}


class TestCustomerRestApi(unittest.TestCase):

    def test1_put(self):
        # Inserting 4 Dummy Customers above
        for i, d in enumerate(dummy_data):
            res = requests.put(BASE + f"customers/{i}",
                               json=d)  # use json attribute, or u will not json serializable error
            status_code = res.status_code
            if status_code != 201:
                self.assertEqual(status_code, 201)

    def test2_get(self):
        # Getting those 4 Customers
        for i in range(4):
            res2 = requests.get(BASE + f"customers/{i}")
            status_code = res2.status_code
            if status_code != 200:
                self.assertEqual(status_code, 200)

    def test3_patch(self):
        # Updating Alice's email and her name
        res3 = requests.patch(BASE + f"customers/0",
                              json={"email": "Alice@skydiving.ie", "note": "Alice has updated her email"})
        status_code = res3.status_code
        self.assertEqual(status_code, 200)
        # Res 4 deleted as it was unnecessary

    def test4_delete(self):
        # Inserting more dummy data to delete
        requests.put(BASE + "customers/4", json=x)  # res5
        requests.put(BASE + "customers/5", json=y)  # res6
        # Deleting the dummy data
        res8 = requests.delete(BASE + f"customers/4")  # res 8
        res9 = requests.delete(BASE + f"customers/5")  # res 9
        status_code_res8 = res8.status_code
        status_code_res9 = res9.status_code
        self.assertEqual(status_code_res8, 204)
        self.assertEqual(status_code_res9, 204)

    def test5_not_found(self):
        r = requests.get(BASE + f"customers/66")
        status_code = r.status_code
        self.assertEqual(status_code, 404)

    def test6_already_exist(self):
        r = requests.put(BASE + f"customers/1", json=x)
        status_code = r.status_code
        self.assertEqual(status_code, 409)

    def test7_delete_unavailable_data(self):
        r = requests.delete(BASE + f"customers/66")
        status_code = r.status_code
        self.assertEqual(status_code, 404)

    # Clears dummy data in the db thats left after running the test() , SO code can be re-run
    def test8_data_clear(self):
        for l in range(4):
            res11 = requests.delete(BASE + f"customers/{l}")
            status_code_res11 = res11.status_code
            if status_code_res11 != 204:
                self.assertEqual(status_code_res11, 204)


if __name__ == '__main__':
    unittest.main()
