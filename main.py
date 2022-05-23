import numpy as np


def min_mse(values):

    mse_min_all = 100
    mse_min_value = 0

    for delta in np.arange(0, 2, 0.1):
        quants = [delta * k for k in range(-5, 5)]
        mse_total = 0

        # Licz MSE dla wartości
        for i in values:
            mse_min = 100

            # Licz min MSE dla próbki
            for j in quants:
                mse_local = (i - j) ** 2
                if mse_local < mse_min:
                    mse_min = mse_local
            mse_total += mse_min

        print(mse_total)
        print(delta, "\n")

        if mse_total < mse_min_all:
            mse_min_all = mse_total
            mse_min_value = delta

    return mse_min_all, mse_min_value


if __name__ == '__main__':
    # USER INPUTS
    input_values = [1.1, 3.2, -5.5, 4.2, -5.5, 0, -0.7]

    # FUNCTION
    result_index, result_value = min_mse(input_values)

    # RESULT
    print("\n### RESULTS ###\n")
    print(result_index)
    print(result_value)
