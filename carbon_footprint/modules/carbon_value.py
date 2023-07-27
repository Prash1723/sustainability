

def electric_bill(x):
    """Calculates carbon mass for electricity consumption"""
    return x*105

def monthly_gas(x):
    """Calculates carbon emissions for gas bill"""
    return x*105

def oil_spent(x):
    """Calculates carbon emissions for oil"""
    return x*113

def fuel_spent(x):
    """Calculates carbon emissions for fuel spent"""
    return x*0.79

def misc_CF(x):
    """Number of members in the house"""
    if x == 1:
        cf = 14
    elif x == 2:
        cf = 12
    elif x == 3:
        cf = 10
    elif x == 4:
        cf = 8
    elif x == 5:
        cf = 6
    elif x == 6:
        cf = 4
    else:
        cf = 2

    return cf

def house_size(x):
    """Calculate carbon footprint based on size of home"""
    if x == 'large':
        cf = 10
    elif x == 'medium':
        cf = 7
    elif x == 'small':
        cf = 4
    else:
        cf = 2

    return cf

def diet(x):
    """Calculate carbon mass based on type of diet"""
    if x == 'daily':
        cf = 10
    elif x == 'few':
        cf = 8
    elif x == 'vegeterian':
        cf = 4
    elif x == 'vegan' or x == 'wild meat':
        cf = 2

    return cf

def machine(x):
    """Calculate carbon footprint based on machine runtime"""
    if x > 9:
        cf = 3
    elif x.between(4,9):
        cf = 2
    elif x.between(1,3):
        cf = 1
    else :
        cf = 0

    return cf

def new_items(x):
    """Calculate carbon footprint based on items bought each year"""
    if x > 7:
        cf = 10
    elif x.between(5,7):
        cf = 8
    elif x.between(3,5):
        cf = 6
    elif x < 3:
        cf = 4
    else:
        cf = 2

    return cf

def garbage_mass(x):
    """Calculate carbon footprint based on garbage produced"""
    if x == 4:
        cf = 50
    elif x == 3:
        cf = 40
    elif x == 2:
        cf == 30
    elif x == 1:
        cf == 20
    else:
        cf == 5

    return cf

def waste_recycle():
    """Add carbon mass based on waste recycled"""
    if x = 0:
        cf = 24
    else:
        cf = 20

    return cf

def public_transport():
    """Add carbon mass for public transportation usage"""
    if x>32400:
        cf = 12
    elif x.between(24300,32400):
        cf = 10
    elif x.between(16200,32400):
        cf = 6
    elif x.between(1620,16200):
        cf = 4
    else:
        cf = 2

    return cf
