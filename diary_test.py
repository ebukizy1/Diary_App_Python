import unittest
import diary
from diary_project.entry import Entry


class diary_test(unittest.TestCase):

    def test_diary_can_exist(self):
        my_diary = diary.Diary
        self.assertIsNotNone(my_diary)

    def test_diary_can_be_lock(self):
        my_diary = diary.Diary("emmanuel", "password")
        self.assertTrue(my_diary.isLocked())

    def test_diary_can_be_unlocked(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.unlock("password")
        self.assertFalse(my_diary.isLocked())

    def test_diary_cannot_be_unlock_with_wrong_pin(self):
        my_diary = diary.Diary("emmanuel", "password")
        self.assertRaises(Exception, my_diary.unlock,  "passwo332rd")

    def test_diary_create_entry(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.create_entry("title", "body")
        self.assertEqual(1, my_diary.check_size_of_list())

    def test_diary_can_add_twice_the_entry(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.create_entry("title", "body")
        my_diary.create_entry("title", "body")
        self.assertEqual(2, my_diary.check_size_of_list())

    def test_diary_can_be_deleted_by_ID(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.create_entry("title", "body")
        my_diary.create_entry("title", "body")
        self.assertEqual(2, my_diary.check_size_of_list())
        my_diary.delete_entry("002")
        self.assertEqual(1, my_diary.check_size_of_list())

    def test_diary_cannot_be_deleted_by_wrong_ID(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.create_entry("title", "body")
        my_diary.create_entry("title", "body")
        self.assertEqual(2, my_diary.check_size_of_list())
        self.assertRaises(Exception,  my_diary.delete_entry,  "0021")

    def test_diary_can_find_entry(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.create_entry("title", "body")
        my_diary.create_entry("title", "body")
        self.assertEqual(2, my_diary.check_size_of_list())
        entry = my_diary.find_entry("002")
        self.assertEqual(" TITLE : title BODY  : body ", entry.__str__())

    def test_diary_can_update_entry(self):
        my_diary = diary.Diary("emmanuel", "password")
        my_diary.create_entry("title", "body")
        my_diary.create_entry("title", "body")
        my_diary.updateEntry("001", "title", "i love jesus")
        entry = my_diary.find_entry("001")
        self.assertEqual(  "i love jesus",   entry.entry_body)


















