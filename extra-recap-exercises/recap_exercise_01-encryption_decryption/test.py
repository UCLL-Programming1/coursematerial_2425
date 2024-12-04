import pytest

# import code from student.py
try:
    from student import decode1, decode2, decode3, decode4, decode5  # Import student's functions from student.py
except ImportError as e:
    pytest.fail(f"Import error: {str(e)}. Make sure the functions 'decode1', 'decode2', 'decode3', 'decode4' and 'decode5' are correctly defined in 'student.py'.")

# Test cases decode1
@pytest.mark.parametrize("test_input,expected", [
    ("bear", "bear"),
    ("dAlphin", "dolphin"),
    ("mangA", "mango"),
    ("tarantula", "tarantula"),
    ("kippenhAk", "kippenhok"),
    ("dafalgan", "dafalgan"),
    ("nAArdpAol", "noordpool"),
    ("dAnutnAAtjes", "donutnootjes"),
])
def test_decode1(test_input, expected):
    try:
        result = decode1(test_input)
        assert result == expected, (
            f"Expected {expected} when decoding '{test_input}', but got '{result}'."
        )
    except Exception as e:
        pytest.fail(f"Error occurred when testing input '{test_input}' with decode1: {str(e)}")


# Test cases for decode2 
@pytest.mark.parametrize("test_input,expected", [
    ("bKeFakrC", "bear"),
    ("dfojlTpJhxianC", "dolphin"),
    ("mBalncgXoC", "mango"),
    ("tbaWrPaGnQtHuQlOaC", "tarantula"),
    ("kOiFpdpSeRnnhLoqkt", "kippenhok"),
    ("duadfpaGlZgqaSnu", "dafalgan"),
    ("nrozoArLdGpDoeovlK", "noordpool"),
    ("dAohnQuJtsnMohontUjIewsF", "donutnootjes"),
])
def test_decode2(test_input, expected):
    try:
        result = decode2(test_input)
        assert result == expected, (
            f"Expected {expected} when decoding '{test_input}', but got '{result}'."
        )
    except Exception as e:
        pytest.fail(f"Error occurred when testing input '{test_input}' with decode2: {str(e)}")


# Test cases for decode3
@pytest.mark.parametrize("test_input,expected", [
    ("ed kat krapt de krollen", "de kat krapt de krollen"),
    ("nav de rollende roltrap", "van de rollende roltrap"),
    ("emO willem danst de tango", "Ome willem danst de tango"),
    ("einniW the pooh and tiger love climbing trees", "Winnie the pooh and tiger love climbing trees"),
    ("siht is a crappy sentence", "this is a crappy sentence"),
    ("secnatsmucric have changed", "circumstances have changed"),
])
def test_decode3(test_input, expected):
    try:
        result = decode3(test_input)
        assert result == expected, (
            f"Expected {expected} when decoding '{test_input}', but got '{result}'."
        )
    except Exception as e:
        pytest.fail(f"Error occurred when testing input '{test_input}' with decode3: {str(e)}")


# Test cases for decode4
@pytest.mark.parametrize("test_input,expected", [
    ("ZEbearsS", "bear"),
    ("jxdolphinQLgjH", "dolphin"),
    ("NvmangoEdN", "mango"),
    ("IItarantulaeYpVGwK", "tarantula"),
    ("MjkippenhokDBAAbAp", "kippenhok"),
    ("sHdafalganXkZFFm", "dafalgan"),
    ("gonoordpoolPKcCrRF", "noordpool"),
    ("WWdonutnootjesqmETXQDBOg", "donutnootjes"),
])

def test_decode4(test_input, expected):
    try:
        result = decode4(test_input)
        assert result == expected, (
            f"Expected {expected} when decoding '{test_input}', but got '{result}'."
        )
    except Exception as e:
        pytest.fail(f"Error occurred when testing input '{test_input}' with decode4: {str(e)}")



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

