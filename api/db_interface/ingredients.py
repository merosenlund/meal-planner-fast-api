import psycopg
from psycopg import sql
from psycopg.rows import dict_row


def get_ingredient(ingredient_id):
    with psycopg.connect(row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM ingredient
                WHERE ingredient_id = %s
                """, [ingredient_id]
            )
            ingredient = cur.fetchone()
    return ingredient


def get_all_ingredients():
    with psycopg.connect(row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM ingredient
                """,
            )
            ingredients = cur.fetchall()
    return ingredients


def add_ingredient(ingredient):
    with psycopg.connect(row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO ingredient (ingredient_name, unit_of_measure, ingredient_type)
                VALUES (%s, %s, %s)
                RETURNING ingredient_id, ingredient_name, unit_of_measure, ingredient_type
                """, [ingredient.name, ingredient.unit_of_measure, ingredient.type]
            )
            ingredient = cur.fetchone()
    return ingredient


def update_ingredient(ingredient_id, data):
    values = list(data.values())
    query = sql.SQL("""
                    UPDATE ingredient SET ({}) = ROW({})
                    WHERE ingredient_id = %s
                    RETURNING ingredient_id, ingredient_name, unit_of_measure, ingredient_type
                    """).format(
                        sql.SQL(", ").join(map(sql.Identifier, list(data.keys()))),
                        sql.SQL(", ").join(sql.Placeholder() * len(values))
                    )
    with psycopg.connect(row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                query, [*values, ingredient_id]
            )
            ingredient = cur.fetchone()
    return ingredient