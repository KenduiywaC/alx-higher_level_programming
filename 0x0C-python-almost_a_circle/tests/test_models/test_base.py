#!/usr/bin/python3
&quot;&quot;&quot;Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 108
    TestBase_save_to_file - line 154
    TestBase_from_json_string - line 232
    TestBase_create - line 286
    TestBase_load_from_file - line 338
    TestBase_save_to_file_csv - line 404
    TestBase_load_from_file_csv - line 482
&quot;&quot;&quot;
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing instantiation of the Base class.&quot;&quot;&quot;

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual(&quot;hello&quot;, Base(&quot;hello&quot;).id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({&quot;a&quot;: 1, &quot;b&quot;: 2}, Base({&quot;a&quot;: 1, &quot;b&quot;: 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing to_json_string method of Base class.&quot;&quot;&quot;

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual(&quot;[]&quot;, Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual(&quot;[]&quot;, Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing save_to_file method of Base class.&quot;&quot;&quot;

    @classmethod
    def tearDown(self):
        &quot;&quot;&quot;Delete any created files.&quot;&quot;&quot;
        try:
            os.remove(&quot;Rectangle.json&quot;)
        except IOError:
            pass
        try:
            os.remove(&quot;Square.json&quot;)
        except IOError:
            pass
        try:
            os.remove(&quot;Base.json&quot;)
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open(&quot;Rectangle.json&quot;, &quot;r&quot;) as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open(&quot;Rectangle.json&quot;, &quot;r&quot;) as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open(&quot;Square.json&quot;, &quot;r&quot;) as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open(&quot;Square.json&quot;, &quot;r&quot;) as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open(&quot;Base.json&quot;, &quot;r&quot;) as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open(&quot;Square.json&quot;, &quot;r&quot;) as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open(&quot;Square.json&quot;, &quot;r&quot;) as f:
            self.assertEqual(&quot;[]&quot;, f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open(&quot;Square.json&quot;, &quot;r&quot;) as f:
            self.assertEqual(&quot;[]&quot;, f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing from_json_string method of Base class.&quot;&quot;&quot;

    def test_from_json_string_type(self):
        list_input = [{&quot;id&quot;: 89, &quot;width&quot;: 10, &quot;height&quot;: 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{&quot;id&quot;: 89, &quot;width&quot;: 10, &quot;height&quot;: 4, &quot;x&quot;: 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {&quot;id&quot;: 89, &quot;width&quot;: 10, &quot;height&quot;: 4, &quot;x&quot;: 7, &quot;y&quot;: 8},
            {&quot;id&quot;: 98, &quot;width&quot;: 5, &quot;height&quot;: 2, &quot;x&quot;: 1, &quot;y&quot;: 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{&quot;id&quot;: 89, &quot;size&quot;: 10, &quot;height&quot;: 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {&quot;id&quot;: 89, &quot;size&quot;: 10, &quot;height&quot;: 4},
            {&quot;id&quot;: 7, &quot;size&quot;: 1, &quot;height&quot;: 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string(&quot;[]&quot;))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing create method of Base class.&quot;&quot;&quot;

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(&quot;[Rectangle] (7) 1/2 - 3/5&quot;, str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(&quot;[Rectangle] (7) 1/2 - 3/5&quot;, str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(&quot;[Square] (7) 5/1 - 3&quot;, str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(&quot;[Square] (7) 5/1 - 3&quot;, str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing load_from_file_method of Base class.&quot;&quot;&quot;

    @classmethod
    def tearDown(self):
        &quot;&quot;&quot;Delete any created files.&quot;&quot;&quot;
        try:
            os.remove(&quot;Rectangle.json&quot;)
        except IOError:
            pass
        try:
            os.remove(&quot;Square.json&quot;)
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing save_to_file_csv method of Base class.&quot;&quot;&quot;

    @classmethod
    def tearDown(self):
        &quot;&quot;&quot;Delete any created files.&quot;&quot;&quot;
        try:
            os.remove(&quot;Rectangle.csv&quot;)
        except IOError:
            pass
        try:
            os.remove(&quot;Square.csv&quot;)
        except IOError:
            pass
        try:
            os.remove(&quot;Base.csv&quot;)
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open(&quot;Rectangle.csv&quot;, &quot;r&quot;) as f:
            self.assertTrue(&quot;5,10,7,2,8&quot;, f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open(&quot;Rectangle.csv&quot;, &quot;r&quot;) as f:
            self.assertTrue(&quot;5,10,7,2,8\n2,4,1,2,3&quot;, f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open(&quot;Square.csv&quot;, &quot;r&quot;) as f:
            self.assertTrue(&quot;8,10,7,2&quot;, f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open(&quot;Square.csv&quot;, &quot;r&quot;) as f:
            self.assertTrue(&quot;8,10,7,2\n3,8,1,2&quot;, f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open(&quot;Base.csv&quot;, &quot;r&quot;) as f:
            self.assertTrue(&quot;8,10,7,2&quot;, f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open(&quot;Square.csv&quot;, &quot;r&quot;) as f:
            self.assertTrue(&quot;8,10,7,2&quot;, f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open(&quot;Square.csv&quot;, &quot;r&quot;) as f:
            self.assertEqual(&quot;[]&quot;, f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open(&quot;Square.csv&quot;, &quot;r&quot;) as f:
            self.assertEqual(&quot;[]&quot;, f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    &quot;&quot;&quot;Unittests for testing load_from_file_csv method of Base class.&quot;&quot;&quot;

    @classmethod
    def tearDown(self):
        &quot;&quot;&quot;Delete any created files.&quot;&quot;&quot;
        try:
            os.remove(&quot;Rectangle.csv&quot;)
        except IOError:
            pass
        try:
            os.remove(&quot;Square.csv&quot;)
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == &quot;__main__&quot;:
    unittest.main()

Rewritten Content:
#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest training:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 108
    TestBase_save_to_file - line 154
    TestBase_from_json_string - line 232
    TestBase_create - line 286
    TestBase_load_from_file - line 338
    TestBase_save_to_file_csv - line 404
    TestBase_load_from_file_csv - line 482
"""
import os
import unittest
from models.base import Base
from fashions.rectangle import Rectangle
from fashions.rectangular import rectangular


elegance TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the bottom magnificence."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.identity, b2.identification - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.identity - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.identification, b2.identification - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.identity, b3.identification - 1)

    def test_id_public(self):
        b = Base(12)
        b.identity = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("howdy", Base("hey").id)

    def test_float_id(self):
        self.assertEqual(five.five, Base(five.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(five), Base(complicated(five)).identity)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).identity)

    def test_bool_id(self):
        self.assertEqual(true, Base(authentic).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).identification)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).identity)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, three})).identification)

    def test_range_id(self):
        self.assertEqual(variety(five), Base(variety(five)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').identity)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).identification)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(flow('inf'), Base(drift('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(go with the flow('nan'), Base(waft('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for trying out to_json_string approach of Base magnificence."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, eight, 6)
        self.assertEqual(str, kind(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, four, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = square(10, 2, 3, 4)
        self.assertEqual(str, kind(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = rectangular(10, 2, 3, four)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = rectangular(10, 2, 3, four)
        s2 = square(four, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


magnificence TestBase_save_to_file(unittest.TestCase):
    """Unittests for checking out save_to_file technique of Base elegance."""

    @classmethod
    def tearDown(self):
        """Delete any created documents."""
        try:
            os.take away("Rectangle.json")
        except IOError:
            skip
        attempt:
            os.dispose of("square.json")
        besides IOError:
            pass
        try:
            os.put off("Base.json")
        except IOError:
            bypass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, eight, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == fifty three)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, eight, five)
        r2 = Rectangle(2, four, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = square(10, 7, 2, eight)
        rectangular.save_to_file([s])
        with open("rectangular.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = rectangular(10, 7, 2, 8)
        s2 = rectangular(8, 1, 2, 3)
        rectangular.save_to_file([s1, s2])
        with open("rectangular.json", "r") as f:
            self.assertTrue(len(f.examine()) == seventy seven)

    def test_save_to_file_cls_name_for_filename(self):
        s = rectangular(10, 7, 2, eight)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.examine()) == 39)

    def test_save_to_file_overwrite(self):
        s = square(9, 2, 39, 2)
        rectangular.save_to_file([s])
        s = square(10, 7, 2, eight)
        square.save_to_file([s])
        with open("square.json", "r") as f:
            self.assertTrue(len(f.examine()) == 39)

    def test_save_to_file_None(self):
        rectangular.save_to_file(None)
        with open("square.json", "r") as f:
            self.assertEqual("[]", f.examine())

    def test_save_to_file_empty_list(self):
        square.save_to_file([])
        with open("square.json", "r") as f:
            self.assertEqual("[]", f.study())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(listing, kind(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = rectangular.to_json_string(list_input)
        list_output = square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = square.to_json_string(list_input)
        list_output = rectangular.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


elegance TestBase_create(unittest.TestCase):
    """Unittests for trying out create approach of Base elegance."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(three, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) half - three/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(three, five, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) half of - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(three, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = rectangular(3, five, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = rectangular.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - three", str(s1))

    def test_create_square_new(self):
        s1 = rectangular(3, five, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = rectangular.create(**s1_dictionary)
        self.assertEqual("[Square] (7) five/1 - three", str(s2))

    def test_create_square_is(self):
        s1 = square(3, five, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = rectangular.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = rectangular(three, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


magnificence TestBase_load_from_file(unittest.TestCase):
    """Unittests for checking out load_from_file_method of Base magnificence."""

    @classmethod
    def tearDown(self):
        """Delete any created documents."""
        try:
            os.take away("Rectangle.json")
        except IOError:
            bypass
        try:
            os.put off("square.json")
        besides IOError:
            bypass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, eight, 1)
        r2 = Rectangle(2, four, five, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, eight, 1)
        r2 = Rectangle(2, 4, five, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, eight, 1)
        r2 = Rectangle(2, four, five, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = square(five, 1, three, 3)
        s2 = square(nine, five, 2, three)
        rectangular.save_to_file([s1, s2])
        list_squares_output = square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = square(five, 1, 3, three)
        s2 = rectangular(nine, 5, 2, 3)
        rectangular.save_to_file([s1, s2])
        list_squares_output = square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = square(5, 1, three, 3)
        s2 = square(nine, 5, 2, 3)
        rectangular.save_to_file([s1, s2])
        output = rectangular.load_from_file()
        self.assertTrue(all(type(obj) == rectangular for obj in output))

    def test_load_from_file_no_file(self):
        output = rectangular.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


magnificence TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for checking out save_to_file_csv approach of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        attempt:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        strive:
            os.do away with("square.csv")
        except IOError:
            bypass
        strive:
            os.eliminate("Base.csv")
        besides IOError:
            skip

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, eight, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("five,10,7,2,8", f.study())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, eight, 5)
        r2 = Rectangle(2, four, 1, 2, three)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8n2,four,1,2,3", f.examine())

    def test_save_to_file_csv_one_square(self):
        s = square(10, 7, 2, eight)
        square.save_to_file_csv([s])
        with open("square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = rectangular(10, 7, 2, eight)
        s2 = square(eight, 1, 2, three)
        rectangular.save_to_file_csv([s1, s2])
        with open("square.csv", "r") as f:
            self.assertTrue("eight,10,7,2n3,8,1,2", f.study())

    def test_save_to_file__csv_cls_name(self):
        s = square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.study())

    def test_save_to_file_csv_overwrite(self):
        s = rectangular(nine, 2, 39, 2)
        square.save_to_file_csv([s])
        s = square(10, 7, 2, 8)
        square.save_to_file_csv([s])
        with open("rectangular.csv", "r") as f:
            self.assertTrue("eight,10,7,2", f.study())

    def test_save_to_file__csv_None(self):
        rectangular.save_to_file_csv(None)
        with open("square.csv", "r") as f:
            self.assertEqual("[]", f.examine())

    def test_save_to_file_csv_empty_list(self):
        square.save_to_file_csv([])
        with open("square.csv", "r") as f:
            self.assertEqual("[]", f.study())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            rectangular.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv approach of Base elegance."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        attempt:
            os.remove("Rectangle.csv")
        besides IOError:
            bypass
        attempt:
            os.cast off("square.csv")
        besides IOError:
            skip

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, four, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, five, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, four, five, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(kind(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = rectangular(five, 1, 3, three)
        s2 = rectangular(nine, 5, 2, 3)
        square.save_to_file_csv([s1, s2])
        list_squares_output = rectangular.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = square(5, 1, 3, three)
        s2 = rectangular(9, five, 2, three)
        rectangular.save_to_file_csv([s1, s2])
        list_squares_output = square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = square(5, 1, 3, 3)
        s2 = square(9, five, 2, three)
        rectangular.save_to_file_csv([s1, s2])
        output = square.load_from_file_csv()
        self.assertTrue(all(type(obj) == square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.important()

