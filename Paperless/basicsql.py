import sqlite3

conn = sqlite3.connect('mydatabase.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS job_form (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            tel TEXT,
            position TEXT)""")


def insert_job(fullname,tel,position):
    with conn:
        command = 'INSERT INTO job_form VALUES (?,?,?,?)'
        c.execute(command,(None,fullname,tel,position))
    conn.commit()
    print('Save')

# insert_job('test','0899999999','admin')

def view_job():
    with conn:
        command = 'SELECT * FROM job_form'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result
# view_job()

def update_job(tel,field,newvalue):
    with conn:
        command = 'UPDATE job_form SET {} = (?) WHERE tel=(?)'.format(field)
        c.execute(command,(newvalue,tel))
    conn.commit()

# update_job('0867799259','fullname','สิรภพ อนุชาติบุตร')
# update_job('0867799259','position','Administrator')

def delete_job(tel):
    with conn:
        command = 'DELETE FROM job_form WHERE tel=(?)'
        c.execute(command,([tel]))
    conn.commit()

# delete_job('0899999999')
