def distinct_terms_count(a_min, a_max, b_min, b_max):
    distinct_terms = set()

    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            distinct_terms.add(a ** b)

    return len(distinct_terms)

result = distinct_terms_count(2, 100, 2, 100)
print(f"The number of distinct terms is: {result}")
