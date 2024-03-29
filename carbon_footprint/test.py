from rich.console import Console
from rich.layout import Layout
from rich.bar import Bar
from rich.progress_bar import ProgressBar
from rich.panel import Panel
from rich.columns import Columns
from modules.carbon_value import *

rc = Console()

# Initial carbon footprint
CF = 0

CF = electric_bill(250) + monthly_gas(151) + oil_spent(3) + fuel_spent(1) + misc_CF(3) + house_size('apt') + diet('few') + machine(5) + new_items(0) + garbage_mass(1) + waste_recycle(0) + public_transport(2000)

pc = Panel.fit(Columns(["This month's carbon footprint : {:.2f} lbs".format(CF),
    "Carbon footprint from electricity : {:.2f} lbs | {:.2f}%".format(electric_bill(250), electric_bill(250)*100/CF), ProgressBar(100, electric_bill(250)*100/CF),
    "Carbon footprint from gas : {:.2f} lbs | {:.2f}%".format(monthly_gas(151), monthly_gas(151)*100/CF), ProgressBar(100, monthly_gas(151)*100/CF),
    "Carbon footprint from oil usage : {:.2f} lbs | {:.2f}%".format(oil_spent(3), oil_spent(3)*100/CF), ProgressBar(100, oil_spent(3)*100/CF),
    "Carbon footprint from fuel usage : {:.2f} lbs | {:.2f}%".format(fuel_spent(1), fuel_spent(1)*100/CF), ProgressBar(100, fuel_spent(1)*100/CF),
    "Carbon footprint from miscellaneous : {:.2f} lbs | {:.2f}%".format(misc_CF(3), misc_CF(3)*100/CF), ProgressBar(100, misc_CF(3)*100/CF),
    "Carbon footprint by house type : {:.2f} lbs | {:.2f}%".format(house_size('apt'), house_size('apt')*100/CF), ProgressBar(100, house_size('apt')*100/CF),
    "Carbon footprint by diet type : {:.2f} lbs | {:.2f}%".format(diet('few'), diet('few')*100/CF), ProgressBar(100, diet('few')*100/CF),
    "Carbon footprint by washing machine runtime : {:.2f} lbs | {:.2f}%".format(machine(5), machine(5)*100/CF), ProgressBar(100, machine(5)*100/CF),
    "Carbon footprint by items bought : {:.2f} lbs | {:.2f}%".format(new_items(0), new_items(0)*100/CF), ProgressBar(100, new_items(0)*100/CF),
    "Carbon footprint by garbage produced : {:.2f} lbs | {:.2f}%".format(garbage_mass(1), garbage_mass(1)*100/CF), ProgressBar(100, garbage_mass(1)*100/CF),
    "Carbon footprint from waste recycling : {:.2f} lbs | {:.2f}%".format(waste_recycle(0), waste_recycle(0)*100/CF), ProgressBar(100, waste_recycle(0)*100/CF),
    "Carbon footprint from public transport usage : {:.2f} lbs | {:.2f}%".format(public_transport(2000),
        public_transport(2000)*100/CF), ProgressBar(100, public_transport(2000)*100/CF)]),
    title="Monthly carbon footprint",
    width=50,
    style="yellow",
    border_style="red"
)

rc.log(pc)
