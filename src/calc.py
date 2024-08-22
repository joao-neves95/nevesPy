def fractional_part(decimal: float) -> float:
    '''
    e.g: fractional_part(2.05) = 0.05
    '''
    return decimal % 1


def convert_to_percentage_of_total(value: float, total: float) -> float:
    """
    E.g.: convert_to_percentage_of_total(105.55, 149.94) = 70.39482459650527
    E.g.: convert_to_percentage_of_total(33.4, 149.94) = 22.275576897425637
    """
    return (value * 100) / total
