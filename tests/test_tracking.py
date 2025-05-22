import unittest
import tracking

class TestTracking(unittest.TestCase):
    def test_detect_courier_ups(self):
        self.assertEqual(tracking.detect_courier('1Z9999999999999999'), 'UPS')

    def test_fetch_status_known(self):
        info = tracking.fetch_status('1Z9999999999999999')
        self.assertIsNotNone(info)
        self.assertEqual(info.courier, 'UPS')
        self.assertEqual(info.status, 'Delivered')

    def test_fetch_status_unknown(self):
        info = tracking.fetch_status('000000000000')
        self.assertTrue(info is None or info.status == 'Unknown')

    def test_fetch_status_invalid(self):
        self.assertIsNone(tracking.fetch_status('invalid'))


if __name__ == '__main__':
    unittest.main()
