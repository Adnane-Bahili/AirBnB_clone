#!/usr/bin/python3
"""defines unittests for "models/city.py"
Unittest classes:
    Test_City_instant
    Test_City_save
    Test_City_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class Test_City_instant(unittest.TestCase):
    """Unittests for testing the instantiation of the "City" class"""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_represent(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_unused_arg(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_kwargs_instantiation(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_no_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class Test_City_save(unittest.TestCase):
    """Unittests for testing "save" method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_arg_save(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_update_file(self):
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class Test_City_dict(unittest.TestCase):
    """Unittests for testing "to_dict" method"""

    def test_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_dict_correct_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_dict_added_attributes(self):
        cy = City()
        cy.middle_name = "ALX"
        cy.my_number = 98
        self.assertEqual("ALX", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_dict_datetime_attributes_strs(self):
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_dict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_dict_contrast(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_dict_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
