tables_data = [
    {"table_id": 9999, "seats": 2, "open": False},
    {"table_id": 1111, "seats": 4, "open": True},
    {"table_id": 2222, "seats": 6, "open": False},
]
def table_for_size(tables, party_size):
    open_tables = []
    for table in tables:
        if not table["open"] and table["seats"] >= party_size:
            open_tables.append(table["table_id"])
    return open_tables



print("3: all tables that are not for party size with 2 seats are =", table_for_size(tables_data, 2))