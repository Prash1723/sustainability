from rich.console import Console
from rich.layout import Layout
from rich.bar import Bar
from rich.progress_bar import ProgressBar
from rich.panel import Panel
from rich.columns import Columns

rc = Console()

layout = Layout()

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

def newspaper_recycle():
    """Adds newspaper waste """
    return 184

def metal_recycle():
    """Calculates carbon emissions for aluminium and tin recycling"""
    return 166

def misc_CF():
    """Miscellaneous emission"""
    return 1

CF = electric_bill(500) + monthly_gas(293) + oil_spent(5) + fuel_spent(1) + newspaper_recycle() + metal_recycle() + misc_CF()

pc = Panel.fit(Columns(["This month's carbon footprint : {:.2f} Kg".format(CF), 
    "Carbon footprint from electricity : {:.2f} Kg | {:.2f}%".format(electric_bill(500), electric_bill(500)*100/CF), ProgressBar(100, electric_bill(500)*100/CF),
    "Carbon footprint from gas : {:.2f} Kg | {:.2f}%".format(monthly_gas(293), monthly_gas(293)*100/CF), ProgressBar(100, monthly_gas(300)*100/CF),
    "Carbon footprint from oil usage : {:.2f} Kg | {:.2f}%".format(oil_spent(5), oil_spent(5)*100/CF), ProgressBar(100, oil_spent(5)*100/CF),
    "Carbon footprint from fuel usage : {:.2f} Kg | {:.2f}%".format(fuel_spent(1), fuel_spent(1)*100/CF), ProgressBar(100, fuel_spent(1)*100/CF),
    "Carbon footprint from not recycling newspaper : {:.2f} Kg | {:.2f}%".format(newspaper_recycle(), newspaper_recycle()*100/CF), ProgressBar(100, newspaper_recycle()*100/CF),
    "Carbon footprint from not recycling metal : {:.2f} Kg | {:.2f}%".format(metal_recycle(), metal_recycle()*100/CF), ProgressBar(100, metal_recycle()*100/CF),
    "Carbon footprint from miscellaneous : {:.2f} Kg | {:.2f}%".format(misc_CF(), misc_CF()*100/CF), ProgressBar(100, misc_CF()*100/CF)]),
    title="Monthly carbon footprint", 
    width=50,
    style="yellow",
    border_style="red"
)

rc.log(pc)
