"""Exact rational identities for the three-point pseudo-Pick example."""

from fractions import Fraction
import json


def rational(numerator, denominator=1):
    return Fraction(numerator, denominator)


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def multiply(left, right):
    return [
        [sum(first * second for first, second in zip(row, column)) for column in transpose(right)]
        for row in left
    ]


def diagonal(entries):
    return [
        [entry if row_index == column_index else rational(0) for column_index in range(len(entries))]
        for row_index, entry in enumerate(entries)
    ]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** column * entry * determinant([
            row[:column] + row[column + 1:] for row in matrix[1:]
        ])
        for column, entry in enumerate(matrix[0])
    )


def factor_positive(matrix):
    size = len(matrix)
    lower = [[rational(row == column) for column in range(size)] for row in range(size)]
    pivots = []
    for column in range(size):
        pivot = matrix[column][column] - sum(lower[column][earlier] ** 2 * pivots[earlier] for earlier in range(column))
        assert pivot > 0
        pivots.append(pivot)
        for row in range(column + 1, size):
            lower[row][column] = (matrix[row][column] - sum(lower[row][earlier] * lower[column][earlier] * pivots[earlier] for earlier in range(column))) / pivot
    assert multiply(multiply(lower, diagonal(pivots)), transpose(lower)) == matrix
    return {'lower': lower, 'positive_diagonal': pivots}


def printable(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, list):
        return [printable(entry) for entry in value]
    if isinstance(value, dict):
        return {key: printable(entry) for key, entry in value.items()}
    return value


