DROP TABLE IF EXISTS recipe;
CREATE TABLE recipe (
  recipe_id SERIAL PRIMARY KEY,
  recipe_name varchar(50),
  is_active boolean DEFAULT TRUE
);

CREATE TYPE ingredient_types AS ENUM ('STANDARD', 'FRUIT', 'VEGGIE');

DROP TABLE IF EXISTS ingredient;
CREATE TABLE ingredient (
  ingredient_id SERIAL PRIMARY KEY,
  ingredient_name varchar(50),
  unit_of_measure varchar(10),
  ingredient_type ingredient_types DEFAULT 'STANDARD'
);

DROP TABLE IF EXISTS recipe_ingredient;
CREATE TABLE recipe_ingredient (
  recipe_id integer REFERENCES recipe,
  ingredient_id integer REFERENCES ingredient,
  serving_size real,
  CONSTRAINT positive_serving_size CHECK (serving_size >= 0),
  PRIMARY KEY (recipe_id, ingredient_id)
);

DROP TABLE IF EXISTS meal_order;
CREATE TABLE meal_order (
  meal_order_id SERIAL PRIMARY KEY,
  is_complete boolean DEFAULT FALSE
);

DROP TABLE IF EXISTS meal;
CREATE TABLE meal (
  meal_id SERIAL PRIMARY KEY,
  meal_ingredient integer,
  meal_date timestamp,
  recipe_id integer REFERENCES recipe,
  planned smallint,
  actual smallint,
  meal_order_id integer REFERENCES meal_order,
  fruit_id integer REFERENCES ingredient,
  fruit_serving_size real,
  veggie_id integer REFERENCES ingredient,
  veggie_serving_size real
);

DROP TABLE IF EXISTS meal_ingredient;
CREATE TABLE meal_ingredient (
  meal_id integer REFERENCES meal,
  ingredient_id integer REFERENCES ingredient,
  needed smallint,
  put_out smallint,
  left_over smallint,
  PRIMARY KEY (meal_id, ingredient_id)
);
