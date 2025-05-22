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


    def test_parse_tracking_numbers(self):
        text = '1Z9999999999999999\n9400110200881111111111,123456789012'
        numbers = tracking.parse_tracking_numbers(text)
        self.assertEqual(numbers, [
            '1Z9999999999999999',
            '9400110200881111111111',
            '123456789012'
        ])

    def test_get_courier_link(self):
        link = tracking.get_courier_link('UPS', '1Z9999999999999999')
        self.assertTrue('1Z9999999999999999' in link)



if __name__ == '__main__':
    unittest.main()
