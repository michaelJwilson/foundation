def calculate_pi(n: int) -> float:
    result = 0.0

    # Initialize denominator
    k = 1

    # Initialize sum
    for i in range(1_000_000):
        # even index elements are positive
        if i % 2 == 0:
            result += 4 / k
        else:
            # odd index elements are negative
            result -= 4 / k

    return round(result, n)


if __name__ == "__main__":
    calculate_pi(3)
