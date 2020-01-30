import unittest
from store import Store


class TestDataStore(unittest.TestCase):

    def setUp(self):
        self.store = Store()

    def test_add_message(self):
        a_message = "يولد جميع الناس أحرارًا متساوين في الكرامة والحقوق"
        e_message = 'this is a message'
        j_message = 'ｲんﾉ丂　ﾉ丂　ﾑ　ﾶ乇丂丂ﾑム乇'

        self.store.put(a_message)
        self.store.put(e_message)
        self.store.put(j_message)
        ms = self.store.get()
        self.assertEqual(ms[-3], a_message)
        self.assertEqual(ms[-2], e_message)
        self.assertEqual(ms[-1], j_message)

    def test_max_records(self):
        """
            ensure only most recent
            x records are returned
            where x is set in constants as MAX_RECORDS
            in this test, we send 100 messages to the store
            then we get messages back from store
            the store should always return the last MAX_RECORDS messages, say 5.
            then we compare the last n messages to those returning from store
        """
        from constants import MAX_RECORDS
        messages = [f'message number: {str(i)}' for i in range(1, 100)]
        for index, message in enumerate(messages, 1):
            self.store.put(message)
            if index >= MAX_RECORDS:
                store_messages = self.store.get()
                msg = messages[index - MAX_RECORDS:index]
                self.assertListEqual(store_messages, msg)


if __name__ == '__main__':
    unittest.main()
