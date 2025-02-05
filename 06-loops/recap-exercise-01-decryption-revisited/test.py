import time
time.sleep(10)
import pytest

# import code from student.py
try:
    from student import decode5  # Import student's functions from student.py
except ImportError as e:
    pytest.fail(f"Import error: {str(e)}. Make sure the function 'decode5' is correctly defined in 'student.py'.")

# Test cases for decode5
@pytest.mark.parametrize("test_input,expected", [
    ("NBFOeWdu XfPAkkagtkzm CaxIkkrGaNprtOGYQszl fhmbdYeI YndYkdrUAVlLlqecnSZJQpxiklmJ ", "de kat krapt de krollen"),
    ("usXxnnaCvIBH aLabdxec VgklrGAXlnlOewnedAevYRQZHszQUUnk OOjErfAalbtzrNavpiGOPLAySDgd ", "van de rollende roltrap"),
    ("IaaqeCmsOHTb ALdkwFirlrlUeqmaxLCSKnbF eLStdGabnYsMtYQXLPWZ BfRAdhen RsZstqajneggAzZMxROm ", "Ome willem danst de tango"),
    ("HrBMeaiHnfnXifWMnWlMpQpI vFwJtIhaekUZ uqlepRAVAkhbDeBA TUAIauntdMJq eilDtlixgDewrSFLIiSg nKEHlVApvGeGeqJG xcLUcPlxiImsbIitntgAPSCAKKerHMXI wUpBtnraekeGsUNXAwiA ", "Winnie the pooh and tiger love climbing trees"),
    ("URfJsLiShzteJjkb wJQmiNsT bqEPaC BrqIcJrhaEpHpVyzKNNKqfjw lzkXszeLnmtsexnfcKediLzPPyCdUdtw ", "this is a crappy sentence"),
    ("bEAKsOeFcXnDaWtXsWmruqcfryizcaUcNQZNXgzscVUrvYhVsSxL UEgThhaavIevncab PXkZcuhuaanrgKegdySazGcarZGW ", "circumstances have changed"),
    ])

def test_decode5(test_input, expected):
    try:
        result = decode5(test_input).strip()
        assert result == expected, (
            f"Expected {expected} when decoding '{test_input}', but got '{result}'."
        )
    except Exception as e:
        pytest.fail(f"Error occurred when testing input '{test_input}' with decode5: {str(e)}")

