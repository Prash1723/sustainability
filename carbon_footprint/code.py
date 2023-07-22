from rich.console import Console
from rich.layout import Layout
from rich.bar import Bar
from rich.progress_bar import ProgressBar
from rich.panel import Panel
from rich.columns import Columns

rc = Console()

# Initial carbon footprint
CF = 0

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

def misc_CF():
    """Miscellaneous emission"""
    return 8

def apt_size():
    """Calculate carbon mass based on size of home"""
    return 2

def diet():
    """Calculate carbon mass based on type of diet"""
    return 8

def washing_machine():
    """Calculate carbon mass based on washing machine runtime"""
    return 2

def new_items():
    """Calculate carbon mass based on items bought each year"""
    return 6

def garbage_mass():
    """Calculate carbon mass based on garbage produced"""
    return 5

def waste_recycle():
    """Add carbon mass based on waste recycled"""
    return 24

def public_transport():
    """Add carbon mass for public transportation usage"""
    return 2

CF = electric_bill(250) + monthly_gas(151) + oil_spent(3) + fuel_spent(1) + misc_CF() + apt_size() + diet() + washing_machine() + new_items() + garbage_mass() + waste_recycle() + public_transport()

pc = Panel.fit(Columns(["This month's carbon footprint : {:.2f} lbs".format(CF), 
    "Carbon footprint from electricity : {:.2f} lbs | {:.2f}%".format(electric_bill(250), electric_bill(250)*100/CF), ProgressBar(100, electric_bill(250)*100/CF),
    "Carbon footprint from gas : {:.2f} lbs | {:.2f}%".format(monthly_gas(151), monthly_gas(151)*100/CF), ProgressBar(100, monthly_gas(151)*100/CF),
    "Carbon footprint from oil usage : {:.2f} lbs | {:.2f}%".format(oil_spent(3), oil_spent(3)*100/CF), ProgressBar(100, oil_spent(3)*100/CF),
    "Carbon footprint from fuel usage : {:.2f} lbs | {:.2f}%".format(fuel_spent(1), fuel_spent(1)*100/CF), ProgressBar(100, fuel_spent(1)*100/CF),
    "Carbon footprint from miscellaneous : {:.2f} lbs | {:.2f}%".format(misc_CF(), misc_CF()*100/CF), ProgressBar(100, misc_CF()*100/CF),
    "Carbon footprint by house type : {:.2f} lbs | {:.2f}%".format(apt_size(), apt_size()*100/CF), ProgressBar(100, apt_size()*100/CF),
    "Carbon footprint by diet type : {:.2f} lbs | {:.2f}%".format(diet(), diet()*100/CF), ProgressBar(100, diet()*100/CF),
    "Carbon footprint by washing machine runtime : {:.2f} lbs | {:.2f}%".format(washing_machine(), washing_machine()*100/CF), ProgressBar(100, washing_machine()*100/CF),
    "Carbon footprint by items bought : {:.2f} lbs | {:.2f}%".format(new_items(), new_items()*100/CF), ProgressBar(100, new_items()*100/CF),
    "Carbon footprint by garbage produced : {:.2f} lbs | {:.2f}%".format(garbage_mass(), garbage_mass()*100/CF), ProgressBar(100, garbage_mass()*100/CF),
    "Carbon footprint from waste recycling : {:.2f} lbs | {:.2f}%".format(waste_recycle(), waste_recycle()*100/CF), ProgressBar(100, waste_recycle()*100/CF),
    "Carbon footprint from public transport usage : {:.2f} lbs | {:.2f}%".format(public_transport(),
        public_transport()*100/CF), ProgressBar(100, public_transport()*100/CF)]),
    title="Monthly carbon footprint", 
    width=50,
    style="yellow",
    border_style="red"
)

rc.log(pc)
