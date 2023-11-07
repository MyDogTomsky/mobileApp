import pytest
from Fourth4Page import FourthPage

def test_savedingred_allclean(capsys) :

    checking = FourthPage(app = None)

    checking.allergyIngred = []

    checking.goingSubmit(None)
    decidedData = capsys.readouterr()

    assert decidedData.out == "Everything is OKAY for me!\n"

def test_savedingred_some(capsys):

    checking = FourthPage(app = None) 
    checking.allergyIngred = ['wheat','Lamb']

    checking.goingSubmit(None)
    decidedData = capsys.readouterr()

    assert decidedData.out == ("allergy :  "+"," .join(checking.allergyIngred)+"\n")
