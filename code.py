def solution(C):
    stable_periods_counter = 0
    n_stable_periods = 0
    for i, item in enumerate(C):
        if i < len(C) - 2:
            velocity1 = C[i+1] - item
            velocity2 = C[i+2] - C[i+1]
            if velocity1 == velocity2:
                stable = True
                if stable:
                    n_stable_periods += 1
            else:
                n_stable_periods = 0

            def fibo_seq(n):
                if n <= 1:
                    return n
                else:
                    return fibo_seq(n - 1) + fibo_seq(n - 2)

            if n_stable_periods == 6:
                stable_periods_counter += 15
            elif n_stable_periods == 5:
                stable_periods_counter += 10
            else:
                for j in range(n_stable_periods):
                    stable_periods_counter += fibo_seq(j + 1)
    if stable_periods_counter > 1_000_000_000:
        return 1
    return stable_periods_counter


if __name__ == '__main__':
    meas_1 = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
    sol = solution(meas_1)
    print(sol)
