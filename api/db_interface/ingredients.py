import psycopg


def get_all_ingredients():
    with psycopg.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM ingredient
                """,
            )
            ingredients = cur.fetchall()
    return ingredients


def add_ingredient(ingredient):
    with psycopg.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO ingredient (ingredient_name, unit_of_measure, ingredient_type)
                VALUES (%s, %s, %s)
                RETURNING (ingredient_id, ingredient_name, unit_of_measure, ingredient_type)
                """, [ingredient.name, ingredient.unit_of_measure, ingredient.type]
            )
            ingredient = cur.fetchone()
    return ingredient