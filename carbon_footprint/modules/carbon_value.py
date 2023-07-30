
def electric_bill(x):
    """Calculates carbon mass for electricity consumption"""
    return round(x*105*0.45359237,2)

def monthly_gas(x):
    """Calculates carbon emissions for gas bill"""
    return round(x*105*0.45359237, 2)

def oil_spent(x):
    """Calculates carbon emissions for oil"""
    return round(x*113*0.45359237, 2)

def fuel_spent(x):
    """Calculates carbon emissions for fuel spent"""
    return round(x*0.79*0.45359237, 2)

def misc_CF(x):
    """Number of members in the house"""
    cf = 0
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

    return round(cf*0.45359237, 2)

def house_size(x):
    """Calculate carbon footprint based on size of home"""
    cf = 0
    if x == 'large':
        cf = 10
    elif x == 'medium':
        cf = 7
    elif x == 'small':
        cf = 4
    else:
        cf = 2

    return round(cf*0.45359237, 2)

def diet(x):
    """Calculate carbon mass based on type of diet"""
    cf = 0
    if x == 'daily':
        cf = 10
    elif x == 'few':
        cf = 8
    elif x == 'vegeterian':
        cf = 4
    elif x == 'vegan' or x == 'wild meat':
        cf = 2

    return round(cf*0.45359237, 2)

def machine(x):
    """Calculate carbon footprint based on machine runtime"""
    cf = 0
    if x > 9:
        cf = 3
    elif x in range(4,9):
        cf = 2
    elif x in range(1,3):
        cf = 1
    else :
        cf = 0

    return round(cf*0.45359237, 2)

def new_items(x):
    """Calculate carbon footprint based on items bought each year"""
    cf = 0
    if x > 7:
        cf = 10
    elif x in range(5,7):
        cf = 8
    elif x in range(3,5):
        cf = 6
    elif x < 3:
        cf = 4
    else:
        cf = 2

    return round(cf*0.45359237, 2)

def garbage_mass(x):
    """Calculate carbon footprint based on garbage produced"""
    cf = 0
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

    return round(cf*0.45359237, 2)

def waste_recycle(x):
    """Add carbon mass based on waste recycled"""
    cf = 0
    if x == 0:
        cf = 24
    else:
        cf = 20

    return round(cf*0.45359237, 2)

def public_transport(x):
    """Add carbon mass for public transportation usage"""
    cf = 0
    if x > 32400:
        cf = 12
    elif x in range(24300,32400):
        cf = 10
    elif x in range(16200,32400):
        cf = 6
    elif x in range(1620,16200):
        cf = 4
    else:
        cf = 2

    return round(cf*0.45359237, 2)


