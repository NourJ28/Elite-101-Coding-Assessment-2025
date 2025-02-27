tables_data = [
    {"table_id": 1, "seats": 2, "open": False},
    {"table_id": 2, "seats": 4, "open": True},
    {"table_id": 3, "seats": 6, "open": False},
]
def problem_3(tables, party_size):
    opentables = []
    for table in tables:
        if not table["open"] and table["seats"] > party_size:
            return f"Table {table['table_id']} is closed"
        if table["open"] and table["seats"] <= party_size:
            return f"Table {table['table_id']} is open"



print("2: one table for party size 2 =", problem_3(tables_data, 2))