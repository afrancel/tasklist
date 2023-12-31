#definir la variable que referenciamos antes 'instructions'
#escribiremos nuestra lista de instrucciones para SQL

instructions = {
    'SET FOREING_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREING_KEY_CHECKS=1;',

    """
        CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
        )
    """,
    """
    CREATE TABLE todo(
        id INT PRIMARY KEY AUTO_INCREMENT,
        created_by INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL,
        FOREING KEY (created_by) REFERENCES user (id)
    )
    """
}