import time

def test_results_1_completes_as_expected():
    time.sleep(3)

    print("Result 1 has completed")

def test_results_2_completes_as_expected():
    time.sleep(2)

    print("Result 2 has completed")

def test_results2_3_completes_as_expected():
    time.sleep(3)

    print("Result 3 has completed")

def test_results_4_completes_as_expected():
    time.sleep(2)

    print("Result 4 has completed")

def test_results_5_completes_as_expected():
    time.sleep(2)

    print("Result 5 has completed")

# pytest -s -n5