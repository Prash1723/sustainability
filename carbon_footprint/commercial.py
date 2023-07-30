from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.columns import Columns

import pandas as pd

from modules.carbon_value import *

rc = Console()

# Read data
df = pd.read_csv(r'data/office_data.csv')

df1 = df.groupby('Name').apply(lambda s: pd.Series({
    'electricity_cf': s['Electricity'].apply(electric_bill),
    'gas_cf': s['Gas'].apply(monthly_gas),
    'oil_cf': s['Oil'].apply(oil_spent),
    'fuel_cf': s['Fuel'].apply(fuel_spent),
    'misc_cf': s['Miscellaneous'].apply(misc_CF),
    'house_cf': s['House_size'].apply(house_size),
    'diet_cf': s['Diet'].apply(diet),
    'wm_cf': s['Washing_Machine_freq'].apply(machine),
    'dw_cf': s['Dishwasher_freq'].apply(machine),
    'items_cf': s['Items_bought'].apply(new_items),
    'garbage_cf': s['Garbage_produced'].apply(garbage_mass),
    'waste_cf': s['Waste_recycled'].apply(waste_recycle),
    'transport_cf': s['public_transport'].apply(public_transport)
    })).reset_index()

df1['Carbon_footprint'] = df1['electric_cf'] + df1['gas_cf'] + df1['oil_cf'] + df1['fuel_cf'] + df1['misc_cf'] + df1['house_cf'] + df1['diet_cf'] + df1['wm_cf'] + df1['dw_cf'] + df1['items_cf'] + df1['garbage_cf'] + df1['waste_cf'] + df1['transport_cf']

rc.log(df1[['Name', 'Carbon_footprint']])
