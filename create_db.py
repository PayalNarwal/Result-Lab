import sqlite3 
def create_db():
    con=sqlite3.connect(database="student_result_management.db")
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS course2(name text,duration text,charges text,description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student_record(roll INTEGER ,name text,email text,gender text,dob text,contact text,admission text, Course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS examrecord(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,course text,semester text,examination text,sub1 text,sub2 text,sub3 text,sub4 text,sub5 text,sub6 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS final_result(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,course text,sub1 text,sub2 text,sub3 text,sub4 text,sub5 text,sub6 text,obt_marks text,total_marks text,percentage text)")
    con.commit()
    
    # cur.execute("delete from final_result")
    # con.commit()

    # cur.execute("CREATE TABLE IF NOT EXISTS report(cid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    # con.commit()

create_db()

