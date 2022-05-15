from sqlalchemy import delete
from sqlalchemy.orm import Session

from source_table import SourceTable, DestinationTable, engine_x, engine_y


def move_data_x_to_y(**kwargs):
    with Session(engine_x) as session_x, Session(engine_y) as session_y:
        select_sql = session_x.query(SourceTable).where(SourceTable.sale_value > 5000)
        dest_rows = []
        for sale in select_sql:
            dest_rows.append(
                DestinationTable(
                    creation_date=sale.creation_date,
                    sale_value=sale.sale_value,
                )
            )
        session_y.add_all(dest_rows)
        delete_sql = delete(SourceTable).where(SourceTable.sale_value > 5000)
        session_x.execute(delete_sql)
        session_y.commit()
        session_x.commit()
