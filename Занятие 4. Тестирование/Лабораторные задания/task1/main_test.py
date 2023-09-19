import unittest
from main import FlashDrive, Lamp, LedLamp, IncandescentLamp


class TestFlashDrive(unittest.TestCase):
    def test_type_memory(self):
        with self.assertRaises(TypeError):
            FlashDrive("123")

    def test_value_memory(self):
        with self.assertRaises(ValueError):
            FlashDrive(-1)

    def test_type_occupied_space(self):
        with self.assertRaises(TypeError):
            FlashDrive(1024, "21")

    def test_value_occupied_space(self):
        with self.assertRaises(ValueError):
            FlashDrive(1024, -1)

    def test_occupied_space(self):
        fd = FlashDrive(1024, 128)
        fd.occupied_space += 128
        self.assertEqual(fd.occupied_space, 256)

    def test_empty_flash_drive(self):
        fd = FlashDrive(1024, 128)
        self.assertEqual(fd.is_empty_flash_drive(), False)
        fd.clear_flash_drive()
        self.assertEqual(fd.is_empty_flash_drive(), True)

    def test_add_file_to_flash(self):
        fd = FlashDrive(1024, 128)
        with self.assertRaises(TypeError):
            fd.add_file_to_flash_drive([1, 2, 3])
        with self.assertRaises(ValueError):
            fd.add_file_to_flash_drive(1024)
        fd.add_file_to_flash_drive(128)
        self.assertEqual(fd.occupied_space, 256)

    def test_more_free_memory(self):
        flash_1 = FlashDrive(1024, 515)
        flash_2 = FlashDrive(1024, 256)
        self.assertTrue(flash_2 == FlashDrive.more_free_memory(flash_1, flash_2))


class TestLamp(unittest.TestCase):
    def test_type_power(self):
        with self.assertRaises(TypeError):
            Lamp("123")

    def test_value_power(self):
        with self.assertRaises(ValueError):
            Lamp(-1)

    def test_type_light_flow(self):
        with self.assertRaises(TypeError):
            Lamp(1024, "21")

    def test_value_light_flow(self):
        with self.assertRaises(ValueError):
            Lamp(1024, -1)

    def test_power(self):
        lamp = Lamp(5)
        self.assertEqual(lamp.power, 5)

    def test_light_flow(self):
        lamp = Lamp(5, 250)
        self.assertEqual(lamp.light_flow, 250)

    def test_efficiency(self):
        lamp_1 = Lamp(10, 1000)
        self.assertEqual(lamp_1.efficiency(), 100)
        with self.assertRaises(ValueError):
            Lamp(20).efficiency()

    def test_calculate_energy(self):
        lamp = Lamp(5, 300)
        with self.assertRaises(TypeError):
            lamp.calculate_energy("123")
        self.assertEqual(lamp.calculate_energy(3), 0.015)


class TestLedLamp(unittest.TestCase):
    def test_type_color_temperature(self):
        with self.assertRaises(TypeError):
            LedLamp(5, "123")

    def test_value_color_temperature(self):
        with self.assertRaises(ValueError):
            LedLamp(5, -1)

    def test_repr_ledlamp(self):
        led_lamp = LedLamp(5, 4000, 300)
        self.assertEqual(repr(led_lamp), 'LedLamp(5, 4000, 300)')


class TestIncandescentLamp(unittest.TestCase):
    def test_change_filament(self):
        lamp = IncandescentLamp(5, 100)
        with self.assertRaises(TypeError):
            lamp.change_filament(123)
        lamp.change_filament("123")
        self.assertEqual(lamp.filament, "123")


if __name__ == '__main__':
    unittest.main()
