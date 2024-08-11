CREATE SEQUENCE tb_test_id_seq;

CREATE TABLE tb_test (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('tb_test_id_seq'),
    title VARCHAR(255),
    message VARCHAR(255)
);

INSERT INTO tb_test (title, message) VALUES
  ('test_title1', 'test_message1'),
  ('test_title2', 'test_message2');