def get_data():
    import cx_Oracle
    con = cx_Oracle.connect('ADPDS_IMPACT_APP/adpds1280app@DW1280.HOFFMAN.DS.ADP.COM')
    print (con.version)
    cursor = con.cursor()
    sql="select * from sched_request where (status='New'and requestor is null) and rownum=1"
    number_of_rows = cursor.execute(sql);
    for r in number_of_rows:
        print(" -- ", r[0])
        return(r[0])
    print(number_of_rows)
    con.close()

def get_Account_From_Party(party_number):
    import cx_Oracle
    con = cx_Oracle.connect('ADPDS_Q2C_APP/adpds1280app@DS1280.HOFFMAN.DS.ADP.COM')
    print(con.version)
    cursor = con.cursor()
    str_partynumber = str(party_number)
    sql = "select Account_name from apps.hz_cust_accounts_all where party_id ='"+str_partynumber+"'"
    number_of_rows = cursor.execute(sql);
    for r in number_of_rows:
        print(" -- ", r[0])
        return (r[0])

def get_PartyID_From_Accountname(Account_Name):
    import cx_Oracle
    con = cx_Oracle.connect('ADPDS_Q2C_APP/adpds1280app@DS1280.HOFFMAN.DS.ADP.COM')
    print("Connected to Oracle Database Vesrion: ",con.version)
    cursor = con.cursor()
    str_partynumber = str(Account_Name)
    sql = "select party_id from apps.hz_cust_accounts_all where Account_name ='" + Account_Name + "'"
    number_of_rows = cursor.execute(sql);
    for r in number_of_rows:
        #print(" -- ", r[0])
        return (r[0])


#get_PartyID_From_Accountname('BRAMAN CADILLAC')