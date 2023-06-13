import pytest

from HW_19.codes.pixel_with_defects import Pixel


@pytest.fixture()
def setup():
    print("Start")
    pixel_correct = Pixel(112, 55, 25)
    return pixel_correct


class Test:

    @pytest.mark.parametrize("r, g, b", [
        (255, 255, 255),
        (25, 160, 100),
        (0, 0, 0)
    ])
    def test_with_valid_creds(self, r, g, b):
        pixel = Pixel(r, g, b)
        assert type(pixel) == Pixel

    @pytest.mark.parametrize("r, g, b", [
        (256, 256, 256),
        (-1, -1, -1),
        (300, 200, 25),
    ])
    @pytest.mark.xfail(raises=ValueError, reason="One of the Pixel components is not in range of [0, 255]")
    def test_with_incorrect_creds(self, r, g, b):
        with pytest.raises(ValueError):
            Pixel(r, g, b)

    @pytest.mark.parametrize("r, g, b", [
        ('q', 25, 35),
        (125, '@', '@'),
        ("255", "255", "25"),
    ])
    @pytest.mark.xfail(raises=TypeError, reason="One of the Pixel components is not integer")
    def test_with_incorrect_creds_with_str(self, r, g, b):
        with pytest.raises(TypeError):
            Pixel(r, g, b)

    @pytest.mark.parametrize("r, g, b", [
        (125.5, 50.5, 46.4),
        (200, 255, 150),
        (100, 50, 23)
    ])
    def test_check_property(self, r, g, b):
        pixel = Pixel(r, g, b)
        assert pixel.r == r
        assert pixel.g == g
        assert pixel.b == b

    @pytest.mark.parametrize("pixel_", [
        Pixel(180, 200, 254),
        Pixel(0, 0, 0)
    ])
    def test_check_add(self, setup, pixel_):
        result = setup.__add__(pixel_)
        for key, value in setup.__dict__.items():
            multiplication = value + pixel_.__dict__[key]
            if multiplication < 0:
                assert result.__dict__[key] == 0.0
            elif multiplication > 255:
                assert result.__dict__[key] == 255
            else:
                assert result.__dict__[key] == value + pixel_.__dict__[key]

    @pytest.mark.parametrize("pixel_", [
        Pixel(255, 255, 255),
        Pixel(12, 10, 9),
        Pixel(0, 0, 0)
    ])
    def test_check_sub(self, setup, pixel_):
        result = setup.__sub__(pixel_)
        for key, value in setup.__dict__.items():
            multiplication = value - pixel_.__dict__[key]
            if multiplication < 0:
                print("if multiplication < 0")
                assert result.__dict__[key] == 0.0
            elif multiplication > 255:
                print("if multiplication > 255")
                assert result.__dict__[key] == 255
            else:
                print("if multiplication ok")
                assert result.__dict__[key] == value - pixel_.__dict__[key]
            print(result.__dict__[key])

    @pytest.mark.parametrize("multiplicator", [
        1.5,
        25.8,
        100.8
    ])
    def test_check_multiplication_with_correct_creds(self, setup, multiplicator):
        result = setup.__mul__(multiplicator)
        for key, value in setup.__dict__.items():
            multiplication = value * multiplicator
            if multiplication < 0:
                print("if multiplication < 0")
                assert result.__dict__[key] == 0.0
            elif multiplication > 255:
                print("if multiplication > 255")
                assert result.__dict__[key] == 255
            else:
                print("if multiplication ok")
                assert result.__dict__[key] == int(value * multiplicator)
            print(result.__dict__[key])

    @pytest.mark.xfail(raises=TypeError, reason="Pixel could be multiplied only by int or float")
    def test_check_multiplication_with_str_creds(self, setup):
        with pytest.raises(TypeError) as error:
            setup.__mul__("25")
        assert "Pixel could be multiplied only by int or float" in str(error)

    @pytest.mark.xfail(raises=ZeroDivisionError, reason="Multiplicator should be greater than 0")
    def test_check_multiplication_with_0_value(self, setup):
        with pytest.raises(ZeroDivisionError) as error:
            setup.__mul__(0)
        assert "Multiplicator should be greater than 0" in str(error)

    @pytest.mark.xfail(raises=ValueError, reason="Multiplicator should be greater than 0")
    def test_check_multiplication_with_less_than_0(self, setup):
        with pytest.raises(ValueError) as error:
            setup.__mul__(-5)
        assert "Multiplicator should be greater than 0" in str(error)

    def test_check_rmul(self):
        pass

    @pytest.mark.parametrize("multiplicator", [
        1,
        20,
        50
    ])
    def test_check_truediv_with_correct_creds(self, setup, multiplicator):
        result = setup.__truediv__(multiplicator)
        for key, value in setup.__dict__.items():
            multiplication = int(value / multiplicator)
            if multiplication < 0:
                assert result.__dict__[key] == 0.0
            elif multiplication > 255:
                assert result.__dict__[key] == 255
            else:
                assert result.__dict__[key] == int(value / multiplicator)

    @pytest.mark.parametrize("value", [
        "-5",
        'q',
        "value"
    ])
    @pytest.mark.xfail(reason="Pixel could be multiplied only by int or float")
    def test_check_truediv_with_incorrect_value(self, setup, value):
        with pytest.raises(TypeError):
            setup.__truediv__(value)

    @pytest.mark.parametrize("value", [
        0,
        -5
    ])
    @pytest.mark.xfail(reason="Defect: need to add 'raise ZeroDivisionError'\nMultiplicator should be greater than 0")
    def test_check_truediv_with_0_value(self, setup, value):
        with pytest.raises((ZeroDivisionError, ValueError)):
            setup.__truediv__(value)

    def test_check_eq(self, setup):
        other_pixel = setup
        assert other_pixel.__eq__(setup)
        assert setup.__eq__(Pixel(112, 55, 25))

    def test_check_str(self, setup):
        result = setup.__str__()
        assert result.__eq__(f"Pixel object\n\tRed: {setup.r}\n\tGreen: {setup.g}\n\tBlue: {setup.b}\n")

    def test_check_repr(self, setup):
        result = setup.__repr__()
        for key, value in setup.__dict__.items():
            assert str(value) in result

    @pytest.mark.parametrize("area", [
        0, 1, 10, 200
    ])
    def test_check_get_pixel_near(self, setup, area):
        result = setup.get_pixel_near(area)
        print(result)
