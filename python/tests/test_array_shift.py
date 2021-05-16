from code_challenges.arrayShift.array_shift import insertShiftArray



def test_insert_shift_Array(test_list=[1,2,3,5,6] ,value=4):
    expected=[1,2,3,4,5,6]
    actual=insertShiftArray(test_list,len(test_list),value)
    assert expected==actual