def main():
    coordinates = [rational(1, 10), rational(1), rational(2)]
    source_kernel = [[1 + first * second for second in coordinates] for first in coordinates]
    target_kernel = [
        [1 + (first ** 2 if row == column else 0) for column in range(3)]
        for row, first in enumerate(coordinates)
    ]
    quotient = [[target_kernel[row][column] / source_kernel[row][column] for column in range(3)] for row in range(3)]
    assert all(entry > 0 for row in source_kernel for entry in row)
    assert determinant(source_kernel) == 0
    assert determinant([row[:2] for row in source_kernel[:2]]) > 0
    assert all(coordinate ** 2 > 0 for coordinate in coordinates)
    assert determinant(target_kernel) > 0
    negative_vector = [rational(-2), rational(1), rational(1)]
    quadratic_form = multiply(multiply([negative_vector], quotient), transpose([negative_vector]))[0][0]
    assert quadratic_form == rational(-10, 33)
    relation = [rational(-10), rational(19), rational(-9)]
    weighted_relation = [coefficient * coordinate for coefficient, coordinate in zip(relation, coordinates)]
    assert sum(relation) == 0
    assert sum(weighted_relation) == 0
    assert weighted_relation == [rational(-1), rational(19), rational(-18)]
    assert multiply([relation], source_kernel) == [[0, 0, 0]]
    assert relation[1] * weighted_relation[2] - relation[2] * weighted_relation[1] != 0
    retractions = [[1, 1, 2], [0, 0, 2], [0, 1, 0]]
    lower_entries = [
        [rational(100, 101), rational(200, 303), rational(1, 153)],
        [rational(100, 101), rational(5, 6), rational(101, 12240)],
        [rational(10, 11), rational(100, 101), rational(110, 2121)],
    ]
    pivots = [
        [rational(101, 200), rational(51, 101), rational(358, 459)],
        [rational(1), rational(10200, 10201), rational(4487, 14688)],
        [rational(1), rational(21, 121), rational(850400, 214221)],
    ]
    retraction_results = []
    for omitted, (retraction, entries, positive_pivots) in enumerate(zip(retractions, lower_entries, pivots)):
        assert all(image != omitted for image in retraction)
        assert all(retraction[index] == index for index in range(3) if index != omitted)
        lower = [[rational(1), 0, 0], [entries[0], rational(1), 0], [entries[1], entries[2], rational(1)]]
        retraction_quotient = [
            [target_kernel[row][column] / source_kernel[retraction[row]][retraction[column]] for column in range(3)]
            for row in range(3)
        ]
        assert all(pivot > 0 for pivot in positive_pivots)
        assert multiply(multiply(lower, diagonal(positive_pivots)), transpose(lower)) == retraction_quotient
        retraction_results.append({
            'omitted_point': omitted,
            'retraction': retraction,
            'quotient': retraction_quotient,
            'lower_entries': entries,
            'positive_diagonal': positive_pivots,
        })
    forced_values = quotient[0]
    mixed_difference = [
        [target_kernel[row][column] - forced_values[row] * forced_values[column] * source_kernel[row][column] for column in range(3)]
        for row in range(3)
    ]
    assert mixed_difference[0] == [0, 0, 0]
    mixed_minor = determinant([row[1:] for row in mixed_difference[1:]])
    assert mixed_minor == rational(-791, 726)
    parameter = rational(1, 100)
    witness_coefficient = sum(entry ** 2 for entry in negative_vector)
    endpoint = -quadratic_form / witness_coefficient
    assert witness_coefficient == 6
    assert endpoint == rational(5, 99)
    perturbed_target = [
        [target_kernel[row][column] + (parameter * source_kernel[row][row] if row == column else 0) for column in range(3)]
        for row in range(3)
    ]
    perturbed_quotient = [
        [perturbed_target[row][column] / source_kernel[row][column] for column in range(3)]
        for row in range(3)
    ]
    assert all(perturbed_quotient[row][column] == quotient[row][column] + (parameter if row == column else 0) for row in range(3) for column in range(3))
    perturbed_form = multiply(multiply([negative_vector], perturbed_quotient), transpose([negative_vector]))[0][0]
    assert perturbed_form == quadratic_form + witness_coefficient * parameter < 0
    perturbed_retractions = []
    for retraction in retractions:
        retracted = [[perturbed_target[row][column] / source_kernel[retraction[row]][retraction[column]] for column in range(3)] for row in range(3)]
        perturbed_retractions.append(factor_positive(retracted))
    first_ratio, second_ratio = rational(10, 11), rational(5, 6)
    polynomial_constant = 10 * (first_ratio ** 2 + second_ratio ** 2) + 1
    assert polynomial_constant == rational(35303, 2178) < 20
    endpoint_shift = 1 + endpoint
    obstruction_endpoint = 10 * (endpoint_shift ** 2 - first_ratio ** 2) * (endpoint_shift ** 2 - second_ratio ** 2) - (endpoint_shift - 3 * first_ratio * second_ratio) ** 2
    assert obstruction_endpoint == rational(-34591631, 96059601)
    result = {
        'arithmetic': 'exact rational',
        'coordinates': coordinates,
        'source_kernel': source_kernel,
        'target_kernel': target_kernel,
        'source_rank': 2,
        'target_rank': 3,
        'quotient': quotient,
        'negative_vector': negative_vector,
        'negative_quadratic_form': quadratic_form,
        'source_relation': relation,
        'weighted_source_relation': weighted_relation,
        'retraction_factorizations': retraction_results,
        'mixed_multiplier_forced_values': forced_values,
        'mixed_multiplier_difference': mixed_difference,
        'mixed_multiplier_negative_minor': mixed_minor,
        'diagonal_family': {
            'parameter_interval': '0 <= t < 5/99; sufficient interval, not an optimal endpoint',
            'witness_linear_coefficient': witness_coefficient,
            'negative_witness_endpoint': endpoint,
            'interior_parameter': parameter,
            'interior_quotient': perturbed_quotient,
            'interior_negative_form': perturbed_form,
            'interior_target_factorization': factor_positive(perturbed_target),
            'interior_retraction_factorizations': perturbed_retractions,
            'complete_pick_polynomial_constant': polynomial_constant,
            'complete_pick_polynomial_at_endpoint': obstruction_endpoint,
        },
        'scope': 'Exact rational identities for the displayed kernels and a rational member of the diagonal family. Written proofs establish the real parameter interval, all interpolation sizes, repeated nodes, source-rank and point minimality, and the complete Pick, BLH, pseudo-Leech and Agler obstructions.',
    }
    print(json.dumps(printable(result), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
