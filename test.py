import sprints.py as s


def first_test():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [1.1,2.2,3.3,4.4,5.5,6.6]
    result = s.MyFunc(list1, list2)
    assert result[0] == (2+4+6+8+10) / 5, f"Should be {(2+4+6+8+10) / 5}"
    assert result[1] == 6.6, "Should be 6.6"

if __name__ == "__main__":
    first_test()
    print("Tests Passed")