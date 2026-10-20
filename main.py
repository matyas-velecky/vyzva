import sys
import csv
import json

import pandas as pd
from rich.console import Console
from rich.align import Align
from rich.table import Table

console = Console()

def import_csv(filename):
    with open(filename, "r", encoding="utf-8", newline="") as file:
        df = pd.read_csv(file)
        return df
        
def table_make(df):
    table = Table(title="Dochádzka", show_lines=True)
    for column in df.columns:
        table.add_column(str(column), style="cyan")

    for _, row in df.iterrows():
        table.add_row(*[str(value) for value in row])
    return table

def menu(num):
    file = import_csv('./dochazka.csv')
    if num == 1:
        console.print(table_make(file))
        return True
    if num == 2:
        file = json.dump()
        return True
    if num == 3:
        
        return True
    if num == 4:
        
        return True
    if num == 0:
        console.print()
        return False

def main():
    while True:
        console.print("[bold red]MENU[/bold red]")
        console.print("Volba 1) Vypis tabulku")
        console.print("Volba 2) Konvertovat do Json")
        console.print("Volba 3) Vypsat zamestance mesice")
        console.print("Volba 4) Vypsat jmeny seznam zamestnancu")
        console.print("Volba 0) Konec")
        input_num = int(input("Zadej cislo"))
        if(menu(input_num) == False):
            break



if __name__ == "__main__":
    main()
